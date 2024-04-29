Usage
=====

.. _registration:

사용자 등록
------------

**서비스 계정 등록 절차**

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

**추가 정보**

- 계정 등록 및 관리와 관련된 자세한 정보는 당사 웹사이트의 FAQ 또는 사용자 가이드 섹션에서 확인할 수 있습니다.
- 웹사이트 링크: [회사 웹사이트 링크]


그 다음 컨텐츠
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

