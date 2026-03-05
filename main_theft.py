"""
Main Theft Detection System - COMPLETE FIXED VERSION
Run this file to start detection
"""

from telegram_notifier import TelegramNotifier
from theft_detector import TheftDetector

def main():
    """Main function to run theft detection"""
    
    # 🔴 YOUR TELEGRAM DETAILS - VERIFY THESE ARE CORRECT
    TELEGRAM_TOKEN = "8736399122:AAFg2X2kMO5CSSQDFMhLdNoH0ry98vWZXr4"
    CHAT_ID = "7137955785"
    
    print("="*50)
    print("🚀 STARTING THEFT DETECTION SYSTEM")
    print("="*50)
    print(f"📱 Telegram Token: {TELEGRAM_TOKEN[:10]}...")
    print(f"📱 Chat ID: {CHAT_ID}")
    print("="*50)
    
    # Initialize notifier
    notifier = TelegramNotifier(TELEGRAM_TOKEN, CHAT_ID)
    
    # Send startup message
    print("📱 Sending startup notification...")
    notifier.send_notification("🚨 Theft Detection System Started!\n📍 Monitoring your home...")
    
    # Initialize and run detector
    detector = TheftDetector(notifier)
    
    try:
        detector.run()
    except KeyboardInterrupt:
        print("\n🛑 System stopped by user")
        notifier.send_notification("🛑 Theft Detection System Stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        notifier.send_notification(f"❌ System Error: {e}")

if __name__ == "__main__":
    main()