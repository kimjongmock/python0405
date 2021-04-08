#0406테스트

#1
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance += amount
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id,self.__name,self.__balance)

account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

#2
class Developer:
    def __init__(self,name):
        self.name = name 
    def getSalary(self,day):
        result = day * 100000
        print("개발자 월급:", result)
#3
class WebDeveloper(Developer):
    def __init__(self,name,skill):
        Developer.__init__(self,name)
        self.skill = skill
    def getSalary(self,day):
        result = day * 200000
        print("웹 개발자 월급:", result)

dev = Developer("전우치")
webDev = WebDeveloper("이순신", "ASP.NET")
dev.getSalary(1); webDev.getSalary(1);


    

# 4.파이썬에서 함수, 클래스, 모듈, 패키지에 대한 개념과 차이점을 
# 정리해서 제출하세요. 

# 함수의 정의 : def로 선언하고 (:)으로 끝낸다. 함수의 시작과 끝은 코드 들여쓰기로 구분하며
#                  함수의 시작과 끝을 명시하지 않는다. 헤더 파일에 함수를 미리 선언할 수 있다.

# 클래스 정의 : 파이썬에 내장되어 있는 클래스들도 있으며 이외에 사용자가 자주 사용하거나 또는
#                  필요에 의해 사용자만의 형식을 정의하여 사용할 수 있다. 이를 커스텀 클래스라고 한다.

# 모듈 : 여러 코드들을 묶어 다른곳에서 재사용할 수 있는 코드들의 모음을 뜻한다.
#          String, data, time 등과 같이 파이썬이 기본적으로 제공하는 모듈들도 있지만
#          사용자가 필요하다면 모듈을 직접 작성하고 이를 제공할 수도 있다.

# 패키지 : 쉽게 모듈을 모아놓은 모듈 모음집이라고 생각하면 된다.

#5. 파이썬의 정규표현식을 사용해서 어떤 문자열에 우편번호가 포함되어 
# 있다면 re모듈의 어떤 함수를 사용해서 손쉽게 검색(가져올 수 있는)하는 
# 코드를 작성하세요. 

# s = "ABCDEFG123456GDGDGD"
# c = re.compile("123456")
# print = (c)
