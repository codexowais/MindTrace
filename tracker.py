from datetime import date
import csv
import os

DATA_FILE = "data.csv"


def initialize_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "date",
                "mood",
                "sleep_hours",
                "stress_level",
                "screen_time",
                "note"
            ])


def log_entry(mood, sleep, stress, screen, note=""):
    if not (1 <= mood <= 10):
        raise ValueError("Mood must be between 1 and 10")

    if not (1 <= stress <= 10):
        raise ValueError("Stress must be between 1 and 10")

    if sleep < 0 or screen < 0:
        raise ValueError("Sleep and screen time cannot be negative")

    initialize_file()

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            date.today(),
            mood,
            sleep,
            stress,
            screen,
            note
        ])
