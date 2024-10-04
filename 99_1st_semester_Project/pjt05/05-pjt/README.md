# 05-pjt

## 구현 과정 중 학습한 내용
- User 객체를 가져와 사용하는 Form을 직접 구현해봄으로써 각 상황에 맞는 form에는 어떤 것들이 있는지 학습할 수 있었습니다.
- 로그인 사용자와 로그인하지 않은 사용자의 접근 가능한 기능을 다르게 함으로써 `is_authenticated`와 `@login_required`의 사용법을 익힐 수 있었습니다. 


## 어려웠던 부분
- `from .forms import CustomUserCreationForm, CustomUserChangeForm` 
- `from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm`
- `from django.contrib.auth import login as auth_login, logout as auth_logout`
- `from django.contrib.auth import get_user_model`
- 위와 같이 import 문을 활용하여 특정 모듈이나 클래스, 함수 등을 불러오는 부분이 잘 생각나지 않아 기존에 작성했던 코드를 참조하며 작성하였고, 이는 아직 손에 익지 않았기 때문이라고 생각되어 보다 많은 학습을 해야겠다고 생각했습니다. 


## 새로 배운 것들 및 느낀 점
- 수업 시간에 배운 내용들을 잘 이해하고 있다고 생각했었는데, 처음부터 끝까지 직접 구현하려고 하다보니 이해가 잘 되지 않는 부분이 생각보다 많았습니다. 원리를 이해하며 사용하는 것이 중요하다고 생각되어 더 구체적으로 공부해야겠다는 생각을 하게 되었습니다. 