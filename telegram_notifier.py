"""
Telegram notification module for sending alerts with photos.
"""

import requests
import logging
import cv2
import os
import tempfile

class TelegramNotifier:
    def __init__(self, bot_token=None, chat_id=None):
        """Initialize Telegram bot notifier."""
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        self.enabled = bool(bot_token and chat_id)
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        if self.enabled:
            self.logger.info("Telegram notifier initialized")
    
    def send_notification(self, message, frame=None):
        """Send a notification message with optional photo."""
        if not self.enabled:
            return False
        
        try:
            if frame is not None:
                return self._send_photo(message, frame)
            else:
                return self._send_text(message)
        except Exception as e:
            self.logger.error(f"Failed to send: {e}")
            return False
    
    def _send_text(self, message):
        url = f"{self.base_url}/sendMessage"
        payload = {'chat_id': self.chat_id, 'text': message}
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        return True
    
    def _send_photo(self, message, frame):
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        temp_filename = temp_file.name
        temp_file.close()
        
        cv2.imwrite(temp_filename, frame)
        
        try:
            url = f"{self.base_url}/sendPhoto"
            with open(temp_filename, 'rb') as photo:
                files = {'photo': photo}
                data = {'chat_id': self.chat_id, 'caption': message}
                response = requests.post(url, files=files, data=data, timeout=10)
                response.raise_for_status()
            return True
        finally:
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)