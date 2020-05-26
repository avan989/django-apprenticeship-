from django.shortcuts import render
from post.models import Post


# Create your views here.
def landing(request):

    entries = Post.objects.all().order_by("-created")[0:3]
    context = {"entries": entries}

    return render(request, "landing.html", context)
