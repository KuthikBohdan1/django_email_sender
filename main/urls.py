from django.urls import path
from main import views

urlpatterns = [
    # Визнач тут свої URL-шляхи
    path('', views.ActionTemplateView.as_view(), name="a"),
    path('api-progres/<str:taskid>/', views.ajaxProgres, name="progres"),
]

app_name = "main"