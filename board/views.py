from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from board.form import PostForm
from board.models import Post
from reply.form import Replyform


@login_required(login_url = '/user/login')
def createBoardGet(request):
    if request.method == "GET":
        postform = PostForm()
        context = {'postform': postform }
        return render(request, "board/getdata.html", context)
    elif request.method == "POST":
        postForm = PostForm(request.POST)# form data를 form instance에 저장
        if postForm.is_valid():  # 유효성 검증
            post = postForm.save(commit=False)# 원래 save하면 db에 저장되는데, 이를 false로 하면 저장을 안하고,DB 객체를 반환한다. 중복데이터나 오류를 미리 알아낼 수 있게 해줌
            post.writer = request.user #작성자 설정, 이 설정을 안하면 writer를 form에서 exclude했기에 유효성 검사는 통과하지만 null값이 들어간다
            post.save()
        return redirect('readdata/'+str(post.id))

def readlist(request): #전체 리스트
    #ids = request.Get.get('id',None) #get방식으로 주소창에 원하는 id를 입력받음
    board_get_data = Post.objects.all().order_by('-id') #id오름차순으로 정렬
    context = {
       'datas': board_get_data
    }
    return render(request, "board/readlist.html", context)

def readdata(request, bid): #단일 게시물
    # prefetch_related
    post = Post.objects.prefetch_related('reply_set').get(id=bid) #reply 요소가 reply_set으로 들어감
    #post = Post.objects.get(id=bid)
    replyform = Replyform()
    context = {'post': post, 'replyform':replyform}
    return render(request, 'board/readdata.html', context)

@login_required(login_url = '/user/login')
def deleteget(request, bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board/readlist')
    else:
        post.delete()
        return redirect('/board/readlist')

@login_required(login_url = '/user/login')
def updateget(request, bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board/readlist')
    else:
        if request.method == "GET":
            postform = PostForm(instance=post) #조회한 post의 글을 가져와서 form에 넣어줌
            context = {'postform': postform}
            return render(request, "board/getdata.html", context)
        elif request.method == "POST":
            postForm = PostForm(request.POST, instance=post)
            if postForm.is_valid():
                post = postForm.save(commit=False)
                post.save()
                return redirect('/board/readdata/' + str(bid))

@login_required(login_url = '/user/login')
def like(request,bid):
    post = Post.objects.get(id=bid)
    post.like.add(request.user) #like에는 게시글 정보와 user 정보가 둘 다 필요하므로 user를 넣어준다
    return JsonResponse({'message':'ok'})

