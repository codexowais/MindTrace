import csv

DATA_FILE = "data.csv"


def load_data():
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def average(values):
    return round(sum(values) / len(values), 2) if values else 0


def generate_insights():
    data = load_data()

    moods = [int(row["mood"]) for row in data]
    sleep = [float(row["sleep_hours"]) for row in data]
    stress = [int(row["stress_level"]) for row in data]
    screen = [float(row["screen_time"]) for row in data]

    avg_mood = average(moods)
    avg_sleep = average(sleep)
    avg_stress = average(stress)
    avg_screen = average(screen)

    insights = {
        "Average Mood": avg_mood,
        "Average Sleep (hrs)": avg_sleep,
        "Average Stress": avg_stress,
        "Average Screen Time (hrs)": avg_screen
    }

    warnings = []

    # Existing warnings
    if avg_sleep < 6:
        warnings.append("Low sleep trend detected")

    if avg_stress > 7:
        warnings.append("High stress trend detected")

    if avg_screen > 8:
        warnings.append("High screen-time trend detected")

    if avg_mood < 6:
        warnings.append("Low mood trend detected")

    # ✅ Positive reassurance condition
    if avg_mood >= 7 and avg_sleep >= 7 and avg_stress <= 6 and avg_screen <= 6:
        print("\n✅ Everything looks good.")
        print("You're doing well. Nothing to worry about today 🌿")

    return insights, warnings
