from django.urls import path

from .views import IndexView, AboutView   #追加aboutページ

urlpatterns = [
    path('', IndexView .as_view()), #ホーム
    path('about/', AboutView .as_view()),  #ここで追加ページ作れる
    # path('contact/', indexview .as_view()), #追加ページ
]
