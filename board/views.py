from django.shortcuts import render, redirect

# Create your views here.
from board.form import PostForm
from board.models import Post


def mainPage(request):
    return render(request, 'board/index.html')

def createBoardGet(request):
    if request.method == "GET":
        postform = PostForm()
        context = {'postform': postform}
        return render(request, "board/getdata.html", context)
    elif request.method == "POST":
        postForm = PostForm(request.POST)  # FORM에게 전달해주면 알아서 객체에 저장해줌
        if postForm.is_valid():  # 유효성 검증
            post = postForm.save(
                commit=False)  # 원래 save하면 db에 저장되는데, 이를 false로 하면 저장을 안하고, model을 반환한다. 중복데이터나 오류를 미리 알아낼 수 있게 해줌
            post.save()
        return redirect('readGet/'+str(post.id))

def createReadBoard(request):
    #ids = request.Get.get('id',None) #get방식으로 주소창에 원하는 id를 입력받음
    board_get_data = Post.objects.all().order_by('-id') #id오름차순으로 정렬
    context = {
       'datas': board_get_data
    }
    return render(request, "board/readData.html", context)

def readGet(request, bid):
    post = Post.objects.filter(id=bid)
    print(post)
    context = {'post': post}
    return render(request, 'board/readget.html', context)

def deleteget(request, bid):
    post = Post.objects.get(id=bid)
    post.delete()
    return redirect('/board/readdata')

def updateget(request, bid):
    post = Post.objects.get(id=bid)
    if request.method == "GET":
        postform = PostForm(instance=post) #조회한 post의 글을 가져와서 form에 넣어줌
        context = {'postform': postform}
        return render(request, "board/getdata.html", context)
    elif request.method == "POST":
        postForm = PostForm(request.POST, instance=post)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect('/board/readGet/'+str(bid))

