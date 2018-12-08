from django.contrib.syndication.views import Feed
from .models import Post

class AllPostRssFeed(Feed):
    title = "Hervie 个人博客"
    link = '/'
    description = 'Hervie 个人博客'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' %(item.category, item.title)

    def item_description(self, item):
        return item.content