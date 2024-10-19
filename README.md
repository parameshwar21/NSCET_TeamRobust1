Team Name: Team Robust 01


College: Nadar Saraswathi College of Engineering and Technology



Team Members:

Parameshwar NS - Team Leader


A Surya Prakash - Team Member


P Gowsik - Team Member


Real-Time Sign Language Translator for Virtual Meetings

Project Overview

This project aims to create a real-time sign language translator for virtual meetings, making online interactions more accessible for deaf and hard-of-hearing participants. The system captures spoken language during the meeting, converts it to text, and then translates that text into sign language. A 3D animated avatar performs the sign language gestures, displayed alongside the virtual meeting.

Features


1. Real-Time Speech-to-Text (STT) Conversion: Converts spoken language into text in real-time using speech recognition technology.
2. Text-to-Sign Language Translation: Translates captured text into sign language and displays it using a 3D avatar.
3. 3D Sign Language Avatar: A virtual avatar that performs sign language gestures corresponding to the meeting’s spoken content.
4. Platform Integration: Easily integrates with virtual meeting platforms such as Zoom and Microsoft Teams.
5. User-Customizable Avatar: Users can adjust the speed, appearance, and other settings of the 3D avatar.
Prerequisites

Ensure the following are installed before running the project:
• Python (version 3.8+)
• pip (Python package manager)
• Unity 3D or Three.js (for creating and controlling the 3D avatar)
• Speech-to-Text API (e.g., Google Cloud Speech API or Azure Speech)
Setup Instructions
1. Clone the Repository
Download the source code from the GitHub repository:
git clone https://github.com/your-username/sign-language-translator.git
cd sign-language-translator
2. Set Up a Virtual Environment
It’s recommended to use a virtual environment for dependency management:
python -m venv venv
Activate the virtual environment:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

3. Install Dependencies
Install the required Python packages using the provided requirements.txt:
pip install -r requirements.txt

4. Configure Speech-to-Text API
Set up your speech-to-text API (e.g., Google Cloud Speech) and store your API credentials in a .env file.
For Google Cloud: export GOOGLE_APPLICATION_CREDENTIALS="path-to-your-credentials.json"

5. Set Up the 3D Avatar System
• Unity 3D Users: Set up a new Unity project and integrate pre-built sign language animations. You can use resources like Mixamo for creating basic human avatar animations.
• Three.js Users: Use Three.js to create and control a 3D model avatar. The animations should correspond to the translated sign language gestures.

6. Run the Application
Start the server to handle speech-to-text conversion and sign language translation:
python app.py
Open a web browser and go to http://127.0.0.1:5000 to access the real-time sign language translator.
Troubleshooting
• Speech Recognition Errors: Ensure that the API key is correctly configured and that your microphone input is clear.
• Avatar Display Issues: Double-check the setup for the 3D avatar system, and ensure that all required animation libraries are installed properly.
Customization
• Modify Avatar Appearance: If using Unity or Three.js, you can customize the avatar’s appearance, speed of signing, and additional visual settings.
• Multiple Sign Languages: The system can be expanded to support multiple sign languages (e.g., ASL, BSL) by modifying the translation models.
Folder Structure

├── app.py                # Main application file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── model/                 # Directory for ML models or datasets
├── static/                # Contains static assets (CSS, JS, etc.)
└── templates/             # HTML templates for the web interface

Contributing
Feel free to contribute to this project by submitting pull requests or opening issues. Be sure to follow best practices for clean code and documentation.
License
This project is licensed under the MIT License. See the LICENSE file for details.
References
• Google Cloud Speech-to-Text API Documentation: https://cloud.google.com/speech-to-text/docs
• Unity 3D: https://unity.com/
• Three.js Documentation: https://threejs.org/docs/
