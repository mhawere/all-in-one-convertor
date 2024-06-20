# Video Conversion Web Application

This web application, built with FastAPI, allows users to convert video files to different formats. It provides a user-friendly interface for uploading video files, selecting the desired output format, and downloading the converted files.

---

## Features

- **Simplicity:** Straightforward video conversion process.
- **Upload:** Upload video files through a web interface.
- **Format Selection:** Select the desired output format (e.g., MP4, AVI, MKV).
- **Conversion:** Convert video files using FFmpeg in the background.
- **Progress Tracking:** Track the progress of the video conversion process.
- **Download:** Download the converted video files.

---

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed:

- **Python 3.7 or higher**
- **FFmpeg** (available in the system's PATH)

---

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repository
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    For Windows:
    ```bash
    venv\Scripts\activate
    ```

    For macOS or Linux:
    ```bash
    source venv/bin/activate
    ```

5. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

---

## Configuration

1. **Open the `main.py` file in a text editor.**
2. **Modify the `origins` list** to include the allowed origins for CORS (Cross-Origin Resource Sharing). By default, it includes `http://localhost` and `http://localhost:8080`. Add any additional origins if required.
3. **Update the `host` and `port` values** in the `uvicorn.run()` function call to specify the desired host and port for running the application. By default, it is set to `host="0.0.0.0"` and `port=5555`.
4. **Save the changes.**

---

## Usage

1. **Start the FastAPI server by running the following command:**

    ```bash
    python main.py
    ```

2. **Open a web browser and visit** `http://localhost:0000` (or the appropriate URL based on your configuration).
3. **On the home page:**
   - Click the "Choose File" button to select a video file from your local machine.
   - Select the desired input and output formats from the dropdown menus.
   - Click the "Upload" button to start the video conversion process.
4. **You will be redirected to a progress page** where you can track the progress of the video conversion. The progress bar will indicate the completion percentage, and additional information such as elapsed time, estimated time remaining, and conversion rate will be displayed.
5. **Once the conversion is complete,** the progress page will automatically trigger the download of the converted video file. The downloaded file will have the name `converted_<task_id>.<output_format>`.
6. **You can continue uploading and converting more video files as needed.**

---

## Customization

- **Add support for additional video formats:**
  Modify the `index.html` file and add the desired format options to the `<select>` elements for input and output formats.
- **Customize the styling of the web pages:**
  Modify the CSS styles in the HTML files (`index.html`, `progress.html`, `redirect.html`).
- **Adjust the FFmpeg command parameters:**
  Modify the `convert_video` function of the `conversion.py` file to fine-tune the video conversion settings.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- **FastAPI:** The web framework used for building the application.
- **FFmpeg:** The powerful multimedia framework used for video conversion.
- **Jinja2:** The templating engine used for rendering HTML templates.
- **Bootstrap:** The CSS framework used for styling the web pages.

---

## Contact

If you have any questions or inquiries, please contact me here :)

---

Feel free to customize this README file based on your specific project details, such as adding additional sections, providing more detailed instructions, or including any other relevant information.
