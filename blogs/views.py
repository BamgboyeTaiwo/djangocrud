from django.shortcuts import redirect, render
from blogs.models import Post
from .forms import Postform
from django.views.generic import ListView, DetailView, UpdateView,DeleteView,CreateView
from django.urls import reverse,reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
        

def index(request):
    return render(request, 'blogs/index.html' )

# def PostCreateView(request):
#     model = Post
#     fields = “__all__”
#     success_url  = reverse_lazy(“blog:all”)
#     if request.method=="POST":
#         name=request.POST['name']
#         age=request.POST['age']
#         address=request.POST['address']
#         obj=Post.objects.create(name=name,age=age,address=address)
#         obj.save()
#         return redirect('/')

# def PostDetailView(request):
#     model = Post
#     fields = “__all__”
#     success_url  = reverse_lazy(“blog:all”)
#     Post=Post.objects.all()
#     return render(request,'blogs/retrieve.html',{'Post':Post})

# def edit(request,id):
#     object=Post.objects.get(id=id)
#     return render(request,'blogs/edit.html',{'object':object})
    
# def PostUpdateView(request,id):
#     model = Post
#     fields = “__all__”
#     success_url  = reverse_lazy(“blog:all”)
#     object=Post.objects.get(id=id)
#     form=Postform(request.POST,instance=object)
#     if form.is_valid:
#         form.save()
#         object=Post.objects.all()
#         return redirect('retrieve')

# def PostDeleteView(request,pk):   
#         model = Post
#         fields = “__all__”
#         success_url  = reverse_lazy(“blog:all”)
#         Post.objects.filter(id=pk).delete()
#         return redirect('retrieve')