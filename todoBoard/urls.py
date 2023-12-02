from django.urls import path
from .views import IndexView, boards_list, board_detail, task_create, board_create

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('boards/', boards_list, name='boards_list'),
    path('addBoard/', board_create, name='board_create'),
    path('boards/<int:board_id>', board_detail, name='board_detail'),
    path('boards/<int:board_id>/backlog/', board_detail, {'template_name': 'board_backlog.html'}, name='board_backlog'),
    path('boards/<int:board_id>/addTask/', task_create, name='task_create'),
]
