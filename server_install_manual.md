airStatus_REST_API 
===================
SERVER INSTALLATION MANUAL
----------------
----------
<b> Installing Raspnerry PI OS </b>
1. 라즈베리 파이 OS 설치하기 
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

2. 가상환경 만들기 
위의 과정을 잘 따라 했다면 virtualenvwrapper.sh 내에 있는 함수인 mkvirtualenv함수를 사용할 수 있다. 
~~~
mkvirtualenv {{가상환경 이름}}
~~~
myvenv 라는 이름의 가상환경이 설치되고 그 가상환경을 사용할 수 있게(workon)된다. 
~~~
mkvirtualenv myvenv
which python 
~~~
명령어를 실행했을 때 아래와 같은 경로로 나오면 제대로 잘 된 것이다. 
~~~
/home/user_name/.virtualenvs/py2/bin/python
~~~
가상환경에서 나가려면
~~~
$ deactivate
~~~
다시 들어가려면
~~~
$ workon py2
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





