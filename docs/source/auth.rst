인증 및 토큰 관리
=====

.. _login:

로그인 및 인증토큰 발급
------------

**1. 로그인**

.. http:post:: /api/v1/auth/login
   :noindex:
	
	아이디 패스워드 기반 로그인을 통한 인증 토큰 (JWT) 발급
	 
   :form string: email (*required*) -- 사용자 email address (id)
   :form string: password (*required*) -- 사용자 패스워드
   
   :requestheader Authorization: `token`
   
.. important::
   중요사항 추가.

**Example Request**

.. sourcecode:: bash
  
   curl -s -H "Authorization: {Bearer}" curl -X POST https://skt.fame.com/api/v1/auth/login -d '{"email": "user@example.com", "password": "your_password"}' 

**Example Response** JWT가 포함된 응답을 받습니다.

.. sourcecode:: json

   {
      "token": "eyJhbGciOiJIUzI1NiIsInR...",
      "refreshToken": "eyDhbHciOiJIUzI1AiIsInW..."
   }

**2. JWT 발급**

- 로그인 성공 시, 서버에서 사용자의 인증 정보를 기반으로 JWT를 자동 발급합니다.
    - ⚠️ JWT claims 에 대한 권한은 사용자 등록시 수동으로 관리 (SMS, FAME (기능 카테고리에 따라 추가 적용)
- 이 토큰은 사용자의 권한 및 세션 정보를 포함하며, API 요청 시 **`Authorization`** 헤더에 포함해 사용합니다.

토큰 관리
------------

**1. 토큰 유효성 체크**

- JWT는 설정된 만료 시간 후에 유효성을 잃습니다. 서버는 만료 시간을 체크하여, 만료된 토큰에 대해서는 **`401 Unauthorized`** 응답을 반환합니다. 아래 API 를 통해 토큰의 유효기간을 확인하여 필요시 토큰을 재발급할 수 있습니다.

.. http:post:: /api/v1/auth/checkTokenValidity
   :noindex:
	
	아이디 패스워드 기반 인증을 통한 토큰 유효기간 확인
	 
   :form string: token (*required*) -- 유효기간 확인하고자 하는 토큰
   
   :requestheader Authorization: `token`
   
.. important::
   중요사항 추가.

**Example Request**

.. sourcecode:: bash
  
   curl -s -H "Authorization: {Bearer}" curl -X POST https://skt.fame.com/api/v1/auth/checkTokenValidity -d '{"token": {token}}' 

**Example Response** JWT가 포함된 응답을 받습니다.

.. sourcecode:: json

   {
      "token": "eyJhbGciOiJIUzI1NiIsInR...",
      "valid-until": "2024-04-01 24:00:00"
   }


**2. 토큰 갱신**

- 토큰 발급 시 같이 지급된 갱신 토큰을 활용하여 토큰 유효기간을 갱신합니다.

.. http:post:: /api/v1/auth/tokenRefresh
   :noindex:
	
	아이디 패스워드 기반 로그인을 통한 인증 토큰 (JWT) 발급
	 
   :form string: refresh token (*required*) -- 갱신토큰
   
   :requestheader Authorization: `token`
   
.. important::
   중요사항 추가.

**Example Request**

.. sourcecode:: bash
  
   curl -s -H "Authorization: {Bearer}" curl -X POST https://skt.fame.com/api/v1/auth/tokenRefresh -d '{"refreshToken": {token}}' 

**Example Response** JWT가 포함된 응답을 받습니다.

.. sourcecode:: json

   {
      "token": "eyJhbGciOiJIUzI1NiIsInR...",
      "refreshToken": "eyDhbHciOiJIUzI1AiIsInW..."
   }


**3. 주의사항 및 기타**

- 모든 인증 관련 통신은 HTTPS를 통해 암호화되어야 합니다.
- 사용자는 토큰을 안전하게 보관하고, 노출되지 않도록 주의해야 합니다.
- 로그인이나 토큰 발급 및 갱신 과정에서 문제가 발생하거나 추가 지원이 필요한 경우, 지원 팀에 문의하십시오.
