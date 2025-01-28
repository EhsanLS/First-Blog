from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm


# Create your views here.

def home_page(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'blog/home.html', context)


def site_footer_component(request):
    return render(request, 'blog/site_footer_component.html')


def persian_numbers_converter(x):
    result = ''
    numbers = {
        '0': '\u06f0',
        '1': '\u06f1',
        '2': '\u06f2',
        '3': '\u06f3',
        '4': '\u06f4',
        '5': '\u06f5',
        '6': '\u06f6',
        '7': '\u06f7',
        '8': '\u06f8',
        '9': '\u06f9'
    }
    for i in numbers.keys():
        if i == x:
            result = numbers.get(i)
    return result


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter(is_approve=True)
    comments_count = comments.count()
    comments_count_final = persian_numbers_converter(str(comments_count))
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('blog:article_detail', slug=article.slug)
    else:
        form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'form': form,
        'comments_count': comments_count_final
    }
    return render(request, 'blog/article_detail.html', context)
