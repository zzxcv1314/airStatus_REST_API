airStatus_REST_API 
===================
Account <br/>
계정
----------------
----------
<b>POST</b> /account/signup/ <br><br>
새로운 사용자를 생성한다. <br><br>
요청 : <br>
~~~
POST /account/login HTTP/1.1
Host : 
Content-Type : application/json
Accept: application/json

{
    "username": "test6",
    "email": "test6@test.com",
    "password1": "test6test6",
    "password2": "test6test6"
}
~~~
응답 : <br>
~~~
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "key": "85e148f3e9a4f2ea71228f3100007bc3ba2f23d5"
}
~~~
------
<b>POST</b> /account/login/ <br/><br>
시스템에 로그인 한다. <br/>로그인을 하게 되면 로그인 절차를 정상적으로 수행 했음을 표시하기 위해서 Session에 대한 key를 얻게 된다. <br>시스템의 대부분의 API는 사용자 데이터에 따라서 수행해야 하는 작업이기 때문에 key를 사용해야 한다. <br><br>

요청 : <br>

~~~
POST /account/login HTTP/1.1
Host : 
Content-Type : application/json
Accept: application/json

{
    "username": "test6",
    "email": "test6@test.com",
    "password": "test6test6"
}
~~~

응답 : <br>
~~~
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "key": "85e148f3e9a4f2ea71228f3100007bc3ba2f23d5"
}

~~~

-------
<b>POST</b> /account/logout <br><br>

로그인 되어있는 계정을 로그아웃한다. <br><br>
요청 : <br>
~~~
POST /account/logout HTTP/1.1
HOST :
Content-Type : application/json
Accept: application/json 

{

}
~~~
응답 : <br>
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "Successfully logged out."
}
~~~

------
<b>POST</b> /account/password/change <br><br>
사용자의 암호를 변경한다. <br><br>
요청 : <br>
~~~
POST /account/logout HTTP/1.1
HOST :
Content-Type : application/json
Accept: application/json 

{
    "new_password1": "test7test7",
    "new_password2": "test7test7"
}
~~~
응답 : <br>
~~~
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "New password has been saved."
}
~~~

-----
<b>GET </b> /account/user/ <br><br>
자신의 계정 정보를 조회할 수 있다. 
응답 : 
~~~
HTTP 200 OK
Allow: GET, PUT, PATCH, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 1,
    "username": "test1",
    "email": "test1@test.com",
    "first_name": "",
    "last_name": ""
}
~~~

<b>PUT </b> /account/user/<br><br>
자신의 계정 정보를 수정할 수 있다. <br>
요청 : <br>
~~~
POST /account/logout HTTP/1.1
HOST :
Content-Type : application/json
Accept: application/json 

{
    "pk": 1,
    "username": "test2",
    "email": "test1@test.com",
    "first_name": "testfirst",
    "last_name": "testlast"
}
~~~
응답 : 
~~~
HTTP 200 OK
Allow: GET, PUT, PATCH, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 1,
    "username": "test2",
    "email": "test1@test.com",
    "first_name": "",
    "last_name": ""
}
~~~

Device <br/>
기기 
----------------
------
<b>POST</b> /devices/ <br><br>
기기를 등록한다. 기기의 이름과 장소를 설정할 수 있다.<br>
기기별 키가 생성이 되며 이 키를 이용하여 각 기기별 공기정보를 저장할 수 있다.  <br><br>
요청 : <br>
~~~
POST /account/logout HTTP/1.1
HOST :
Content-Type : application/json
Accept: application/json 

{
    "dname": "testdev1",
    "dlocation": "hwayangdong"
}
~~~
응답 : <br>
~~~
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "dname": "testdev1",
    "dlocation": "hwayangdong",
    "dkey": "712a5b92-1604-11e8-803d-9c42967a3cc3",
    "downer": "test6"
}
~~~

-------
<b> GET </b> /devices/ <br><br>

모든 기기를 조회해 볼 수있다. 

