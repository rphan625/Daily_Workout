# Making a Desktop App with TKinter
from tkinter import *
from datetime import date
import webbrowser


def callback(url):
    webbrowser.open_new_tab(url)


root = Tk()
root.title("Today's Workout!")
root.geometry("400x200")
root.iconbitmap(
    r"C:\Users\richa\Desktop\Personal Projects\python\Workout App\Daily_Workout\dumbbell.ico"
)

# Get today's date
today = date.today()
day = today.weekday()
print(day)

days_of_week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
links = [
    Label(
        root,
        text="https://www.hybridcalisthenics.com/pushups",
        font=("Helveticabold", 15),
        fg="blue",
        cursor="hand2",
    ),
    Label(
        root,
        text="https://www.hybridcalisthenics.com/legraises",
        font=("Helveticabold", 15),
        fg="blue",
        cursor="hand2",
    ),
    Label(
        root,
        text="https://www.hybridcalisthenics.com/pullups",
        font=("Helveticabold", 15),
        fg="blue",
        cursor="hand2",
    ),
    Label(
        root,
        text="https://www.hybridcalisthenics.com/squats",
        font=("Helveticabold", 15),
        fg="blue",
        cursor="hand2",
    ),
    Label(
        root,
        text="https://www.hybridcalisthenics.com/bridges",
        font=("Helveticabold", 15),
        fg="blue",
        cursor="hand2",
    ),
    Label(
        root,
        text="https://www.hybridcalisthenics.com/twists",
        font=("Helveticabold", 15),
        fg="blue",
        cursor="hand2",
    ),
]


def workout():
    first_workout = None
    first_link = None
    second_workout = None
    second_link = None

    if today.weekday() in {6, 3}:
        print("Its sunday or thursday")
        first_workout = Label(root, text="Push-Ups 2-3 Sets", font=("Helvetica", 20))
        first_workout.grid(row=1, column=0, sticky=W)

        first_link = links[0]
        first_link.grid(row=2, column=0)
        first_link.bind("<Button-1>", lambda e: callback(first_link["text"]))

        second_workout = Label(root, text="Leg-Raises 2-3 Sets", font=("Helvetica", 20))
        second_workout.grid(row=3, column=0, sticky=W)

        second_link = links[1]
        second_link.grid(row=4, column=0)
        second_link.bind("<Button-1>", lambda e: callback(second_link["text"]))

    elif today.weekday() in {0, 4}:
        print("Its monday or friday")
        first_workout = Label(root, text="Pull-Ups 2-3 Sets", font=("Helvetica", 20))
        first_workout.grid(row=1, column=0, sticky=W)

        first_link = links[2]
        first_link.grid(row=2, column=0)
        first_link.bind("<Button-1>", lambda e: callback(first_link["text"]))

        second_workout = Label(root, text="Squats 2-3 Sets", font=("Helvetica", 20))
        second_workout.grid(row=3, column=0, sticky=W)

        second_link = links[3]
        second_link.grid(row=4, column=0)
        second_link.bind("<Button-1>", lambda e: callback(second_link["text"]))

    elif today.weekday() in {1, 5}:
        print("Its tuesday or saturday")
        first_workout = Label(root, text="Bridges 2-3 Sets", font=("Helvetica", 20))
        first_workout.grid(row=1, column=0, sticky=W)

        first_link = links[4]
        first_link.grid(row=2, column=0)
        first_link.bind("<Button-1>", lambda e: callback(first_link["text"]))

        second_workout = Label(root, text="Twists 2-3 Sets", font=("Helvetica", 20))
        second_workout.grid(row=3, column=0, sticky=W)

        second_link = links[5]
        second_link.grid(row=4, column=0)
        second_link.bind("<Button-1>", lambda e: callback(second_link["text"]))

    else:
        print("It's Wednesday!!")
        first_workout = Label(root, text="No Workout Today!", font=("Helvetica", 20))
        first_workout.grid(row=1, column=0)


def main():
    myLabel = Label(
        root, text=f"{days_of_week[day]}'s Workout: ", font=("Helvetica", 25)
    )
    myLabel.grid(row=0, column=0)

    workout()

    root.mainloop()


main()
