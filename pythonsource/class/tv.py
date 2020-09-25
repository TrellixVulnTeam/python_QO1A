class TV:
    """
    power, volume, size 프로퍼티를 가진 클래스
    생성잘르 통해 초기화
    switch() : power의 on / off 변환
    set_volume() : volume 조절
    watch() : power 여부에 따라 on 상태면 tv 보는중.. 메세지 보여주기
                               off 상태면 tv 켜세요 메세지 보여주기
    """
    def __init__(self, power, volume, size):
        self.power = power
        self.volume = volume
        self.size = size

    def switch(self, on_off) :
        self.power = on_off

    def set_volume(self, vol):
        self.volume = vol

    def watch(self):
        str = "TV 보는 중" if self.power else "TV를 켜주세요"
        print(str)

tv = TV(False, 14, 21)
tv.watch()

tv.switch(True)
tv.set_volume(9)
tv.watch()


