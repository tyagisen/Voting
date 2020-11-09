from django.urls import path
from . import views
from .views import QuestionListView, QuestionDetailView

urlpatterns = [
    path('', QuestionListView.as_view(), name='home'),
    path('detail/<int:pk>/', QuestionDetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('lte/', views.lte, name = 'lte')
]
