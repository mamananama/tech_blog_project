# Django blog project
Python Django를 사용하여 모놀리식 블로그를 만드는 프로젝트 입니다.
<br>
<br>
<br>
## 프로젝트 개요
### 프로젝트 기간
> 2023.10.26 ~ 2023.11.07
<br>
<br>

### 프로젝트 설명
> 특정 주제에 관하여 사용자들이 모여 의견과 정보를 나누는 커뮤니티를 생각하며 제작했습니다.
> 
> 특정 주제에 글이 쌓여가는 모습이 마치, 선로 위를 달리는 기차와 비슷한 모습이라 생각해, "TRAIN"이라는 이름을 붙였습니다.
> 
> 이 커뮤니티 블로그에서, 특정한 카테고리 또는 주제는 기차의 노선인 "ROUTE"로 표현되며, 각 ROUTE에서 자유롭게 주제에 맞는 글을 작성할 수 있습니다.
> 
> 또한 "운행 상태"를 표시하여 해당 주제가 진행중인 주제인지, 진행이 종료된 주제인지 표시할 수 있게 했고,  
> 이는 프로젝트와 같은 진행단계의 표시가 필요한 주제,
> 시작과 종료가 있는 주제에 대해 이야기할 수 있도록 도움을 줄 것입니다.
>
> 각 ROUTE에 글을 작성한 User를 표시하는 기능으로 특정 주제로 진행되는 커뮤니티의 인원을 서로 파악할 수 있게 했습니다.
> 
> 누구든 자유롭게 ROUTE를 만들고, 그 ROUTE속에서 함께하는 많은 사람들과 의견을 나누세요! 🚂
<br>
<br>

### 요구사항 분석
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/1fbae51c-e28c-4757-83d2-01b45aa58a5f)
<br>
<br>

## 프로젝트 목표와 기능
### 목표
* Django의 Class Base View를 사용하여 모놀리식으로 블로그 개발
* "ROUTE"로 표현되는 카테고리 기반의 커뮤니티 블로그
* 회원가입, CURD 구현

### 기능
* 로그인 한 유저는 자유롭게 ROUTE 생성할 수 있습니다.
* 최초로 ROUTE를 생성한 유저는 ROUTE의 "운행 상태"를 수정할 수 있는 권한을 가집니다.
* 메인 페이지에서 ROUTE, 조회수, 최근 작성 기준으로 글을 확인할 수 있습니다.
* 게시글에 사진과 파일을 업로드 할 수 있으며, 파일을 다운 받을 수 있습니다.
* 각 ROUTE에 한번이라도 글을 쓴 사람을 ROUTE 정보에서 확인할 수 있으며,  
다른 유저의 프로필을 확인하여 그 유저가 활동한 ROUTE, 최근 작성 글 목록, 최근 작성 댓글을 확인할 수 있습니다.
<br>
<br>

### WBS
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/f6c9361e-eeda-4ed1-ab18-5b6bb058a2be)
<br>
<br>

