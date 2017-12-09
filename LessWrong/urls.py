from django.conf.urls import url, include

from game import views

urlpatterns = [
    url(r'^', include('game.urls', namespace='game')),
]
