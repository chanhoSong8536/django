from contextlib import redirect_stderr
from django.shortcuts import redirect, render
from .models import Topic, Choice
from django.utils import timezone
# Create your views here.

def delete(req,tpk):
    t = Topic.objects.get(id=tpk)
    if req.user == t.maker:
        t.delete()
    else:
        pass # 혼내줌
    return redirect("vote:index")


def create(req):
    if req.method=="POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        cn = req.POST.getlist("cname")
        cp = req.FILES.getlist("cpic")
        cc = req.POST.getlist("ccom")
        t = Topic(subject=s, maker=req.user, content=c, pubdate=timezone.now())
        t.save()
        for name,pic,con in zip(cn,cp,cc):
            Choice(topic=t, name=name, pic=pic, con=con).save()
        return redirect("vote:index")
    return render(req, "vote/create.html")


def cancel(req,tpk):
    t = Topic.objects.get(id=tpk)
    t.voter.remove(req.user)
    req.user.choice_set.get(topic=t).choicer.remove(req.user)
    return redirect("vote:detail", tpk)


def vote(req,tpk):
    t = Topic.objects.get(id=tpk)
    if not req.user in t.voter.all():
        t.voter.add(req.user)
        cpk = req.POST.get("cho")
        c = Choice.objects.get(id=cpk)
        c.choicer.add(req.user)
    return redirect("vote:detail", tpk)


def detail(req,tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(req, "vote/detail.html", context)


def index(req):
    t = Topic.objects.all()
    context = {
        "tset" : t
    }
    return render(req, "vote/index.html",context)