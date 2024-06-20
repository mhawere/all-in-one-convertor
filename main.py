from fastapi import FastAPI, File, UploadFile, BackgroundTasks, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn
import os
import uuid
from conversion import convert_video, conversion_progress
from fastapi.middleware.cors import CORSMiddleware
import starlette.status

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://0.0.0.0:8080",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploadfile/")
async def upload_file(background_tasks: BackgroundTasks, file: UploadFile = File(...), input_format: str = Form(...), output_format: str = Form(...), request: Request = None):
    input_file_location = f"files/{file.filename}"
    os.makedirs(os.path.dirname(input_file_location), exist_ok=True)
    with open(input_file_location, "wb") as file_object:
        file_object.write(file.file.read())
    task_id = str(uuid.uuid4())
    output_file_location = f"static/converted_{task_id}.{output_format}"  # Include task ID and output format in the output file name
    # Run conversion in background to avoid blocking
    background_tasks.add_task(convert_video, input_file_location, output_file_location, task_id, input_format, output_format)
    return templates.TemplateResponse("redirect.html", {"request": request, "task_id": task_id})

@app.get("/progress/{task_id}")
async def get_progress(task_id: str):
    progress = conversion_progress.get(task_id, {
        "progress": 0,
        "elapsed_time": 0,
        "estimated_time_remaining": "Unknown",
        "conversion_rate": "Unknown"
    })
    return JSONResponse(progress)

@app.get("/progress_page/{task_id}")
async def progress_page(request: Request, task_id: str):
    return templates.TemplateResponse("progress.html", {"request": request, "task_id": task_id})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=0000, reload=True)
