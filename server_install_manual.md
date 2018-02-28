airStatus_REST_API 
===================
SERVER INSTALLATION MANUAL
----------------
<b> Installing Raspnerry PI OS </b>
1. 라즈베리 파이 OS 설치하기 <br>
https://www.raspberrypi.org/documentation/installation/installing-images/README.md
--------
<b> How to setup your Raspberry Pi with Django.</b>

1. virtualenv 설치
* 파이썬 패키지를 설치할 때 관리자 권한이 아니라 유저권한으로 설치하기 위함. 
* 파이썬의 실행 환경을 리눅스의 것과 온전히 구분한다. 
* python3을 사용할 때 python 명령으로 실행
* 개발환경과 실 서버 환경을 동일하게 맞춤 
<br><br>

virtualenvwrapper 설치 
~~~
sudo pip install virtualenv
sudo pip install virtualenvwrapper
~~~
virtualenv 환경설정 <br>
디폴트 디렉토리 만들기 (.virtualenv)
~~~
mkdir ~/.virtualenvs
~~~
WORKON_HOME 환경 변수에 디폴트 디렉토리 등록 
~~~
export WORKON_HOME=~/.virtualenvs
~~~
.profile(우분투 기준 유저 로그인시 실행되는 스크립트) 에 virtualenvwrapper를 임포트 하도록 위 파일의 가장 하단에 아래 스크립트 추가 
~~~
. /usr/local/bin/virtualenvwrapper.sh
~~~
적용
~~~
source /usr/local/bin/virtualenvwrapper.sh
~~~

2. github에서 프로젝트 불러오기 
~~~
git clone https://github.com/zzxcv1314/airStatus_REST_API
~~~

3. 쟝고(Django)설치 
장고 설치 
~~~
sudo pip install django 
~~~

프로젝트 생성

~~~
python manage.py startapp {{examapp}}
~~~

테스트 
~~~
cd {{examapp}}
python manage.py migrate
python manage.py runserver
~~~

http://rpi_ip_address:8000/주소로 접속해서 확인. 




