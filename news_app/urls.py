from django.urls import path
from .views import (news_list, news_detail, homePageView, ContactPageView, singlePageView, HomePageView,
                    LocalNewsView, GlobalNewsView, TechnologyNewsView, SportNewsView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('single-page/', singlePageView, name='single_page'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('global-news/', GlobalNewsView.as_view(), name='global_news_page'),
    path('technology-news/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page')
]