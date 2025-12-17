import tkinter as tk
from tkinter import messagebox

from tracker import log_entry
from insights import generate_insights


def save_entry():
    try:
        mood = int(mood_entry.get())
        sleep = float(sleep_entry.get())
        stress = int(stress_entry.get())
        screen = float(screen_entry.get())
        note = note_entry.get()

        log_entry(mood, sleep, stress, screen, note)
        messagebox.showinfo("Success", "Entry saved successfully")

        clear_fields()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_insights():
    try:
        insights, warnings = generate_insights()

        result = ""
        for key, value in insights.items():
            result += f"{key}: {value}\n"

        if warnings:
            result += "\nObservations:\n"
            for w in warnings:
                result += f"- {w}\n"

        messagebox.showinfo("Insights", result)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_fields():
    mood_entry.delete(0, tk.END)
    sleep_entry.delete(0, tk.END)
    stress_entry.delete(0, tk.END)
    screen_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)


# ---------------- GUI SETUP ----------------

root = tk.Tk()
root.title("MindTrace")
root.geometry("350x420")
root.resizable(False, False)

tk.Label(root, text="MindTrace", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Mood (1–10)").pack()
mood_entry = tk.Entry(root)
mood_entry.pack()

tk.Label(root, text="Sleep Hours").pack()
sleep_entry = tk.Entry(root)
sleep_entry.pack()

tk.Label(root, text="Stress (1–10)").pack()
stress_entry = tk.Entry(root)
stress_entry.pack()

tk.Label(root, text="Screen Time (hours)").pack()
screen_entry = tk.Entry(root)
screen_entry.pack()

tk.Label(root, text="Note (optional)").pack()
note_entry = tk.Entry(root, width=40)
note_entry.pack(pady=5)

tk.Button(root, text="Save Entry", command=save_entry, width=20).pack(pady=10)
tk.Button(root, text="View Insights", command=show_insights, width=20).pack()

root.mainloop()
