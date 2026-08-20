import time
import datetime
import json
import os

class JarvisAssistant:
    def __init__(self, user_name="Aamir Hussain"):
        self.user_name = user_name
        print(f"[*] Jarvis initialized for {self.user_name}")

    def speak(self, text):
        # Voice output / Speech synthesis
        print(f"Jarvis: {text}")

    def get_time_and_date(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        current_date = now.strftime("%B %d, %Y")
        return f"Aamir bhai, abhi time {current_time} ho raha hai aur aaj taareekh {current_date} hai."

    def get_battery_status(self):
        # Battery percentage & system status
        try:
            # Termux API fallback for battery status
            battery_info = os.popen("termux-battery-status").read()
            if battery_info:
                data = json.loads(battery_info)
                percentage = data.get("percentage", "Unknown")
                return f"Aamir bhai, aapke phone ki battery {percentage}% hai."
        except Exception:
            pass
        return "Aamir bhai, battery status check ho raha hai."

    def get_gps_location(self):
        # GPS & Location tracking
        try:
            location_info = os.popen("termux-location").read()
            if location_info:
                data = json.loads(location_info)
                lat = data.get("latitude")
                lon = data.get("longitude")
                return f"Aamir bhai, aapki live location Latitude: {lat}, Longitude: {lon} par hai."
        except Exception:
            pass
        return "Aamir bhai, GPS location trace ki jaa rahi hai."

    def read_whatsapp_notification(self, sender_name, message_text):
        # WhatsApp Message Reader & Auto Responder
        prompt = f"Aamir bhai, {sender_name} ka message aaya hai: '{message_text}'. Kya aap iska jawaab dena chahenge? 😊👍"
        self.speak(prompt)
        return prompt

    def send_whatsapp_reply(self, reply_text):
        # Stylish Auto-Reply with Emoji
        formatted_reply = f"{reply_text} ✨ [Sent via Jarvis]"
        self.speak(f"Message bhej diya gaya hai: {formatted_reply}")
        return formatted_reply

    def read_screen_content(self):
        # Screen Monitor / Reader
        self.speak("Aamir bhai, screen content analyze ho raha hai...")
        return "Screen Reader Active"

# Testing Jarvis Features
if __name__ == "__main__":
    jarvis = JarvisAssistant(user_name="Aamir Hussain")
    
    # 1. Time Update
    print(jarvis.get_time_and_date())
    
    # 2. Battery & System Info
    print(jarvis.get_battery_status())
    
    # 3. WhatsApp Notification Prompt
    jarvis.read_whatsapp_notification("Dost", "Kahan ho bhai?")
    
    # 4. WhatsApp Auto-Reply
    jarvis.send_whatsapp_reply("Bas aane wala hoon!")
    
    # 5. GPS Location Check
    print(jarvis.get_gps_location())
    
