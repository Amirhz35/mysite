from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + '...'


@register.inclusion_tag('blog/sidebar/blog-popular-post.html')
def popularpost():
    posts = Post.objects.filter(status=1).order_by('published_date')
    return {'posts':posts}

@register.inclusion_tag('blog/sidebar/blog-post-category.html')
def postcategories():
    post = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=post.filter(category=name).count()
    return {'categories':cat_dict}