Retrieve Book Titles by Author
------------------------------

.. http:get:: /libapi/author/(author_name)
   :noindex:
   
     Retrieves a list of books written by a specified author.
	 
   :query string:  author_name (*required*) -- The name the of the particular author
   
   :requestheader Authorization: `token`
   
.. important::
   The author name must be in URL encoded format.

**Example Request**

.. sourcecode:: bash
  
   curl -s -H "Authorization: e52858e3-529a-40da-99d2-3bffd80a7a9b" curl -X GET https://fictionallibrary.com/libapi/author/Crichton%20Michael 

**Example Response**

.. sourcecode:: json

   {
      "count": 17,
      "results": [
         {
             "author": "Crichton, Michael",
             "title": "The Andromeda Strain",
             "publisher": "Vintage", 
             "latest_publication_date": "January 24, 2017",
             "language": "en",
             "isbn10": "1101974494",
             "isbn13": "9781101974490"
         },
         {
             "author": "Crichton, Michael",
             "title": "Jurassic Park",
             "publisher": "Vintage", 
             "latest_publication_date": "May 14, 2012",
             "language": "en",
             "isbn10": "1501216902",
             "isbn13": "9781501216909"
         },
         {
             "author": "..."
         },
      ]
   }


API 사용 방법
API 엔드포인트 개요
API 호출 예시
요청 및 응답 형식
주요 API 기능 설명

API 호출 제한 및 관리
API 호출 제한 정책
호출 제한 초과 처리
호출량 추적 및 모니터링
관리자 설정 및 사용자 제한 조정

오류 코드 및 문제 해결
일반적인 오류 코드 목록
오류 대응 가이드
문제 해결 단계

보안 및 권한 관리
사용자 권한 및 역할 관리
보안 모범 사례
데이터 보호 및 개인정보 처리

고급 주제 및 추가 리소스
고급 구성 옵션
외부 통합 및 확장 기능
참고 문헌 및 추가 도구

부록
API 참조 문서
용어 정리
변경 로그 및 업데이트 이력

고객 지원
지원 연락처 정보
FAQ
커뮤니티 및 포럼
