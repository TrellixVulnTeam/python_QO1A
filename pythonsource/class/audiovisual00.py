class AudioVisual:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

    def swith(self, on_off):
        self.power = on_off

    def set_volume(self, vol):
        self.volume = vol


class Audio(AudioVisual):
    def __init__(self, power, volume):
        super().__init__(power, volume)

    def tune(self):
        str = "La La La......" if self.power else "turn it on"
        print(str)


class TV(AudioVisual):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size

    def watch(self):
        str = "Tv 보는 중 " if self.power else "Tv 켜세요"
        print(str)


tv = TV(False, 12, 48)
tv.swith(True)
tv.watch()

audio = Audio(True, 15)
audio.set_volume(20)
audio.tune()
