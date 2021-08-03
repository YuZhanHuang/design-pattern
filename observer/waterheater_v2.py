from abc import ABCMeta, abstractmethod
from observer_model import Observer, Observable


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self._temperature = 25

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature
        print(f'Current Temperature is {self._temperature} degree.')
        self.notify_observers()


class WashingMode(Observer):

    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) and observable.get_temperature() <= 45:
            print('可以洗澡啦')


if __name__ == '__main__':
    heater = WaterHeater()
    wash_mode = WashingMode()
    heater.add_observer(wash_mode)
    heater.set_temperature(40)
    heater.set_temperature(50)