## 프로젝트 설계
### 개발환경 및 사용한 기술
* Enviroment<br>
  ![Static Badge](https://img.shields.io/badge/visualstudiocode-%23007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
  ![Static Badge](https://img.shields.io/badge/github-%23181717?style=flat-square&logo=github&logoColor=white)

* Stack<br>
  ![Static Badge](https://img.shields.io/badge/python-%233776AB?style=flat-square&logo=python&logoColor=white)
  ![Static Badge](https://img.shields.io/badge/django-%23092E20?style=flat-square&logo=django&logoColor=white)
  ![Static Badge](https://img.shields.io/badge/html5-%23E34F26?style=flat-square&logo=html5&logoColor=white)
  ![Static Badge](https://img.shields.io/badge/css3-%231572B6?style=flat-square&logo=css3&logoColor=white)

* DB<br>
  ![Static Badge](https://img.shields.io/badge/sqlite-%23003B57?style=flat&logo=sqlite&logoColor=white)

<br>
<br>

### URL 설계
- `/` 메인 페이지
- `/admin/` 관리자 페이지
- `/account/`
    - `/account/welcome/` 회원 가입 완료 웰컴 페이지
    - `/account/signup/` 회원 가입
    - `/account/login/` 로그인
    - `/account/logout/` 로그아웃
    - `/account/profile/<str:user_name>/` `user_name`의 프로필
- `/station/` 태그별로 정리 된 글 목록
    - `/station/create/` 새 route 생성
- `/station/route/<str:tag_name>/` `tag_name`으로 등록된 글 목록
    - `/station/route/<str:tag_name>/route_edit/` `tag_name` 의 상태 수정
    - `/station/route/<str:tag_name>/create/` 해당 `tag_name`으로 설정된 새 글 생성
    - `/station/route/<str:tag_name>/<int:post_pk>/` `tag_name`으로 등록된 `pk` 번의 글
        - `/station/route/<str:tag_name>/<int:post_pk>/post_delete/` `tag_name`으로 등록된 `post_pk` 번의 글 삭제
        - `/station/route/<str:tag_name>/<int:post_pk>/post_edit/` `tag_name`으로 등록된 `post_pk` 번의 글 수정
        - `/station/route/<str:tag_name>/<int:post_pk>/comment/` `tag_name`으로 등록된 `post_pk` 번의 글에 댓글 생성
        - `/station/route/<str:tag_name>/<int:post_pk>/comment_delete/<int:comment_pk>` `tag_name`으로 등록된 `post_pk` 번의 글의 `comment_pk`  댓글 삭제
<br>
<br>

### ERD 설계
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/6bc562d5-90bf-49f9-b0f0-3cee265a42fb)
> * 모델의 연결
>   * User-Post : 일대다 연결
>   * User-Route : 일대다 연결
>   * User-Comment : 일대다 연결
>   * Post-Comment : 일대다 연결
>   * Route-Post : 일대다 연결
  
<br>
<br>

### 페이지 설계
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/261ed80d-bb40-40fb-a64d-fd355da0f378)
https://www.figma.com/file/iftq8MW7Rn4L9PdRcfnDd4/tech_blog?type=design&node-id=1%3A6&mode=design&t=qBbcosNpXNXZiuVG-1
<br>
<br>

### Project Tree
```
📦tech_blog
 ┣ 📂account
 ┃ ┣ 📂migrations
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂main
 ┃ ┣ 📂migrations
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂templatetags
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜template_filters.cpython-312.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-312.pyc
 ┃ ┃ ┣ 📜template_filters.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
 ┃ ┗ 📂station
 ┃ ┃ ┣ 📂files
 ┃ ┃ ┗ 📂images
 ┣ 📂route
 ┃ ┣ 📂migrations
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜validators.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜index.css
 ┃ ┣ 📂icon
 ┃ ┃ ┣ 📜favicon-16x16.png
 ┃ ┃ ┣ 📜favicon-32x32.png
 ┃ ┃ ┗ 📜favicon.ico
 ┣ 📂station
 ┃ ┣ 📂migrations
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂templatetags
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜template_filters.cpython-312.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-312.pyc
 ┃ ┃ ┣ 📜template_filters.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂templates
 ┃ ┣ 📂account
 ┃ ┃ ┣ 📜login.html
 ┃ ┃ ┣ 📜profile.html
 ┃ ┃ ┣ 📜signup.html
 ┃ ┃ ┗ 📜welcome.html
 ┃ ┣ 📂error
 ┃ ┃ ┣ 📜error404.html
 ┃ ┃ ┗ 📜error500.html
 ┃ ┣ 📂main
 ┃ ┃ ┗ 📜index.html
 ┃ ┣ 📂route
 ┃ ┃ ┣ 📜post.html
 ┃ ┃ ┣ 📜postdelete.html
 ┃ ┃ ┣ 📜route.html
 ┃ ┃ ┗ 📜route_base.html
 ┃ ┣ 📂station
 ┃ ┃ ┣ 📜create.html
 ┃ ┃ ┗ 📜station.html
 ┃ ┗ 📜base.html
 ┣ 📂train
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```
<br>
<br>

## 프로젝트 페이지 설명
### '/'
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/8bf22b66-5feb-4aab-9a6f-17d6651bd533)
메인페이지 입니다.<br>
* Route 탭: 현재 생성된 Route의 목록을 확인할 수 있습니다. Route의 상태와 개척자, 작성된 게시물의 수를 확인할 수 있습니다.
* 많이 본 글 탭: Post model에 속한 글 중(전체 게시물 중) 조회수가 가장 높은 상위 10개 게시물을 확인 할 수 있습니다.
* 최근 작성 글 탭: Post model에 속한 글 중(전체 게시물 중) created_at(생성 시간)이 가장 최근인 상위 10개 게시물을 확인 할 수 있습니다.
<br>

### '/staion/'
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/714cfa75-24e5-49d4-ae8e-5b49b5c43b7e)
station 페이지 입니다.<br>
* 생성된 Route의 목록을 확인할 수 있습니다.
* 제목, 생성시간, 상태, 작성된 포스트 수의 간단한 Route의 정보를 확인할 수 있습니다.
* 로그인 한 유저는 'Route 생성' 버튼을 통해 Route를 생성 할 수 있습니다.
<br>

### '/station/create/'
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/5a50901a-0790-4365-a729-6d2e16edb7ec)
route 생성 페이지 입니다.<br>
* 생성할 Route의 제목과 상태를 입력할 수 있습니다.
* 작성된 제목과 상태는 Route 모델에 저장됩니다.
<br>

### '/station/<str:tag_name>
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/4767e861-652f-475d-8867-bd21266ba2d5)
'tag_name'으로 등록된 Route의 게시글 목록을 확인할 수 있는 페이지 입니다.  
'tag_name'은 'Route'모델의 primary key 입니다.

* Route 정보에서 Route의 개설일, 개척자, 작성된 글의 수, 상태를 확인할 수 있습니다.

  > ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/5d0d0c41-6c32-42aa-91d1-ae9a2d666b08)
