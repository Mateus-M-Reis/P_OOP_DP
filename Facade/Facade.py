class Travelrganizer(object):
    def __init__(self):
        print('Travelrganizer: Let me arrange the travel for you!\n')

    def arrangeTravel(self, destination, typeoftravel):
        print('The destination is {}\n'.format(destination))

        self.meansoftransport = Transporter(destination = destination, typeoftravel = typeoftravel)
        self.meansoftransport.bookTravel()

        self.meansofsleeping = Hotelier()
        self.meansofsleeping.bookRoom()
        self.meansofsleeping.arrangeFood()

class Transporter(object):
    def __init__(self, destination, typeoftravel):
        print('Arranging transport to destination: {} be means: {}\n'.format(destination, typeoftravel))
        self.destination = destination
        self.typeoftravel = typeoftravel

    def bookTravel(self):
        if self.typeoftravel == 'owncar':
            print('Nothing to book, the customer user his/her own car!\n')
        elif self.typeoftravel == 'plane':
            print('Booking seats for travelling to: {} by PLANE!\n'.format(self.destination))
        elif self.typeoftravel == 'bus':
            print('Booking seats for travelling to: {} by BUS!\n'.format(self.destination))

class Hotelier(object):
    def __init__(self):
        print('Arranging room for customers. ---\n')

    def roomFree(self):
        print('Checking if there are any rooms left free?\n')
        return True

    def bookRoom(self):
        if self.roomFree():
            print('Booking room for customer\n')

    def arrangeFood(self):
        print('Arranging room for the customers\n')

class roadTripping(object):
    def __init__(self):
        print('Arranging some sightseeing for the customers. ---\n')

    def arrangTour(self):
        print('Arranging some fancy places to visit!\n')


class You(object):
    def __init__(self, name):
        print('\nMe:: Whohooooooo we are traveling: {}\n'.format(name))

    def talkToAgent(self):
        print('Me:: Asking agent to arrange this weekend!\n')
        manager = Travelrganizer()
        manager.arrangeTravel(destination='Greece', typeoftravel='plane')

    def __del__(self):
        print('Me:: Thankyou mister for arranging us this beaulful weekend!\n')

Me = You('Daniel')
Me.talkToAgent()




