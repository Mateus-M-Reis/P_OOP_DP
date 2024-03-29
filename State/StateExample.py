from abc import abstractmethod, ABCMeta

class InternalState(metaclass = ABCMeta):
    @abstractmethod
    def changeState(self):
        pass

class TurnedOn(InternalState):
    def changeState(self):
        print("Turning  ON the device!!!")
        return "ON"

class TurnedOff(InternalState):
    def changeState(self):
        print("Turning  OFF the device!!!")
        return "OFF"

class IncreaseVolume(InternalState):
    def changeState(self):
        print("Increasing volume by 10 !!!")
        return "+10"

class DecreaseVolme(InternalState):
    def changeState(self):
        print("Decreasing volume by 10 !!!")
        return "-10"

class RadioStation(InternalState):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, status):
        self.state = status

    def changeState(self):
        self.state = self.state.changeState()

Radio = RadioStation()
print('The radios internal state is currently: {}'.format(Radio.getState()))

ON = TurnedOn()
OFF = TurnedOff()

Louder = IncreaseVolume()
Lower = DecreaseVolme()

print("\nTurning on the radio!")
Radio.setState(ON)
Radio.changeState()
print('The radios internal state is currently: {}'.format(Radio.getState()))

print("\nTurning off the radio!")
Radio.setState(OFF)
Radio.changeState()
print('The radios internal state is currently: {}'.format(Radio.getState()))

print("\nIncreasing the volume")
Radio.setState(Louder)
Radio.changeState()
print('The radios internal state is currently: {}'.format(Radio.getState()))

print("\nDecreasing the volume")
Radio.setState(Lower)
Radio.changeState()
print('The radios internal state is currently: {}'.format(Radio.getState()))
