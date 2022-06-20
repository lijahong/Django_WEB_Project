from django.db.models import Q
from django.shortcuts import render, redirect
from reply.models import Reply
from reply.form import Replyform

def createreply(request):
    if request.method == "GET":
        replyform = Replyform()
        return render(request, "reply/createreply.html", { 'replyform': replyform})
    elif request.method == "POST":
        replyform = Replyform(request.POST)
        if replyform.is_valid():
            reply = replyform.save(commit=False)
            print(reply)
            reply.save()
        return redirect('/reply/readreply/'+str(reply.id))

def readreplylist(request):
    replys = Reply.objects.all().order_by('id')
    return render(request,'reply/readreplylist.html',{ 'replylist':replys})

def readreply(request, bid):
    reply = Reply.objects.filter(Q(id=bid))
    return render(request,'reply/readreply.html',{ 'reply':reply})

def deletereply(request, bid):
    reply = Reply.objects.get(id=bid)
    reply.delete()
    return redirect('/reply/readreplylist')

def updatereply(request, bid):
    reply = Reply.objects.get(id=bid)
    if request.method == "GET":
        replyform = Replyform(instance=reply)
        return render(request, "reply/createreply.html", { 'replyform': replyform})
    elif request.method == "POST":
        replyform = Replyform(request.POST, instance=reply)
        if replyform.is_valid():
            reply = replyform.save(commit=False)
            reply.save()
        return redirect('/reply/readreply/'+str(reply.id))


