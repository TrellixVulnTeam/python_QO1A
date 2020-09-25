class AudioVisual:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume
    
    def switch(self, on_off):
        self.power = on_off

    def set_volume(self, vol):
        self.volume = vol

class Audio(AudioVisual):    
    def __init__(self, power, volume):
        super().__init__(power, volume)     # 부모생성자 호출방법2. super().[]
    
    def tune(self):
        str = "♪~♬~~♩~" if self.power else "turn it on"   # 삼항연산자
        print(str)

class TV(AudioVisual):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size

    def watch(self):
        str = "TV 보는 중" if self.power else "TV를 켜주세요"
        print(str)


tv = TV(False, 12, 48)
tv.switch(True)
tv.watch()

audio = Audio(True, 15)
audio.set_volume(20)
audio.tune()
