from django.shortcuts import render

# Create your views here.
from board.models import Post


def mainPage(request):
    return render(request, 'board/index.html')


def createBoardGet(request):
    return render(request, "board/getdata.html")

def createBoardPost(request):
    board_data = Post()
    board_data.title = request.POST.get('btitle',None)
    board_data.contents = request.POST.get('bcontent',None)
    print(board_data.title)
    board_data.save()
    return render(request, "board/postresult.html")

def createReadBoard(request):
    board_get_data = Post.objects.all()
    context = {
       'datas': board_get_data
    }
    return render(request, "board/readData.html", context)