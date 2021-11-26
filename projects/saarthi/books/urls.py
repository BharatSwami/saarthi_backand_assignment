from django.urls import path
from django.conf.urls import url 
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('api',views.api,name='api'),
    #path('findByName',views.findbyName,name='name'),
    url(r'^api/v1/books/:[0-9]+/updateTablesecond',views.updateTablesecond),
    url(r'^api/external-books/findbyPublisher',views.findbyPublisher),
    url(r'^api/external-books/findbyName',views.findbyName),
    url(r'^api/external-books/findbyCountry',views.findbyCountry),
    url(r'^api/external-books/publisher',views.publisherfinding),
    url(r'^api/external-books/name',views.namefinding),
    url(r'^api/external-books/country',views.countryfinding),
    url(r'^api/external-books/',views.external_books),
    url(r'^api/v1/books\?name:=',views.finding),
    url(r'^api/v1/books\?country:=',views.finding),
    url(r'^api/v1/books/updateTablesecond', views.updateTablesecond),
    url(r'^api/v1/books/:[0-9]+/update', views.update),
    url(r'^api/v1/books/:[0-9]+/delete', views.deleteding),
    url(r'^api/v1/books/:[0-9]+', views.process),
    url(r'^api/v1/books$', views.books),
    url(r'^api/v1', views.search_options),
    url(r'^api/v1/books(?P<pk>[0-9]+)$', views.books),
    url(r'^api/', views.api_options)
    #url(r'^api/v1/published$', views.tutorial_list_published)

    #path('api/v1/books',views.books,name='books')
]