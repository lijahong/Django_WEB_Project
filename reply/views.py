from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from reply.models import Reply
from reply.form import Replyform
from board.form import Post

@login_required(login_url = '/user/login')
def createreply(request, bid ):
    if request.method == "POST":
        replyform = Replyform(request.POST)
        if replyform.is_valid():
            reply = replyform.save(commit=False)
            reply.writer = request.user

            reply_post = Post() #reply의 post는 Post와 관계를 맺고 있어서 Post의 객체 값만 저장할 수 있기에 객체를 생성해서 저장한다
            reply_post.id = bid
            reply.post = reply_post #post에 객체를 저장하는 것, bid를 저장하는 것이 아니다

            reply.save()
        return redirect('/board/readdata/' + str(bid))

def readreplylist(request):
    replys = Reply.objects.all().order_by('id')
    return render(request,'reply/readreplylist.html',{ 'replylist':replys})

def readreply(request, bid):
    reply = Reply.objects.filter(Q(id=bid))
    return render(request,'reply/readreply.html',{ 'reply':reply})

@login_required(login_url = '/user/login')
def deletereply(request, bid):
    reply = Reply.objects.get(id=bid)
    if reply.writer == request.user:
        reply.delete()
        return redirect('/reply/readreplylist')
    else:
        return redirect('/reply/readreplylist')

@login_required(login_url = '/user/login')
def updatereply(request, bid):
    reply = Reply.objects.get(id=bid)
    if reply.writer == request.user:
        if request.method == "GET":
            replyform = Replyform(instance=reply)
            return render(request, "reply/createreply.html", { 'replyform': replyform})
        elif request.method == "POST":
            replyform = Replyform(request.POST, instance=reply)
            if replyform.is_valid():
                reply = replyform.save(commit=False)
                reply.save()
            return redirect('/reply/readreply/'+str(reply.id))
        else:
            return redirect('/reply/readreplylist')


