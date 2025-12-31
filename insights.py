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

    insights = {
        "Average Mood": average(moods),
        "Average Sleep (hrs)": average(sleep),
        "Average Stress": average(stress),
        "Average Screen Time (hrs)": average(screen)
    }

    warnings = []

    if insights["Average Sleep (hrs)"] < 6:
        warnings.append("Low sleep trend detected")

    if insights["Average Stress"] > 7:
        warnings.append("High stress trend detected")

    if insights["Average Screen Time (hrs)"] > 8:
        warnings.append("High screen-time trend detected")

    if sleep >= 7 and stress <= 6 and screen_time <= 6 and good_mood:
        print("\n✅ Everything looks good.")
        print("You're doing well. Nothing to worry about today 🌿")

    return insights, warnings
