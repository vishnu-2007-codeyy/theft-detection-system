🚨 AI Smart Security System with Telegram Alerts

🔒 Real-time AI security system that detects motion and faces through a webcam and sends instant Telegram alerts with captured images.

📌 Overview

The AI Smart Security System is a computer-vision-based monitoring system built with Python.

The system continuously analyzes your webcam feed to detect:

Motion in the environment

Human faces

Suspicious activity

When a face is detected:

1️⃣ A photo of the intruder is captured
2️⃣ The image is saved locally
3️⃣ An instant alert with the photo is sent to Telegram

This project demonstrates real-time computer vision, automation, and notification systems.

✨ Key Features
Feature	Description
📸 Real-time Face Detection	Detects human faces using OpenCV Haar Cascade
🟢 Motion Detection	Identifies movement within the camera frame
🔴 Intruder Detection	Highlights detected faces in real time
📱 Telegram Alerts	Sends instant notifications with captured photos
💾 Auto Image Storage	Saves intruder photos locally
⏱ Alert Cooldown	Prevents notification spam
🧪 Test Mode	Send test alerts manually
⌨️ Keyboard Controls	Easy control with keyboard shortcuts
📊 Live Status Display	Shows detection information on screen
🛠 Technology Stack
Component	Technology
Programming Language	Python 3.10+
Computer Vision	OpenCV
Face Detection	Haar Cascade Classifier
Motion Detection	Background Subtraction (MOG2)
Notifications	Telegram Bot API
Data Processing	NumPy

Development Environment:
Visual Studio Code

🏗 System Architecture
Webcam Feed
      │
      ▼
Frame Capture
      │
      ▼
Motion Detection
 (Green Box)
      │
      ▼
Face Detection
 (Red Box)
      │
      ▼
Alert System
      │
      ▼
Telegram Notification
      │
      ▼
Mobile Phone Alert
📁 Project Structure
theft-detection-system/

main_theft.py
theft_detector.py
telegram_notifier.py
main_activity.py
activity_classifier.py
camera_test.py
requirements.txt
README.md

intruders/
    intruder_20240305_153045.jpg

__pycache__/   (ignored in Git)
⚙ Installation
1️⃣ Clone the Repository
git clone https://github.com/vishnu-2007-codeyy/theft-detection-system.git
cd theft-detection-system
2️⃣ Create Virtual Environment (Recommended)

Windows

python -m venv venv
venv\Scripts\activate

Linux / Mac

python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🤖 Telegram Bot Setup
Step 1 — Create a Telegram Bot

Open Telegram and search for @BotFather

Run:

/newbot

Choose:

Bot Name

Bot Username (must end with bot)

Copy the Bot Token provided.

Step 2 — Get Your Chat ID

Send any message to your bot.

Open in browser:

https://api.telegram.org/botYOUR_TOKEN/getUpdates

Find:

"chat":{"id":123456789}

That number is your Chat ID.

Step 3 — Add Credentials

Edit main_theft.py:

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
🚀 Usage

Start theft detection:

python main_theft.py

Start activity detection (optional):

python main_activity.py

Test camera:

python camera_test.py
🎮 Keyboard Controls
Key	Function
q	Quit program
t	Send test alert

| Increase alert cooldown

| Decrease cooldown

📊 Sample Console Output
🔒 Security System Initialized
⏱ Alert Cooldown: 30 seconds

🚨 SECURITY MONITORING ACTIVE

🟢 Green box = Motion
🔴 Red box = Face detected

Press 'q' to quit
Press 't' for test alert

🚨 Intruder detected!
📸 Photo captured
📱 Telegram alert sent
🔧 Troubleshooting
Problem	Solution
Camera not opening	Close other apps using camera
No Telegram alerts	Verify token and chat ID
Too many alerts	Increase cooldown value
Low detection accuracy	Improve lighting conditions
🔒 Security Best Practices

Never upload Telegram tokens to GitHub

Use .gitignore for sensitive files

Place camera at entry points

Ensure proper lighting

Backup intruder images regularly

Example .gitignore

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
Push to the branch
Open a Pull Request

Possible improvements:

Facial recognition for known people

Night-vision mode

Email alerts

Cloud storage integration

Multi-camera monitoring

📜 License

MIT License

Copyright (c) 2026 Vishnu

Permission is granted to use, modify and distribute this software.

📧 Contact

Developer: Vishnu

GitHub:
https://github.com/vishnu-2007-codeyy/theft-detection-system

⭐ Support

If you find this project useful:

⭐ Star the repository
📢 Share it
🤝 Contribute improvements