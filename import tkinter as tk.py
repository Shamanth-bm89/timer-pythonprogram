import tkinter as tk
from tkinter import messagebox
import threading
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Timer App")

        self.seconds_var = tk.StringVar()
        self.seconds_var.set("60")  # default value

        self.label = tk.Label(root, text="Timer:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, textvariable=self.seconds_var)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=20)

        self.timer_label = tk.Label(root, text="")
        self.timer_label.pack()

    def start_timer(self):
        try:
            seconds = int(self.seconds_var.get())
            if seconds <= 0:
                messagebox.showwarning("Invalid Input", "Please enter a positive number of seconds.")
                return

            self.start_button.config(state="disabled")  # Disable the button during the timer

            self.timer_thread = threading.Thread(target=self.run_timer, args=(seconds,))
            self.timer_thread.start()

        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number of seconds.")

    def run_timer(self, seconds):
        for i in range(seconds, 0, -1):
            time.sleep(1)
            self.timer_label.config(text=f"Time remaining: {i} seconds")
            self.root.update()

        self.timer_label.config(text="Time's up!")
        messagebox.showinfo("Timer Complete", "Time's up!")
        self.start_button.config(state="normal")  # Enable the button after the timer

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
