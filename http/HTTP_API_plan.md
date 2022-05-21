# HTTP API 설계 예시
+ HTTP API - 컬렉션
+ POST 기반 등록 ex) 회원 관리 API 제공

+ HTTP API - 스토어
+ PUT 기반 등록 ex) 정적 컨텐츠 관리, 원격 파일 관리

+ HTML FORM 사용
+ 웹 페이지 회원 관리
+ GET, POST만 지원

# 회원 관리 시스템
+ 회원 목록 /members -> GET
+ 회원 등록 /members -> POST
+ 회원 조회 /members/{id} -> GET
+ 회원 수정 /members/{id} -> PATCH, PUT, POST
+ 회원 삭제 /members/{id} -> DELETE

+ 클라이언트는 등록될 리소스의 URI를 모름
+ 서버가 새로 등록된 리소스 URI를 생성해줌
+ 컬렉션(Collection)
+ 서버가 관리하는 리소스 디렉토리
+ 서버가 리소스의 URI를 생성하고 관리
+ 여기서 컬렉션은 /members

# 파일 관리 시스템
+ 파일 목록 /files -> GET
+ 파일 조회 /files/{filename} -> GET
+ 파일 등록 /files/{filename} -> PUT
+ 파일 삭제 /files/{filename} -> DELETE
+ 파일 대량 등록 /files -> POST

+ 클라이언트가 리소스 URI를 알고 있어야 함
+ 클라이언트가 직접 리소스의 URI를 지정
+ 스토어(Store)
+ 클라이언트가 관리하는 리소스 저장소
+ 클라이언트가 리소스의 URI를 알고 관리
+ 여기서 스토어는 /files

# HTML FORM 사용
+ HTML FORM은 GET, POST만 지원
+ Ajax 같은 기술을 사용해서 해결 가능
+ 여기서는 순수 HTML, HTML FORM 얘기
+ GET, POST만 지원하므로 제약이 있음

+ 회원 목록 /members -> GET
+ 회원 등록 폼 /members/new -> GET
+ 회원 등록 /members/new, /members -> POST
+ 회원 조회 /members/{id} -> GET
+ 회원 수정 폼 /members/{id}/edit -> GET
+ 회원 수정 /members/{id}/edit, /members/{id} -> POST
+ 회원 삭제 /members/{id}/delete -> POST