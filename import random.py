import random


class Environment:

    def __init__(self):
        # 0 = clean, 1 = light dirt, 2 = heavy dirt
        self.locationCondition = {
            'A': random.randint(0, 2),
            'B': random.randint(0, 2),
            'C': random.randint(0, 2)
        }


class VacuumCleaner:

    def __init__(self, Environment):

        self.environment = Environment
        self.location = random.choice(['A', 'B', 'C'])

        self.battery = 100
        self.dustbin = 0
        self.score = 0
        self.cleanCount = 0
        self.moveCount = 0
        self.totalTime = 0

        print("Initial condition:", self.environment.locationCondition)
        print("Vacuum starts at:", self.location)
        print("Battery:", self.battery, "%")
        print("Dustbin:", self.dustbin, "%")

        self.clean()

    def dirtType(self, value):

        if value == 0:
            return "Clean"

        elif value == 1:
            return "Light Dirt"

        else:
            return "Heavy Dirt"

    def cleanRoom(self, room):

        dirt = self.environment.locationCondition[room]

        if dirt == 0:
            print(room, "is already clean")
            return

        # Select mode according to dirt and battery
        if dirt == 1:

            mode = "Eco"
            batteryUsed = 5
            dust = 10
            points = 5
            cleaningTime = 2

        else:

            # Save battery when battery is getting low
            if self.battery <= 50:

                mode = "Eco"
                batteryUsed = 5
                dust = 15
                points = 7
                cleaningTime = 4

            else:

                mode = "Turbo"
                batteryUsed = 10
                dust = 20
                points = 10
                cleaningTime = 5

        print("\n", room, "has", self.dirtType(dirt))
        print("Mode:", mode)
        print("Cleaning time:", cleaningTime, "minutes")

        if self.battery < batteryUsed:
            print("Not enough battery")
            return

        if self.dustbin + dust > 100:

            print("Dustbin is full")
            self.emptyDustbin()

        print("Cleaning", room, "...")

        self.environment.locationCondition[room] = 0

        self.battery = self.battery - batteryUsed
        self.dustbin = self.dustbin + dust
        self.score = self.score + points

        self.cleanCount = self.cleanCount + 1
        self.totalTime = self.totalTime + cleaningTime

        print(room, "cleaned")
        print("Battery:", self.battery, "%")
        print("Dustbin:", self.dustbin, "%")

    def move(self, room):

        if self.location == room:
            return

        if self.battery < 5:

            print("Battery is low, cannot move")
            return

        print("\nMoving from", self.location, "to", room)

        self.location = room
        self.battery = self.battery - 5
        self.score = self.score - 1
        self.moveCount = self.moveCount + 1

        print("Now at", self.location)
        print("Battery:", self.battery, "%")

    def findDirtyRoom(self):

        # Heavy dirt is given first priority
        for room in self.environment.locationCondition:

            if self.environment.locationCondition[room] == 2:
                return room

        # Then light dirt
        for room in self.environment.locationCondition:

            if self.environment.locationCondition[room] == 1:
                return room

        return None

    def charge(self):

        print("\nBattery is low")
        print("Returning for charging...")

        self.battery = 100

        print("Battery is now 100%")

    def emptyDustbin(self):

        print("Emptying dustbin...")

        self.dustbin = 0

        print("Dustbin is empty")

    def clean(self):

        for i in range(6):

            currentDirt = self.environment.locationCondition[self.location]

            if currentDirt != 0:

                self.cleanRoom(self.location)

            else:

                print("\n", self.location, "is clean")

                nextRoom = self.findDirtyRoom()

                if nextRoom is None:

                    print("All rooms are clean")
                    break

                self.move(nextRoom)

            # Save battery by charging when it becomes low
            if self.battery <= 15:

                self.charge()

            # Empty dustbin when it is almost full
            if self.dustbin >= 80:

                self.emptyDustbin()

        self.result()

    def result(self):

        print("\n-------------------------")
        print("Final Result")
        print("-------------------------")

        print("Environment:",
              self.environment.locationCondition)

        print("Vacuum Location:", self.location)
        print("Battery:", self.battery, "%")
        print("Dustbin:", self.dustbin, "%")
        print("Rooms cleaned:", self.cleanCount)
        print("Number of moves:", self.moveCount)
        print("Total cleaning time:", self.totalTime, "minutes")
        print("Final score:", self.score)


environment = Environment()

vacuum = VacuumCleaner(environment)