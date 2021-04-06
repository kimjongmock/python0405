#다중 상속

class Tiger:                          
    def jump(self):
        print("호랑이 점프")

    def cry(self):
        print("호랑이 어흥~~")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self):
        print("사자 으릉으릉~~")

class Liger(Lion, Tiger):      #Lion Tiger 중 앞에 있는것을 부름 ex-> (Tiger,Lion) 순서면 Tiger 출력됨
    def play(self):
        print("라이거와 놀기")


l = Liger()
l.cry()
print("Liger MOR:", Liger.__mro__)
        
