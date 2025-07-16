from django.urls import path
from . views import *


urlpatterns = [
    path("",chat_view,name="home"),
    path('chat/new-groupchat', create_groupchat, name = "new-groupchat"),
    path('chat/<username>', get_or_create_chatroom, name="start-chat"),
    path('chat/room/<chatroom_name>', chat_view, name="chatroom"),
    path("chat/edit/<str:chatroom_name>",chatroom_edit_view, name="edit-chatroom"),
    path("chat/delete/<str:chatroom_name>",delete_chatroom_view, name="chatroom-delete"),
    path("chat/leave/<str:chatroom_name>",leave_chatroom_view, name="chatroom-leave")
]