from django.http import HttpResponse
from rest_framework.views import APIView

from .conf import portal_url


class MainPageView(APIView):
    """ Главная страница API
    """
    
    def get(self, request):
        html = f'''
<html>
  <head>
  <style type="text/css">
    a {{
      text-decoration:none!important;
      color: black;
      margin-left: 5px;
      margin-right: 5px;
    }}
    a:hover {{
      text-decoration:none!important;
      color: blue;
      margin-left: 5px;
      margin-right: 5px;
    }}
  </style>
  </head>
  <body>
    <a href="{ portal_url }">Перейти в портал</a>
    <a href="/admin">Перейти в панель администратора</a>
  </body>
</html>'''

        return HttpResponse(html)
