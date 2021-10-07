import lift
import person
import building
from tkinter import*
import time
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random

# clear the people array and the text file
people = []
file = open("waittimelog.txt", "w")
file.close()

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

    # call the move function on all the lifts
    stop = True
    for l in main_building.lifts:
        # if a lift is not finished, do not stop
        if not l.move():
            stop = False

    return stop


def find_max(n, no_lifts, no_floors):

    """ Return the initial maximum floor for a given lift, number of floors and
        number of lifts """

    increment = no_floors/no_lifts
    return int(n*increment)


def start_simulation():

    """ function called after a button press so that number of lifts can be
        specified """

    # get the number of lifts and destroy the GUI
    no_lifts = int(lifts_label.get())
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
        lift_ = lift.Lift(main_building, find_max(n, no_lifts, no_floors))

    # run the simulation of this case
    while not loop(main_building):
        continue

    # calculate and write the average time to the file
    total = sum([person_.wait_time for person_ in people])
    wait_time = total/main_building.no_people
    main_building.lifts[0].write(wait_time)

# create a GUI to allow the user to enter a number of lifts
window = Tk()

lifts_text = Label(window, text="Enter the number of lifts:").grid(row=0, column=0)
lifts_label = Entry(window)
lifts_label.grid(row=1, column=0)
lifts_submit = Button(window, text="Start Simulation", command=lambda: start_simulation())
lifts_submit.grid(row=2, column=0)

window.mainloop()
