# 전역변수 (이름충돌)
str = "Not Class Member"
class GString:
    #초기화를 담당(생성자 메서드)
    def __init__(self):
        #인스턴스 멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str)   # print(self.str)을 사용하면 g.print()결과값이 "First Message"

g = GString()
g.set("First Message")
g.print()
