#from 패키지명 improt 모듈명
from bs4 import BeautifulSoup

#페이지를 로딩(html문서를 읽어와라 -> 유니코드)
page = open("c:\\work2\\test01.html", "rt", encoding="utf-8").read() # read() -> 한줄로 읽어와라

#검색에 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )

#<p>태그를 모두 검색해라
#print( soup.find_all("p") )

#첫번째 <p>를 검색
#print( soup.find("p") )

#<p class="outer-text"> 된 경우 (약간의 필터링)
#print( soup.find_all("p", class_="outer-text") )

#특정 id속성을 검색
#print( soup.find(id="first") )

#<a>태그를 가져와라
#print( soup.find_all("a") )
#print( soup.find_all("b") )

#태그를 제거하고 내부 문자열을 가져와라
for tag in soup.find_all("p"):
    print( tag.text )
