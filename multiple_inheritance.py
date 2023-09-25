class CommunicationDevice:
    def make_call(self):
        return "Making a call..."

class MultimediaPlayer:
    def play_music(self):
        return "Playing music..."

class Smartphone(CommunicationDevice, MultimediaPlayer):
    pass

phone = Smartphone()
print(phone.make_call())   # Output: Making a call...
print(phone.play_music())  # Output: Playing music...
