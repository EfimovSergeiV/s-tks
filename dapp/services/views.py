from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *



class SignatureGeneratorView(APIView):
    """ Генератор электронных подписей для сотрудников """

    def get(self, request):

        users = [
            {"id": 1, "name" : "Cергей Иванов"},
            {"id": 2, "name" : "Сергей Ефимов"},
            {"id": 3, "name" : "Алабай Лохматый"},
            {"id": 4, "name" : "Вася Никитин"},
        ]

        templates = [
            {"id": 1, "name" : "Базовый шаблон 1"},
            {"id": 2, "name" : "Базовый шаблон 2"},
            {"id": 3, "name" : "Базовый шаблон 3"},
            {"id": 4, "name" : "Базовый шаблон 4"},
        ]

        return Response({ "users": users, "templates": templates })
    
    def post(self, request):
        data = request.data

        worker_link = data['work_phone'].replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11]
        mobile_link = data['mobile'].replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11]

        whatsapp = data.get('whatsapp').replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11] if data.get('whatsapp') else worker_link
        telegramm = data.get('telegramm').replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11] if data.get('telegramm') else mobile_link

        context = {
            "name": data.get("name"),
            "job": data.get("job"),

            "work_phone": data.get("work_phone"),
            "worker_link": worker_link,
            
            "mobile": data.get("mobile"),
            "mobile_link": mobile_link,
            
            "whatsapp": whatsapp,
            "telegramm": telegramm,
        }

        signature = render_to_string('email.html', context)

        return HttpResponse(signature)
