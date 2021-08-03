import time
from abc import abstractmethod


class WaterHeater:
    """
    熱水器，冬天的英雄
    """

    def __init__(self):
        self._observer = []
        self.temperature: int = 25

    def set_temperature(self, temperature: int):
        self.temperature = temperature
        self.notifies()

    def get_temperature(self):
        return self.temperature

    def add_observer(self, mode):
        self._observer.append(mode)

    def notifies(self):
        for observer in self._observer:
            observer.notify(self)

    def auto_heater(self):
        current_temperature = self.get_temperature()
        while True:
            if current_temperature <= 45:
                print(f'Current Temperature is {current_temperature}')
                current_temperature += 1
                self.set_temperature(current_temperature)
                time.sleep(0.5)
            else:
                break


class Observer:
    @abstractmethod
    def notify(self, heater: WaterHeater):
        pass


class ShowerMode(Observer):

    def notify(self, heater: WaterHeater):
        current_temperature = heater.get_temperature()
        if 35 <= current_temperature <= 45:
            print(f'可以洗澡囉！！！！')


if __name__ == '__main__':
    water_heater = WaterHeater()
    shower_mode = ShowerMode()
    water_heater.add_observer(shower_mode)
    water_heater.auto_heater()
