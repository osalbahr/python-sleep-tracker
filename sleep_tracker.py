from tkinter import *
from sys import *


def main():
    if len(argv) != 2:
        print("Usage: sleep-tracker.py <filename>")
        exit(1)

    filename = argv[1]

    total = 0
    count = 0

    print(filename)
    try:
        with open(filename) as file:
            for line in file:
                total += get_hours_delta(*line.split(","))
                count += 1
    except FileNotFoundError:
        print(f"File {filename} does not exist")
        exit(2)

    create_gui(total / count)


# Example: 2:00 am, 10:00 am -> 8.0
def get_hours_delta(start, end):
    delta = get_hour(end) - get_hour(start)
    if delta <= 0:
        delta += 24

    return delta


def get_hour(s):
    time, ampm = s.split()
    hour, minute = [int(x) for x in time.split(":")]
    hours = time_to_int(hour, ampm)

    return hours + minute / 60


def time_to_int(hour, ampm):
    hours = hour

    if ampm == "pm" and hours != 12:
        hours += 12

    if ampm == "am" and hours == 12:
        hours -= 12

    return hours


def create_gui(h):
    verdict = ":) Good job!" if h >= 8 else ":( Not enough"
    root = Tk()
    a = Label(root, text=f"Average sleep: {h} hours\n{verdict}")
    a.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
