from django.shortcuts import render,get_object_or_404,redirect
from . models import ChatGroup
from . forms import ChatMessageCreateForm
# Create your views here.


def chat_view(request):
    chat_group    = get_object_or_404(ChatGroup,group_name = "public_chat")
    chat_messages = chat_group.chat_messages.all().order_by('id')[:30]   
    form  = ChatMessageCreateForm()
    if request.htmx:
        data = request.POST
        form = ChatMessageCreateForm(data)
        if form.is_valid():
            message         = form.save(commit=False)
            message.author  = request.user
            message.group   = chat_group
            message.save()
            context = {
                "message" : message,
                "user"    : request.user
            }
            return render(request,"partials/chat_message_p.html",context)
       
    context = {"chat_messages" :chat_messages,"form" : form } 
    # for msg in chat_messages:
    #     print(msg.author.profile.displayname)
    return render(request,"a_rtchart/chat.html",context )