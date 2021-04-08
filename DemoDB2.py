#DemoDB2.py
#SQLite를 사용하는 데모(로컬 데이터베이스)
import sqlite3

#처음에는 데이터베이스파일(또는 메모리)를 생성
con = sqlite3.connect("memory")
#SQL구문을 실행하는 것은 대부분 커서 객체
cur = con.cursor()
#저장소(테이블)를 만들기 : 테이블 스키마(뼈대)
# cur.execute("create table PhoneBook (Name text, PhoneNum text);") //
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
#입력 파라메터 처리(python format {0},{1})
#텍스트박스(GUI, web Page)에서 입력을 받아서 처리
name = "gildong"
phonenumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name , phonenumber))
#다중의 레코드(행, row)를 입력받는 경우 : 2차원 행열데이터
datalist = (("tom", "010-123"), ("dsp", "010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#커밋(작업을 정상적으로 완료. log --> db에도 기록)
#데이터를 변경(입력,수정,삭제)
# con.commit()

#백업받기(덤프)
#파일로 저장(write Text)
f = open("c:\\work2\\dump.sq1", "wt")
for item in con.iterdump():
    print(item)
    f.write(item + "\n")

f.close()

#복구하기(with 블럭안에서 파일을 닫고 빠져나온다.)
with open("C:\\work2\\dump.sq1") as f:
    SQLScript = f.read()
#구문을 실행하기 위해
con = SQLScript.connect("c://work2//Demo.db")
cur = con.sursor()
#다중 라인으로 된 SQL 배치파일
cur.executescript(SQLScript)
con.close()
