import tkinter as tk
from datetime import datetime, timedelta


class StopwatchApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Секундомер")
        self.root.geometry("400x300")

        self.start_time = None
        self.elapsed_time = timedelta(0)
        self.paused_time = timedelta(0)

        self.time_label = tk.Label(self.root, text="00:00:00.000", font=("Arial", 24))
        self.time_label.pack(pady=20)

        start_button = tk.Button(self.root, text="Старт", command=self.start)
        start_button.pack()

        pause_button = tk.Button(self.root, text="Пауза", command=self.pause)
        pause_button.pack()

        resume_button = tk.Button(self.root, text="Возобновить", command=self.resume)
        resume_button.pack()

        stop_button = tk.Button(self.root, text="Стоп", command=self.stop)
        stop_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def start(self):
        if self.start_time is None:
            current_time = datetime.now()
            self.start_time = current_time
            self.paused_time = current_time
            self.elapsed_time = timedelta(0)

            self.update_time_label()

    def pause(self):
        if self.start_time and self.paused_time == self.start_time:
            self.paused_time = datetime.now()

    def resume(self):
        if self.start_time and self.paused_time != self.start_time:
            pause_duration = datetime.now() - self.paused_time
            self.start_time += pause_duration
            self.paused_time = self.start_time

    def stop(self):
        if self.start_time:
            self.previous_elapsed_time = self.elapsed_time + datetime.now() - self.start_time
            self.start_time = None
            self.elapsed_time = timedelta(0)
            self.paused_time = timedelta(0)
            self.update_time_label()

    def update_time_label(self):
        if self.start_time:
            if self.paused_time != self.start_time:
                elapsed_time = datetime.now() - self.start_time - (datetime.now() - self.paused_time)
            else:
                elapsed_time = datetime.now() - self.start_time

            elapsed_str = str(elapsed_time)
            milliseconds = int(elapsed_time.microseconds / 1000)
            self.time_label.config(text=f"{elapsed_str[:-7]}.{milliseconds:03d}")

            self.root.after(50, self.update_time_label)

    def close(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()