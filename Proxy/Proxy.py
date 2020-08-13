from random import randint

class Player(object):
    def __init__(self, name):
        self.name = name
        self.price = randint(100000000, 900000000)
        self.training = False
        self.training = False

    def onTraining(self):
        self.training = True
        return self.training

    def onVacation(self):
        self.vacation = True
        return self.vacation

    def getPrice(self):
        return self.price

    def status(self):
        return (self.vacation or self.training)

class Manager(object):
    def __init__(self, playa):
        self.managed_player = playa
        print('Managing Player: {}'.format(self.managed_player.name))

    def send_player_on(self, typeee):
        if typeee in ['vacation', 'training']:
            if typeee == 'vacation':
                print('Sending  player: {} on vacation!'.format(self.managed_player.name))
                self.managed_player.onVacation()
            else:
                print('Sending  player: {} on vacation!'.format(self.managed_player.name))
                self.managed_player.onTraining()
        else:
            print('Cant send player on: {}, it\'s not a valid option!'.format(typeee) )
    
    def sell_player(self, offer):
        print('Price of player is: {}'.format(self.managed_player.getPrice()))
        if offer > self.managed_player.getPrice():
            print('Saying goodbye to: {}'.format(self.managed_player))
        else:
            print('Saying No to offer: {}, as the player is more valuable!'.format(offer))

if __name__ == '__main__':
    fballer = Player('Daniel')
    mgr = Manager(fballer)
    #mgr.send_player_on('vacation')
    #mgr.send_player_on('training')
    mgr.send_player_on('WHATEVER!')
    mgr.sell_player(10000000000000000)



