from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),  # nova rota adicionada aqui
]