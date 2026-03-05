🚨 AI Smart Security System with Telegram Alerts

A real-time computer vision security system that detects motion and faces using your webcam and sends instant Telegram alerts with photos.

📌 Overview

This project is an AI-powered security monitoring system built with Python and computer vision.

The system continuously monitors a webcam feed and performs:

Motion detection

Face detection

Intruder alert notification

When a face is detected:

The system captures an image

The image is saved locally

A Telegram alert with the photo is sent instantly

This project demonstrates real-time computer vision, automation, and notification systems.

✨ Features

Real-time face detection using OpenCV

Motion detection using background subtraction

Intruder alerts sent to Telegram

Automatic image capture of intruders

Configurable alert cooldown

Test mode for sending alerts

Keyboard controls for system operation

🛠 Technology Stack
Component	Technology
Language	Python 3.10+
Computer Vision	OpenCV
Face Detection	Haar Cascade
Motion Detection	MOG2 Background Subtraction
Notifications	Telegram Bot API
Data Processing	NumPy

Development environment:
Visual Studio Code

🏗 System Workflow
Webcam Feed
     ↓
Frame Capture
     ↓
Motion Detection
     ↓
Face Detection
     ↓
Intruder Detection
     ↓
Image Capture
     ↓
Telegram Alert
     ↓
Mobile Notification
📁 Project Structure
theft-detection-system/

main_theft.py              # Main security monitoring script
theft_detector.py          # Intruder detection logic
telegram_notifier.py       # Telegram alert system
main_activity.py           # Activity detection module
activity_classifier.py     # Activity classification
camera_test.py             # Camera testing script
requirements.txt           # Python dependencies
README.md                  # Project documentation

intruders/                 # Saved intruder images
⚙ Installation
1️⃣ Clone the repository
git clone https://github.com/vishnu-2007-codeyy/theft-detection-system.git
cd theft-detection-system
2️⃣ Create virtual environment (optional)

Windows

python -m venv venv
venv\Scripts\activate

Linux / Mac

python3 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
🤖 Telegram Bot Setup
Step 1 — Create a bot

Open Telegram and search @BotFather

Run the command:

/newbot

Choose a bot name and username.

Copy the bot token you receive.

Step 2 — Get your Chat ID

Send a message to your bot.

Open this URL:

https://api.telegram.org/botYOUR_TOKEN/getUpdates

Look for:

"chat":{"id":123456789}

That number is your Chat ID.

Step 3 — Add credentials

Edit the file main_theft.py:

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
🚀 Usage

Run the main security system:

python main_theft.py

Optional modules:

Activity detection:

python main_activity.py

Camera test:

python camera_test.py
🎮 Keyboard Controls
Key	Action
q	Quit the program
t	Send test Telegram alert

| Increase alert cooldown |

| Decrease alert cooldown |

📊 Example Output

Console output:

Security system initialized
Alert cooldown: 30 seconds

Monitoring started...

Face detected
Intruder alert triggered
Photo captured
Telegram notification sent
🔧 Troubleshooting
Problem	Solution
Camera not opening	Close other applications using the camera
No Telegram alerts	Check bot token and chat ID
Too many alerts	Increase alert cooldown
Low detection accuracy	Improve lighting conditions
🔒 Security Notes

Never upload Telegram tokens to GitHub

Use .gitignore to hide sensitive files

Position camera at entry points

Ensure good lighting for detection

Example .gitignore:

__pycache__/
intruders/
*.jpg
.env
🤝 Contributing

Contributions are welcome.

Steps:

Fork the repository

Create a new branch

Commit your changes

Push the branch

Create a Pull Request

Possible improvements:

Facial recognition for known users

Night vision mode

Email alerts

Cloud storage integration

Multiple camera support

📜 License

MIT License

Copyright (c) 2026 Vishnu

📧 Contact

Developer: Vishnu

GitHub Repository:

https://github.com/vishnu-2007-codeyy/theft-detection-system

⭐ Support

If you like this project:

⭐ Star the repository

📢 Share the project

🤝 Contribute improvements
