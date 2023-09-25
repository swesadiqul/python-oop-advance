from abc import ABC, abstractmethod

class RemoteControl(ABC):
    def __init__(self, device_name):
        self.device_name = device_name

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

class TV(RemoteControl):
    def power_on(self):
        return f"Turning on the {self.device_name} TV."

    def power_off(self):
        return f"Turning off the {self.device_name} TV."

    def volume_up(self):
        return f"Increasing volume on the {self.device_name} TV."

    def volume_down(self):
        return f"Decreasing volume on the {self.device_name} TV."

class DVDPlayer(RemoteControl):
    def power_on(self):
        return f"Powering on the {self.device_name} DVD player."

    def power_off(self):
        return f"Powering off the {self.device_name} DVD player."

    def volume_up(self):
        return f"Increasing volume on the {self.device_name} DVD player."

    def volume_down(self):
        return f"Decreasing volume on the {self.device_name} DVD player."


tv = TV("Samsung")
dvd_player = DVDPlayer("Sony")

print(tv.power_on())           # Output: Turning on the Samsung TV.
print(dvd_player.power_off())   # Output: Powering off the Sony DVD player.
print(tv.volume_up())          # Output: Increasing volume on the Samsung TV.
print(dvd_player.volume_down()) # Output: Decreasing volume on the Sony DVD player.


