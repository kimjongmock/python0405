# -*- 생성자와 소멸자 -*-

import sys
class MyClass:
    #생성자 필수
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
        #소멸자는 크케 중요하지 않음
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(5)
# d_copy = d
print("참조 횟수:{0}".format(sys.getrefcount(d)))
# del d_copy 
# del d

print("전체코드 실행 종료")



