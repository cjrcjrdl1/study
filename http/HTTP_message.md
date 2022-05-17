# HTTP 메시지 시작 라인
+ start-line=request-line / status-line
+ request-line = method SP(공백) request-target SP HTTP-version CRLF(빈 줄)
+ HTTP method (GET: 조회, POST: 요청 내역 처리)
+ 요청 대상 (/corse?data=abc)
+ HTTP Version
+ absolute-path[?query] (절대경로[?쿼리]) 이 때, 절대경로란 / 로 시작하는 경로를 의미

# 응답 메시지
+ start-line = request-line / status-line
+ status-line = HTTP-version SP status-code SP reason-phrase CRLF

# HTTP 헤더
+ header-field = field-name":" OWS field-value OWS (OWS: 띄어쓰기 허용)
+ HTTP 전송에 필요한 모든 부가정보
+ 표준 헤더가 많고 필요시 임의의 헤더 추가 가능

# HTTP 메시지 바디
+ 실제 전송할 데이터
+ HTML, 이미지, 영상, Json 등 byte로 표현할 수 있는 모든 데이터 전송 가능