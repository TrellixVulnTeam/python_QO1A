class Audio:
    """
    power, volume 을 가진 클래스
    power => True, False
    volume => 정수

    switch() => power 값을 변경
    tune() => power 켜있으면 음악 재생되고,
               power 꺼진 상태면 power를 켜라는 메세지 출력
    volume() => volume 값을 변경
    """
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

    def switch(self, on_off):
        self.power = on_off
            
    def set_volume(self, vol):
        self.volume = vol

    def tune(self):
        str = "♪~♬~~♩~" if self.power else "turn it on"   # 삼항연산자
        print(str)

# 삼항연산자
# (Java)  조건 ? 참 : 거짓(자바)
# (Python)  [참일 때 실행될 구문] if [조건] else [거짓일 때 실행될 구문]

mp3 = Audio(False, 9)
mp3.set_volume(12)
mp3.tune()
mp3.switch(True)
mp3.tune()
