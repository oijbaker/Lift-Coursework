import random

class Person:

    """ Person class stores information about people in the building """

    def __init__(self, building):

        """ constructor initialises:
            - building: the building they are in
            - start: the person's start floor
            - destination: the destination floor
            - wait_time: counter to track the wait time
        """

        self.building = building
        self.start = random.randint(0, self.building.floors)
        self.destination = random.randint(0, self.building.floors)
        # make sure start floor isn't the same as destination
        while self.destination == self.start:
            self.destination = random.randint(0, self.building.floors)
        self.wait_time = 0
        self.load_to_floor()


    def load_to_floor(self):

        """ put the person on a floor """

        self.building.floor_queues[self.start].append(self)


    def update_wait(self):

        """ update the building's maximum wait time if the person's wait time
            is greater than it """
            
        if self.wait_time > self.building.max_wait_time:
            self.building.max_wait_time = self.wait_time
