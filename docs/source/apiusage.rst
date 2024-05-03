서비스 활용 예시
=====

.. _example:

.. image:: ../img/fame_svc_scen.png

FAME 서비스는 위와 같은 다양한 시나리오에서 안전한 금융 거래를 위한 특별한 보조 안전망을 제공하고 있습니다. 
각각의 서비스 시나리오에 따라 FAME 의 어떤 기능을 어떻게 활용할 수 있는지 몇 가지 예시를 통해 보여드리도록 하겠습니다. 

보이스 피싱 및 사칭 감지
------------

.. image:: ../img/fame_call.png

FAME 은 대상 고객의 최근 통화 및 메시징 이력을 AI 기술로 분석 합니다. SKT 빅데이터와 AI 분석 모델을 통해 보이스피싱, 스미싱, 사칭 등 범죄에 연관된 SKT 고객을 구분하고 해당 고객과의 통화 및 메시징 이력 여부를 제공합니다. 
금융 서비스 기관은 고객이 금융 서비스를 이용하는 과정에서 FAME 의 해당 기능을 활용하여 부가적인 보안 절차를 도입할지 여부를 결정할 수 있게 됩니다. 

.. http:post:: /api/v1/fame/checkNumbers

    대상 고객의 금융 범죄 연관 대상자와의 통화 및 메시징 기록 여부 제공. 기본 최근 24시간이며 날짜를 지정하여 조회할 수 있습니다. (최근 30일 제한)

    **Example request**:

    .. tabs::

        .. code-tab:: bash

            $ curl \
              -X POST \
              -H "Authorization: Token <token>" https://skt.fame.com/api/v1/fame/checkNumbers \
              -H "Content-Type: application/json" \
              -d @body.json

        .. code-tab:: python

            import requests
            import json
            URL = 'https://skt.fame.com/api/v1/fame/checkNumbers'
            TOKEN = '<token>'
            HEADERS = {'Authorization': f'token {TOKEN}'}
            data = json.load(open('body.json', 'rb'))
            response = requests.post(
                URL,
                json=data,
                headers=HEADERS,
            )
            print(response.json())

    ``body.json`` 의 내용은 아래와 같습니다. 

    .. sourcecode:: json

        {
            "target_user_id": "string",
	    "start_date": "2024-05-03",
            "end_date": "2024-05-03"
        }
     
	.. important::
	   중요사항 추가.
	
	**Example Response** 최근 24 시간, 금융 범죄 연관 대상자와의 통화 및 메시징 횟수 제공
	
	.. sourcecode:: json
	
	   {
	      "user id": "id",
	      "abnormal_call_count": 5
	   }

기기 및 개인정보 탈취 시도 방지
------------

작업 중

.. image:: ../img/fame_private.png


FAME 은 고객이 실제 이동한 궤적을 SKT 의 고도화된 AI 위치 추정 기술을 바탕으로 재구성할 수 있습니다. 만약 불상자가 실제 명의자의 휴대폰 USIM 을 복제하여 기기 변경 후 실제 명의자를 사칭하여 모바일 기반 금융 거래를 시도할 경우 기존의 인증 체계만으로는 이 불법 행위를 검출해내기가 어렵습니다. 이 경우 FAME 서비스를 활용하여 실제 명의자의 이동 기록과 불상자가 임의로 개통한 기기의 이동 기록을 비교하는 방식으로 위치 기반 2차 인증 작업을 진행할 수 있습니다.

이는 불상자가 실제 명의자의 위치 이동 궤적을 유지하지 않는 한, 불상자의 위치는 실제 명의자의 예상 위치에서 벗어나게 됩니다.

.. http:post:: /api/v1/fame/getLocationHistory

    대상 고객의 최근 1시간 동안 위치 이력 정보 제공 (10분 단위, 요구 사항에 따라 조회 기간 확대 협의)

    **Example request**:

    .. tabs::

        .. code-tab:: bash

            $ curl \
              -X POST \
              -H "Authorization: Token <token>" https://skt.fame.com/api/v1/fame/getLocationHistory \
              -H "Content-Type: application/json" \
              -d @body.json

        .. code-tab:: python

            import requests
            import json
            URL = 'https://skt.fame.com/api/v1/fame/getLocationHistory'
            TOKEN = '<token>'
            HEADERS = {'Authorization': f'token {TOKEN}'}
            data = json.load(open('body.json', 'rb'))
            response = requests.post(
                URL,
                json=data,
                headers=HEADERS,
            )
            print(response.json())

    ``body.json`` 의 내용은 아래와 같습니다. 

    .. sourcecode:: json

        {
            "target_user_id": "string"
        }
     
	.. important::
	   중요사항 추가.
	
	**Example Response** 최근 1시간 동안의 위치 이력 정보 제공
	
	.. sourcecode:: json
	
	   {
	      "user id": "id",
	      "location history":[
	      	"d-10": "경기도 용인시 수지구 풍덕천1동",
		"d-20": "부산시 해운대구 해운대동",
		"d-30": "부산시 해운대구 해운대동",	
		"d-40": "부산시 해운대구 해운대동",	
		"d-50": "부산시 해운대구 해운대동",	
		"d-60": "부산시 해운대구 해운대동"	
	      ]
	   }
