**Video Conversion Web Application**
This is a web application built with FastAPI that allows users to convert video files to different formats. It provides a user-friendly interface for uploading video files, selecting the desired output format, and downloading the converted files.

**Features**
The main feature for this application is its simplicity, straight up convertor and thats it!
Upload video files through a web interface
Select the desired output format (e.g., MP4, AVI, MKV)
Convert video files using FFmpeg in the background
Track the progress of the video conversion process
Download the converted video files

**Prerequisites**
Before running the application, ensure that you have the following prerequisites installed:

**Python 3.7 or higher**
FFmpeg (available in the system's PATH)

**Installation
**
Step 1: Clone the repository:
git clone https://github.com/your-username/your-repository.git
Step 2: Navigate to the project directory:
cd your-repository
Step 3: Create a virtual environment (optional but recommended):
python -m venv venv
Step 4: Activate the virtual environment:
  for windows:
    venv\Scripts\activate
  for macOS or Linux
    source venv/bin/activate
Step 5: Install the required dependencies:
pip install -r requirements.txt

**Configuration**

Open the main.py file in a text editor.
Modify the origins list to include the allowed origins for CORS (Cross-Origin Resource Sharing). By default, it includes http://localhost and http://localhost:8080. Add any additional origins if required.
Update the host and port values in the uvicorn.run() function call to specify the desired host and port for running the application. By default, it is set to host="0.0.0.0" and port=5555.
Save the changes.

Usage
1. Start the FastAPI server by running the following command:
   python main.py
2. Open a web browser and visit http://localhost:0000 (or the appropriate URL based on your configuration).
3. On the home page, you will see a file upload form. Click the "Choose File" button to select a video file from your local machine.
Select the desired input and output formats from the dropdown menus.
Click the "Upload" button to start the video conversion process.
You will be redirected to a progress page where you can track the progress of the video conversion. The progress bar will indicate the completion percentage, and additional information such as elapsed time, estimated time remaining, and conversion rate will be displayed.
Once the conversion is complete, the progress page will automatically trigger the download of the converted video file. The downloaded file will have the name converted_<task_id>.<output_format>.
You can continue uploading and converting more video files as needed.

Customization

To add support for additional video formats, modify the index.html file and add the desired format options to the <select> elements for input and output formats.
Customize the styling of the web pages by modifying the CSS styles in the HTML files (index.html, progress.html, redirect.html).
Adjust the FFmpeg command parameters in the convert_video function of the conversion.py file to fine-tune the video conversion settings.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.
License
This project is licensed under the MIT License.
Acknowledgements

FastAPI - The web framework used for building the application.
FFmpeg - The powerful multimedia framework used for video conversion.
Jinja2 - The templating engine used for rendering HTML templates.
Bootstrap - The CSS framework used for styling the web pages.

Contact
If you have any questions or inquiries, please contact your-email@example.com.

Feel free to customize the README file based on your specific project details, such as adding additional sections, providing more detailed instructions, or including any other relevant information.
