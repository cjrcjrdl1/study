# URI(Uniform Resource Identifier)
+ URI(URL(Resource Locator), URN(Resource Name))
+ Uniform : 리소스 식별하는 통일된 방식
+ Resource : 자원, URI로 식별할 수 있는 모든 것(제한X)
+ Identifier : 다른 항목과 구분하는데 필요한 정보
+ URL - 리소스가 있는 위치를 지정
+ URN - 리소스에 이름을 부여
+ 위치는 변할 수 있으나 이름은 변하지 않음
+ URI나 URL이나 같은 의미(URN은 잘 사용하지 않음)

# URL 문법
+ scheme://[userinfo@]host[:port][/path][?query][#fragment]
+ https://www.naver.com:80/search?q=hello&hl=ko
+ 프로토콜(https)
+ 호스트명(www.naver.com)
+ 포트번호(80) //생략 가능
+ 패스(/search)
+ 쿼리 파라미터(q=hello&hl=ko)
+ 쿼리는 key=value 형태이고 ?로 시작하여 &로 추가가 가능. 이는 쿼리 파라미터, 쿼리 스트링으로 불린다
+ fragment는 html 내부 북마크 등에 사용하고 서버에 전송하는 정보가 아님