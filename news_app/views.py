from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import ContactForm
from django.views.generic import TemplateView, ListView

# Create your views here.
def news_list(request):
    # news_list = News.objects.filter(status=News.Status.Published)
    news_list = News.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }

    return render(request, 'news/news_detail.html', context)

def homePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-published_time')
    local_news = News.published.all().filter(category__name='Mahalliy')
    global_news = News.published.all().filter(category__name='Xorij')
    technology_news = News.published.all().filter(category__name='Texnologiya')
    sport_news = News.published.all().filter(category__name='Sport')
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news,
        'global_news': global_news,
        'technology_news': technology_news,
        'sport_news': sport_news
    }

    return render(request, 'news/home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()
        context['news_list'] = News.published.all().order_by('-published_time')
        context['local_news'] = News.published.all().filter(category__name='Mahalliy').order_by('-published_time')
        context['global_news'] = News.published.all().filter(category__name='Xorij')
        context['technology_news'] = News.published.all().filter(category__name='Texnologiya')
        context['sport_news'] = News.published.all().filter(category__name='Sport')
        return context

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h2> Biz bilan boglanganingiz uchun tashakkur</h2>')
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)

def singlePageView(request):
    context = {

    }

    return render(request, 'news/single-page.html')

class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news

class GlobalNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorijiy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news

class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = 'texnologik_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news