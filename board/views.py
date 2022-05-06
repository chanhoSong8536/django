from django.shortcuts import redirect, render
from .models import Board, Reply
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def unlikey(req,bpk):
    b = Board.objects.get(id=bpk)
    b.likey.remove(req.user)
    return redirect("board:detail", bpk)

def likey(req,bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(req.user)
    return redirect("board:detail", bpk)

def index(req):
    pg = req.GET.get("page",1)
    cate = req.GET.get("cate","")
    kw = req.GET.get("kw","")

    if kw:
        if cate == "sub":
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == "wri":
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()

        elif cate == "con":
            b = Board.objects.filter(content__contains=kw)
        else:
            b = Board.objects.all()
    else:
        b = Board.objects.all()

    b = b.order_by('-pubdate')

    pag = Paginator(b,5)
    obj = pag.get_page(pg)
    context = {
        "bset" : obj,
        "cate" : cate,
        "kw" : kw
    }
    return render(req, "board/index.html", context)



def dreply(req,bpk,rpk):
    r = Reply.objects.get(id=rpk)
    if req.user == r.replyer:
        r.delete()
    else:
        pass # 경고메세지 예정!
    return redirect("board:detail",bpk)


def creply(req,bpk):
    b = Board.objects.get(id=bpk)
    c = req.POST.get("com")
    Reply(board=b, replyer=req.user, comment=c).save()
    return redirect("board:detail",bpk)

def update(req, bpk):
    b = Board.objects.get(id=bpk)

    if b.writer != req.user:
        # 경고메세지 대기중
        return redirect("board:index")

    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        b.subject = s
        b.content = c
        b.save()
        return redirect("board:detail", bpk)
    context = {
        "b" : b
    }
    return render(req, "board/update.html", context)


def create(req):
    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        Board(subject=s, writer=req.user, content=c, pubdate=timezone.now()).save()
        return redirect("board:index")
    return render(req, "board/create.html")

def delete(req, bpk):
    b = Board.objects.get(id=bpk)
    if b.writer == req.user:
        b.delete()
    else: # hacking
        pass # 경고메세지~~
    return redirect("board:index")


def detail(req, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()

    context = {
        "b":b,
        "rset":r
    }
    return render(req, "board/detail.html",context)