* 참여자 탭에서 해당 Route에 글을 작성한 User의 아이디를 확인 할 수 있습니다.

  > ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/9cb84053-ee80-4c34-b6b0-ce48ce0e78a8)
* 글 목록이 노선도처러 보여지도록 디자인을 꾸몄습니다.

  > ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/64c0759e-0686-46df-b4af-25ac146daa52)
* 사진을 포함한 게시물인 경우, 글 목록에서 작은 썸네일로 미리 볼 수 있도록 했습니다.

  > ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/a0497c0f-92fd-44a8-84b7-e3a9069682e1)
* 검색 기능을 통해 게시물을 검색하여 찾을 수 있습니다.

  > ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/83254862-4711-4943-a4c3-ca4863ad5dbe)
<br>

### '/station/<str:tag_name>/<int:post_pk>/'
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/591f7728-f1de-4d0f-9c86-eff707212baa)
'tag_name'으로 등록된 Route의 게시물 중 'post_pk'번의 게시물의 디테일 페이지 입니다.  
'post_pk'는 'Post' 모델의 primary key 입니다.

* Route 페이지로 돌아가는 기능과, 현재 로그인한 계정이 작성자 본인과 일치하면 해당 게시물을 수정, 삭제할 수 있는 메뉴를 조작하는 부분입니다.

  > ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/0961f94f-e37e-4445-ba50-cbb48c63c3bc)
* post의 제목과 작성자, 조회수, 작성일을 확인할 수 있는 부분입니다.

  > ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/e97492f3-ebfd-4fb1-91e0-0f10f383bb3b)
  > * 수정되어 게시물 내용이 변경되면 수정일이 추가로 표시됩니다.
  >   ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/fb934351-9ef9-4fe4-a5e8-3b637bbe1b5e)
