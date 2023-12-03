from django.urls import path
from .views import (news_list, news_detail, homePageView, ContactPageView, singlePageView, HomePageView,
                    LocalNewsView, GlobalNewsView, TechnologyNewsView, SportNewsView, NewsUpdateView, NewsDeleteView,
                    NewsCreateView, admin_page_view, SearchResultsList)

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/<slug>/edit', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('single-page/', singlePageView, name='single_page'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('global-news/', GlobalNewsView.as_view(), name='global_news_page'),
    path('technology-news/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('searchresult/', SearchResultsList.as_view(), name='search_results'),
]