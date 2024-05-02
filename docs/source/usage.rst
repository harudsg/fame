기본활용
=====

.. _registration:

사용자 등록
------------

**1. 계정 등록 페이지 접속**

- 우리 서비스의 계정 등록 페이지에 접속합니다.
- 페이지 URL: [계정 등록 페이지 링크]

**2. 회사 정보 입력**

- 등록 폼에 다음 회사 정보를 입력합니다:
    - **회사명**: 귀하의 회사명을 정확하게 입력해주세요.
    - **담당자명**: 계정 관리를 담당할 담당자의 전체 이름을 입력해주세요.
    - **담당자 이메일 주소**: 담당자의 이메일 주소를 입력해주세요. 모든 중요한 소통은 이 이메일을 통해 이루어집니다.
    - **담당자 연락처**: 담당자의 연락 가능한 전화번호를 입력해주세요.

**3. 정보 확인 및 제출**

- 입력한 정보를 다시 한 번 확인합니다.
- 모든 정보가 정확하면, ‘등록’ 버튼을 클릭하여 계정 등록 요청을 제출합니다.

**4. 계정 활성화**

- 등록 요청 후, 당사의 관리 팀이 제출된 정보를 검토합니다.
- 정보가 확인되면, 담당자 이메일로 계정 활성화 링크가 포함된 이메일이 발송됩니다.
- 이메일에 포함된 링크를 클릭하여 계정을 활성화합니다.

**5. JWT 발급**

- 계정 활성화가 완료되면, 로그인하여 대시보드에서 인증 토큰(JWT)을 생성할 수 있습니다.
- 이 JWT를 사용하여 서비스 API에 안전하게 접근하고 필요한 데이터를 요청할 수 있습니다. 토큰은 헤더에 **`Authorization: Bearer <token>`** 형식으로 포함하여 API 요청을 합니다.

**6. 지원 및 문의**

- 등록 과정에서 문제가 발생하거나 추가적인 지원이 필요한 경우, 다음 연락처로 문의해 주시기 바랍니다:
    - **기술 지원 이메일**: [지원 이메일 주소]
    - **기술 지원 전화번호**: [지원 전화번호]


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
