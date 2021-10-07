import lift
import person
import building
from tkinter import Entry, Label, Button, Tk
import time
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random

with open("waittimelog.txt", "w") as file:
    pass


def show_data():

    """ retrieve and display data about the system """

    # create empty dictionary to store data
    data = {"FLOORS":[],"PEOPLE":[],"WAITTIME":[]}

    # open text file and store data in the dictionary
    with open("waittimelog.txt", "r") as file:
        file_data = file.readlines()
        for line in file_data:
            line = line.rstrip("\n").split(",")
            data['FLOORS'].append(int(line[0]))
            data['PEOPLE'].append(int(line[1]))
            data['WAITTIME'].append(float(line[2]))

    # create an empty 3D graph
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.set_xlabel("Floors")
    ax.set_ylabel("People")
    ax.set_zlabel("Average Wait Time")

    # plot the data on the graph
    ax.scatter3D(data["FLOORS"], data["PEOPLE"], data["WAITTIME"], c="red")

    # display the graph
    plt.show()


def loop(main_building):

    """ loop the lift's move function """

    # update all people's wait time
    for n in range(main_building.floors+1):
        for person in main_building.floor_queues[n]:
            person.wait_time += 1

    # if one lift is not finished, do not stop
    stop = True
    for l in main_building.lifts:
        if not l.move():
            stop = False

    return stop



def start_simulation():

    """ function called after a button press so that number of lifts can be
        specified """

    # get the number of lifts and destroy the GUI
    try:
        no_lifts = int(lifts_label.get())
        if no_lifts < 1 or no_lifts > 10:
            raise Exception("Number of lifts must be between 1 and 10")
    except (TypeError):
        error_label.config(text="Please enter an integer between 1 and 10")
        return
    except Exception as e:
        error_label.config(text="Please enter an integer between 1 and 10")
        return
    window.destroy()

    # run all of the simulations
    for n in range(10,100,10):
        for i in range(10,100):
            people = []
            start(n, i, no_lifts, people)
    show_data()


def start(no_floors, no_people, no_lifts, people):

    """ initialise all variables and instantiate all objects """

    # create the building
    main_building = building.Building(no_floors, no_people)
    for n in range(no_people):
        new_person = person.Person(main_building)
        people.append(new_person)

    # create the lifts
    for n in range(no_lifts):
        lift_ = lift.Lift(main_building)

    # run the simulation of this case
    while not loop(main_building):
        continue

    total = sum([person_.wait_time for person_ in people])
    wait_time = total/main_building.no_people
    main_building.lifts[0].write(wait_time)


# create a GUI to allow the user to enter a number of floors
window = Tk()
window.config(bg = "dark grey")

lifts_text = Label(window, text="Enter the number of lifts:",
                   font = ("Helvetica", 10)).grid(row=0, column=0,
                                                  sticky="NSEW")
lifts_label = Entry(window)
lifts_label.grid(row=1, column=0, sticky="NSEW")
lifts_submit = Button(window, text="Start Simulation", font = ("Helvetica", 10),
                      command=lambda: start_simulation())
lifts_submit.grid(row=2, column=0, sticky="NSEW")
error_label = Label(window, text="", fg="red", bg="dark grey")
error_label.grid(row=3, column=0)

window.mainloop()
