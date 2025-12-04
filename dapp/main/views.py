from django.http import HttpResponse
from rest_framework.views import APIView



class MainPageView(APIView):
    """ Главная страница API
    """
    
    def get(self, request):
        html = '<html><body><a href="/admin">Перейти в панель администратора</a></body></html>'
        return HttpResponse(html)
