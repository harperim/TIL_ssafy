### Django 진행 순서 
1. 가상환경 만들기
```bash
$ python -m venv venv
```


2. 장고 설치
```bash
$ pip install django
$ pip instlal -r requirements.txt
```

3. 가상환경 활성화
```bash
$ source venv/Scripts/activate
```

4. 프로젝트 만들기
```bash
$ django-admin startproject <project-name> .
```

5. 앱 만들기
```bash
$ python manage.py startapp <app-name>
```

6. 앱 등록하기
- `settings.py`에 가서 앱 등록하기

7. django server 실행
```bash
$ python manage.py runserver
```

8. 각 앱 별로 URL 분리
- `app_name = '앱 이름'`
- name 속성 사용
- `url` 태그 사용 

9. 최상위 템플릿 폴더 추가
- `settings.py` 에 추가
  - `DIR : [BASE_DIR/templates]`

10. 모든 템플릿은 base.html을 상속 받아야 한다.
- `extends`를 사용해 상속 받는다.


```
[진행 순서]
1. URL
2. views
3. templates
- app 이름 폴더 만들어서 그 아래에 html 파일 만들기
```

### 참고
- 프로젝트 이름 변경하고 싶을 때
  - 변경하지 말고 아예 삭제 후, 새로 만드는게 빠르고 깔끔함