응답 : 
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "dname": "testdev1",
        "dlocation": "hwayangdong",
        "dkey": "712a5b92-1604-11e8-803d-9c42967a3cc3",
        "downer": "AnonymousUser"
    },
    {
        "dname": "testdev2",
        "dlocation": "hwayang",
        "dkey": "057a42e4-1606-11e8-8e56-9c42967a3cc3",
        "downer": "test6"
    }
]
~~~
<b>URI filtering을 이용하여 원하는 정보만 가져올 수 있다. </b> 
1. 특정 사용자가 소유한 기기 검색 <br/>
<b>GET</b> /devices/?downer={userid} <br><br>
응답 :
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "dname": "testdev2",
        "dlocation": "hwayang",
        "dkey": "057a42e4-1606-11e8-8e56-9c42967a3cc3",
        "downer": "test6"
    }
]
~~~

2. 특정 위치의 기기만 조회해 볼 수 있다. <br/>
<b>GET</b> /devices/?dlocation={location} <br><br>
응답 : 
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "dname": "testdev2",
        "dlocation": "hwayang",
        "dkey": "057a42e4-1606-11e8-8e56-9c42967a3cc3",
        "downer": "test6"
    }
]
~~~

3. 기기 이름을 검색하여 정보를 가져온다. <br/>
<b> GET</b> /devices/?dname={devname} <br><br>
응답 : 
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "dname": "testdev1",
        "dlocation": "hwayangdong",
        "dkey": "712a5b92-1604-11e8-803d-9c42967a3cc3",
        "downer": "AnonymousUser"
    }
]
~~~



Airstatus <br/>
공기 상태 
----------------
----
<b>POST </b> /airstatus/ <br><br>

디바이스에서 공기 정보를 업로드 한다. 


요청 : 
~~~
POST /account/login HTTP/1.1
Host : 
Content-Type : application/json
Accept: application/json

{
    "pm25": "5",
    "pm10": "5",
    "temperature": "5",
    "devicekey": "a83c92fa-1546-11e8-86cb-9c42967a3cc3"
}
~~~

응답 : 
~~~
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pm25": "5",
    "pm10": "5",
    "temperature": "5",
    "devicekey": "a83c92fa-1546-11e8-86cb-9c42967a3cc3"
}

~~~
----
<b>GET </b> /airstatus/ <br><br>

업로드 되어있는 공기정보를 모두 보여준다. 

응답 : 
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pm25": "aa",
        "pm10": "aa",
        "temperature": "aa",
        "devicekey": null
    },
    {
        "pm25": "aa",
        "pm10": "aa",
        "temperature": "aa",
        "devicekey": null
    },
    {
        "pm25": "9",
        "pm10": "10",
        "temperature": "33",
        "devicekey": null
    },
    {
        "pm25": "10",
        "pm10": "11",
        "temperature": "33",
        "devicekey": null
    }
]
~~~

URI filtering을 이용하여 원하는 정보만 가져올 수 있다. 
1. 해당 device에서 업로드 한 공기 정보 조회하기 
<b> GET </b> /airstatus/?devicekey={devicekey} 
응답 : 
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pm25": "10",
        "pm10": "11",
        "temperature": "33",
        "devicekey": "a83c92fa-1546-11e8-86cb-9c42967a3cc3"
    },
    {
        "pm25": "7",
        "pm10": "7",
        "temperature": "33",
        "devicekey": "a83c92fa-1546-11e8-86cb-9c42967a3cc3"
    },
    {
        "pm25": "10",
        "pm10": "11",
        "temperature": "33",
        "devicekey": "a83c92fa-1546-11e8-86cb-9c42967a3cc3"
    },
    {
        "pm25": "10",
        "pm10": "11",
        "temperature": "33",
        "devicekey": "a83c92fa-1546-11e8-86cb-9c42967a3cc3"
    }
]
~~~
2. 해당 공기 정보에 해당하는 결과만 보기 <br>

<b> GET </b> /airstatus/?pm25={10} <br>
응답 : 
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pm25": "10",
        "pm10": "11",
        "temperature": "33",
        "devicekey": null
    }
]
~~~

<b> GET </b> /airstatus/?pm10={10} <br>
응답 :
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pm25": "9",
        "pm10": "10",
        "temperature": "33",
        "devicekey": null
    }
]
~~~
<b> GET </b> /airstatus/?temperature={33} <br>
응답 : 
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pm25": "9",
        "pm10": "10",
        "temperature": "33",
        "devicekey": null
    }
]
~~~


------
<b>DELETE</b> /airstatus/{id} <br><br>

등록된 공기정보를 삭제한다.<br>
해당 정보의 id field를 이용하여 등록된 공기정보를 삭제할 수 있다. <br>
요청 : 
~~~

~~~


4

    
    

