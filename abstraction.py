from abc import abstractmethod,ABC

class Remote(ABC):
    @abstractmethod
    def power(self):
        pass
class TV(Remote):
    def power(self):
        print("Tv is ON")

tv = TV()
tv.power()
