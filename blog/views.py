from django.shortcuts import render,get_object_or_404
from blog.models import Post
from datetime import datetime,timezone

def blog(requests):
    dt_now = datetime.now(timezone.utc)
    post = Post.objects.filter(published_date__lte=dt_now)
    for i in post:
        i.status = 1
        i.save()
    context = {'posts': post}
    return render(requests,'blog/blog-home.html',context)
    
def blog_single(requests,pid):
    post = get_object_or_404(Post,pk=pid,status=1)
    if post:
        post.counted_veiw += 1
        post.save()
    context = {'post': post}
    return render(requests,'blog/blog-single.html',context)

def blog_test(requests,pid):
    return render(requests,'test.html')