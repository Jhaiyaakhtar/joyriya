
import tkinter as tk
import RPi.GPIO as GPIO

# GPIO পিন নির্দিষ্ট করুন
LED_PIN = 17

# GPIO সেটআপ
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def toggle_light():
    # বর্তমান আলোর অবস্থা অনুমান করুন
    current_state = GPIO.input(LED_PIN)
    # আলোর অবস্থা পরিবর্তন করুন
    GPIO.output(LED_PIN, not current_state)

# Tkinter উইন্ডো তৈরি করুন
root = tk.Tk()
root.title("টচ লাইট অ্যাপ")

# বাটন তৈরি করুন
toggle_button = tk.Button(root, text="টগল লাইট", command=toggle_light)
toggle_button.pack(pady=10)

# উইন্ডো চালু রাখুন
root.mainloop()

# প্রোগ্রাম শেষ করার সময় GPIO মুক্ত করুন
GPIO.cleanup()