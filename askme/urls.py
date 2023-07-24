from django.urls import path
from askme import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_question/', views.post_question, name='post_question'),
    path('make_answer/<int:question_id>/', views.make_answer, name='make_answer'),
    path('hit_like/<int:answer_id>/', views.hit_like, name='hit_like')
]
