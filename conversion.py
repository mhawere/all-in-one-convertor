import subprocess
import re
from tqdm import tqdm
import time
import logging

logging.basicConfig(level=logging.INFO)

conversion_progress = {}
conversion_processes = {}

def convert_video(input_file: str, output_file: str, task_id: str, input_format: str, output_format: str) -> None:
    command = [
        'ffmpeg',
        '-y',  # Overwrite output files without asking
        '-i', input_file,
        '-c:v', 'libx264' if output_format == 'mp4' else 'copy',
        '-c:a', 'aac' if output_format == 'mp4' else 'copy',
        '-b:a', '128k' if output_format == 'mp4' else None,  # Set the audio bitrate if output is mp4
        '-max_muxing_queue_size', '9999',  # Increase the maximum muxing queue size
        '-bufsize', '500M',  # Increase the buffer size
        '-threads', '8',  # Set the number of threads for parallel processing
        output_file
    ]

    command = [arg for arg in command if arg is not None]  # Remove None values from the command list

    process = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines=True)
    conversion_processes[task_id] = process

    total_duration = None
    start_time = time.time()
    progress_bar = None

    for line in process.stderr:
        logging.info(line)

        if 'Duration' in line:
            match = re.search(r'Duration: (\d{2}):(\d{2}):(\d{2}\.\d{2})', line)
            if match:
                hours, minutes, seconds = match.groups()
                total_duration = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
                progress_bar = tqdm(total=total_duration, unit='s', unit_scale=True, desc="Converting")

        if total_duration:
            match = re.search(r'time=(\d{2}):(\d{2}):(\d{2}\.\d{2})', line)
            if match:
                hours, minutes, seconds = match.groups()
                elapsed_time = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
                progress_bar.n = elapsed_time
                progress_bar.refresh()

                conversion_rate = elapsed_time / (time.time() - start_time)
                estimated_time_remaining = (total_duration - elapsed_time) / conversion_rate

                conversion_progress[task_id] = {
                    "progress": (elapsed_time / total_duration) * 100,
                    "elapsed_time": elapsed_time,
                    "estimated_time_remaining": estimated_time_remaining,
                    "conversion_rate": conversion_rate
                }

    process.wait()

    if progress_bar:
        progress_bar.close()

    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, command)

    conversion_progress[task_id] = {
        "progress": 100,
        "elapsed_time": total_duration,
        "estimated_time_remaining": 0,
        "conversion_rate": total_duration / (time.time() - start_time)
    }

def cancel_conversion(task_id: str):
    process = conversion_processes.get(task_id)
    if process:
        process.terminate()
        conversion_progress.pop(task_id, None)
        conversion_processes.pop(task_id, None)
