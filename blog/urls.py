from django.conf.urls import url
from . import views

# ^은 "시작"을 뜻합니다.
# 첫 부분 다음부터 나오는 post/는 URL이 post 를 포함해야한다는 것을 뜻합니다. 아직까지 할 만 하죠?
# (?P<pk>[0-9]+) - 이 부분은 좀 까다롭습니다. 이 정규 표현식의 의미는 장고가 여러분이 여기에 넣은 모든 것을 pk변수에 넣어 뷰로 전송하겠다는 뜻입니다. [0-9]은 문자를 제외하고, 숫자 0부터 9까지 하나의 숫자만 있다는 뜻입니다. +는 하나 또는 그 이상의 숫자가 와야한다는 것을 의미합니다. 따라서 http://127.0.0.1:8000/post//라고 하면 post/ 다음에 숫자가 없기 때문에 해당이 안되지만, http://127.0.0.1:8000/post/1234567890/는 완벽하게 매칭됩니다.
# / - 다음에 / 가 한번 더 와야 한다는 의미입니다.
# $ - "마지막"! 입니다. 그 뒤로 더이상 문자가 오면 안됩니다.#

urlpatterns= [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
	url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
]