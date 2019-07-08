from django.urls import path
from ticket_notify_app import views

app_name = 'ticket_notify_app'
urlpatterns = [
    # 書籍
    path('concert/', views.concert_list, name='concert_list'),   # 一覧
    path('concert/add/', views.concert_edit, name='concert_add'),  # 登録
    path('concert/edit/<int:concert_id>/', views.concert_edit, name='concert_edit'),  # 修正
    path('concert/delete/<int:concert_id>/', views.concert_delete, name='concert_delete'),   # 削除
]