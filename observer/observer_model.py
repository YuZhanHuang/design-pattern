from abc import ABCMeta, abstractmethod


class Observable:
    """
    被觀察的對象，可以想成是發消息的人
    """

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, obj=0):
        for observer in self._observers:
            observer.update(self, obj)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable, obj):
        pass