* 댓글을 작성할 수 있습니다.

  > ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/c5912ba5-665f-4dc6-9ab8-ac14c8ed5761)
  > * 댓글 현재 로그인한 계정이 댓글 작성자 본인과 일치하면 해당 댓글을 삭제할 수 있는 아이콘이 나타납니다.
  >  ![image](https://github.com/mamananama/tech_blog_project/assets/114140050/9d498a8d-2774-4b57-8132-f5d4819844d0)








## 프로젝트 기능 시연
### 회원가입 및 로그인 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/c76b53dd-09c8-4cd0-9324-865536b9e39b

### "ROUTE" 생성 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/1e79eba0-5be8-4a08-8c9f-83b53a680032

### 글 작성 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/6ed9878e-6631-46e4-a533-29fb788bf52b

### 첨부파일 다운로드 및 이미지 확인 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/54ac3edb-a847-4249-9f16-1dff10f8277b

### 글 수정 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/65db9f8a-3f40-4442-a9c6-841466c97c57

### 로그아웃 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/dbf5a8c5-a2cc-4512-bc67-af6e9fa5c565

### 비 로그인 유저 접근 제한 기능(로그인 화면으로 redirect)
https://github.com/mamananama/tech_blog_project/assets/114140050/e5452b0f-eba8-43ee-a815-b724faca88c3

### 댓글 작성 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/6f87cd31-80a6-4950-824d-28465664ab3f

### Profile 페이지
https://github.com/mamananama/tech_blog_project/assets/114140050/aec160cc-a8ac-41ed-9317-5ba77766fe6f

### Profile 페이지 요소 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/11b623ba-96d2-4a17-89d6-0383359a2631

### 검색 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/33d40c02-7553-4e03-8784-b0e965b8dd40

### 다른 유저의 Profile 열람 기능
https://github.com/mamananama/tech_blog_project/assets/114140050/f7cd3c5b-86ee-4490-b1f3-6a0b530d7c62

### 잘못된 URL 접근을 막는 기능(404, 500 Error)
https://github.com/mamananama/tech_blog_project/assets/114140050/f68ec886-c872-4d2b-8724-326f2f80bbef

### 전체 기능 둘러보기
https://github.com/mamananama/tech_blog_project/assets/114140050/2a254ebc-7389-439a-b990-c42fb79dd653
<br>
<br>
---
## 트러블슈팅
### 하나의 View에서 복수의 모델 쿼리 또는 한 모델에서 복수의 쿼리 셋을 전달하는 방법.
![image](https://github.com/mamananama/tech_blog_project/assets/114140050/b7bd23ff-e901-4bb7-8834-dcd8216c7e74)

위의 이미지는 "ROUTE" 탭은 Route 모델의 전체 항목을 조회하는 쿼리셋을 사용하고, 
"많이 본 글" 탭은 Post 모델의 count를 기준으로 상위 10개 글을 조회하는 쿼리셋을 사용하고,
"최근 작성 글" 탭은 Post 모델의 create_at를 기준으로 상위 10개 글을 조회하는 쿼리셋을 사용했습니다.
메인페이지에서 하나의 뷰를 통해 2개 이상의 모델의 쿼리셋과 하나의 모델에서 2개 이상의 쿼리셋을 사용하려했습니다.

최초에 `get_object` 메서드를 사용하여 쿼리셋을 전달하려고 했지만, 해당 메서드는 하나의 쿼리셋만 전달할 수 있습니다.

```python
class MainListView(ListView):
    model = Route
    template_name = "main/index.html"
    context_object_name = 'routes'
    
    def get_object(self, queryset=None):
        queryset = super().get_queryset()
        queryset = Route.objects.all()
        print(queryset)
        return queryset
```
해당 방법만으로는 원하는 기능을 얻을 수 없었고, <br> 
원하는 기능을 수행하기 위해 쿼리셋 별로 별도의 모델을 생성하고, 별도의 뷰를 사용하는 방법을 시도했습니다.

하지만 하나의 쿼리셋을 수행하는 별도의 모델을 생성하는 것과, 뷰를 생성하여 그 뷰를 다른 뷰에 HTML \<embed\> 태그를 통해 원하는 뷰를 그리는 것이 매우 비효율적이라 생각했습니다.  

여러가지 context를 전달하는 `get_context_date` 메서드를 확인하였고, 이를 통해 다수의 쿼리셋을 하나의 뷰에 전달할 수 있었습니다.
```python
class MainListView(ListView):
    model = Route
    template_name = "main/index.html"
    context_object_name = 'routes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        routes = Route.objects.all()
        hit_posts = Post.objects.order_by('-count')[:10]
        recent_posts = Post.objects.order_by('-created_at')[:10]

        post_number = {}
        route_status = {}
        for route in context['routes']:
            post_number[str(route)] = Post.objects.filter(
                route__name__exact=str(route)).distinct().count()
            route_status[str(route)] = route.status

        context['routes'] = routes
        context['hit_posts'] = hit_posts
        context['recent_posts'] = recent_posts
        context['post_number'] = post_number
        context['route_status'] = route_status
        return context
```





