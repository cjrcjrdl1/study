# TCP, UDP
+ **TCP 특징** - 전송 제어 프로토콜(Transmission Control Protocol)
+ 연결 지향 - TCP 3 way handshake(가상 연결) -> SYN: 접속 요청 ACK: 요청 수락
+ SYN -> SYN + ACK -> ACK
+ 데이터 전달 보증
+ 순서 보장
+ 신뢰할 수 있는 프로토콜
+ 현재는 대부분 TCP 사용

+ **UDP 특징** - 사용자 데이터그램 프로토콜(User Datagram Protocol)
+ 기능이 거의 없음
+ 데이터 전달을 보증하지 않음
+ 순서 보장 X
+ 단순하며 빠름
+ IP와 유사하나 PORT, 체크섬 기능 추가
+ 애플리케이션에서 추가 작업이 필요