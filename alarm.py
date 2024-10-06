import time
import winsound
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    alarm_time = entry.get()
    if alarm_time:
        alarm_clock(alarm_time)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid time in HH:MM:SS format.")

def alarm_clock(alarm_time):
    print("Alarm set for:", alarm_time)
    
    while True:
        current_time = time.strftime("%H:%M:%S")
        time_label.config(text=current_time)
        
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Time to Wake Up!")
            winsound.Beep(440, 1000)
            break
        
        root.update()
        time.sleep(1)

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Set Alarm Time (HH:MM:SS):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

time_label = tk.Label(root, text="", font=("Helvetica", 24))
time_label.pack(pady=20)

root.mainloop()

