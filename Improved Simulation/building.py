class Building:

    """ Building class controls the graphics and store the people waiting
        for the lift """

    def __init__(self, floors, no_people):

        """ Constructor initialises lists and variables """

        self.floors = floors
        self.floor_queues = {}
        # create the lists of people on the floor
        for n in range(self.floors+1):
            self.floor_queues[n] = []

        self.no_people = no_people
        self.max_wait_time = 0
        self.lifts = []


    def sort_floors(self):

        """ arrange the people on each floor so that they can be picked up
            more efficiently """

        for floor in self.floor_queues:
            self.floor_queues[floor].sort(key = lambda x:-abs(self.floors/2-x.destination))
