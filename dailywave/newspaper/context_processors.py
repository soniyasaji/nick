from newspaper.models import Newspaper

def menu_links(request):
    links=Newspaper.objects.all()
    return {'links':links}



