from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .form import PostForm, ConfirmPasswordForm
from django.views.generic.edit import UpdateView

def post_main(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()  

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'form':form, "posts":posts}
    return render(request, 'blog/post_main.html',context)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()    
    return render(request,'blog/post_edit.html',{'form':form})


def post_auth(request,pk):
    post = get_object_or_404(Post, pk=pk) 

    if post.password is not None:
        # 구현필요  
        return render(request, 'blog/post_auth.html', {'post':post})
 
    return redirect('post_edit', pk=post.pk)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) 

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'form':form, "posts":posts}
    return render(request, 'blog/post_main.html',context)   
    #return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_main')


class ConfirmPasswordView(UpdateView):
    form_class = ConfirmPasswordForm
    template_name = 'blog/post_auth.html'

    def get_object(self):
        return self.request.post

    def get_success_url(self):
        return self.request.get_full_path()


'''   
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
'''