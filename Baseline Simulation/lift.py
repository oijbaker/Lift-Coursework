class Lift:

    """ Implements the main algorithm determining how the lift moves """

    def __init__(self, building):

        """ Initialises attributes of the lift """

        self.building = building
        self.floor = 0
        self.capacity = 8
        self.contents = []
        self.number = 0
        self.max = self.building.floors
        self.min = 0
        self.direction = "up"
        self.move_count = 0
        self.building.lifts.append(self)


    def move(self):

        """ check whether the algorithm is finished, move the lift up or down
            whilst ensuring it stays within the boundaries """

        self.move_count += 1

        for person in self.contents:
            person.wait_time += 1

        # update boundaries
        self.max = self.find_max()
        self.min = self.find_min()

        # move the lift and check if they cross the boundaries
        if self.direction == "up":
            if self.floor+1 <= self.building.floors:
                self.floor += 1
            else:
                self.change_direction()
        else:
            if self.floor-1 >= 0:
                self.floor -= 1
            else:
                self.change_direction()

        self.get_people()
        self.drop_off()

        # check if the algorithm is finished
        finished = True
        if self.contents != []:
            finished = False
        for n in range(self.building.floors+1):
            if self.building.floor_queues[n] != []:
                finished = False
        return finished




    def find_max(self):

        """ find the maximum floor the lift needs to travel to """
        max = 0

        # check lift contents
        for person in self.contents:
            if person.destination > max:
                max = person.destination

        # check building contents
        for n in range(self.building.floors):
            for person in self.building.floor_queues[n]:
                if person.start > max:
                    max = person.start
                elif person.destination > max:
                    max = person.destination

        return max


    def find_min(self):

        """ find the minimum floor the lift needs to travel to """
        min = 0

        # check lift contents
        for person in self.contents:
            if person.destination < min:
                min = person.destination

        # check building contents
        for n in range(self.building.floors):
            for person in self.building.floor_queues[n]:
                if person.start < min:
                    min = person.start
                elif person.destination < min:
                    min = person.destination

        return min


    def change_direction(self):

        """ change the direction of the lift """

        if self.direction == "up":
            self.direction = "down"
        else:
            self.direction = "up"


    def get_people(self):

         """ pick up people on the floor """

         for person in self.building.floor_queues[self.floor]:
            if self.direction == "up":
                if person.destination > self.floor:
                    if self.number+1 <= self.capacity:
                        self.load(person)
            else:
                if person.destination < self.floor:
                    if self.number+1 <= self.capacity:
                        self.load(person)
            #if self.number+1<=self.capacity:
            #    self.load(person)


    def load(self, person):

        """ pick up an individual from the floor """

        self.contents.append(person)
        self.number += 1
        self.building.floor_queues[self.floor].remove(person)


    def drop_off(self):

        """ drop off all relevant people """

        to_drop = [person for person in self.contents
                   if person.destination == self.floor]
        for person in to_drop:
            self.contents.remove(person)
            self.number -= 1
            person.update_wait()


    def write(self, wait_time):

        """ write the system information to a file """

        with open("waittimelog.txt", "a") as file:
            file.write(str(self.building.floors)+","+
                       str(self.building.no_people)+","+
                       str(wait_time)+","+
                       str(len(self.building.lifts))+"\n")
