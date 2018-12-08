from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('contact/post/',views.post_contact, name='post_contact'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('archives/<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),
    path('categories/<int:pk>', views.CategoryView.as_view(), name='categories'),
    path('tags/<int:pk>', views.TagView.as_view(), name='tags'),
    path('search/', views.search, name='search'),
]

# app_name = 'blog'
