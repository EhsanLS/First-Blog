
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import FormMixin

from .models import Article, Comment
from .forms import CommentForm


# Create your views here.


class ArticleListView(ListView):
    template_name = 'blog/home.html'
    model = Article
    context_object_name = 'articles'
    ordering = ['-created_at']


class SiteFooterComponentView(TemplateView):
    template_name = 'blog/site_footer_component.html'


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


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        approved_comments = Comment.objects.filter(article=self.object, is_approve=True)
        context['comments'] = approved_comments
        comments_count_in_persian = persian_numbers_converter(str(approved_comments.count()))
        context['comments_count'] = comments_count_in_persian
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return self.request.path
