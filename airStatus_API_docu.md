airStatus_REST_API 
===================
Account <br/>
계정
----------------
----------
<b>POST</b> /account/signup/ <br>
새로운 사용자를 생성한다. <br>
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
<b>POST</b> /account/login/ <br/>
    시스템에 로그인 한다. <br/>로그인을 하게 되면 로그인 절차를 정상적으로 수행 했음을 표시하기 위해서 Session에 대한 token을 얻게 된다. <br>시스템의 대부분의 API는 사용자 데이터에 따라서 수행해야 하는 작업이기 때문에 token을 사용해야 한다. 
    <br><br>
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
POST /account/logout <br>
로그인 되어있는 계정을 로그아웃한다. 
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


Device <br/>
기기 
----------------

Airstatus <br/>
공기 상태 
----------------



    
    

