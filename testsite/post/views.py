from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
# from .serializers import DeveloperSerializer


# Create your views here.
def post_detail(request, pk):

    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, "post-detail.html", context)


def post_all(request):

    return render(request, "post-all.html")

# apprenticeDeveloper - viewsets handle post and get request
# class DeveloperView(viewsets.ModelViewSet):
#
#     # get all the data
#     queryset = ApprenticeshipDevelop.objects.all()
#     serializer_class = DeveloperSerializer
