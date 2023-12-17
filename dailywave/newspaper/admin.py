from django.contrib import admin
from newspaper.models import Newspaper,News_Type
from newspaper.models import Video

admin.site.register(Newspaper)
admin.site.register(News_Type)
admin.site.register(Video)
