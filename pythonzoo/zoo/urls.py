from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.zooDetailView.as_view(), name='zooDetail'),
    path('exhibit/<int:pk>', views.exhibitDetailView.as_view(), name='exhibitDetail')
]
