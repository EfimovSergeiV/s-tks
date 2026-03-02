from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from random import randint, sample

class SignatureGeneratorView(APIView):
    """ Генератор электронных подписей для сотрудников """

    def get(self, request):
        users = UserSerializer(EmployeesModel.objects.all(), many=True).data
        templates = SignatureSerializer(SignatureGeneratorModel.objects.all(), many=True ).data

        return Response({ "users": users, "templates": templates })
    
    def post(self, request):
        data = request.data

        try:
            worker_link = data.get('work_phone').replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11]
            mobile_link = data.get('mobile').replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11]
            whatsapp = data.get('whatsapp').replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11] if data.get('whatsapp') else mobile_link
            telegramm = data.get('telegramm').replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11] if data.get('telegramm') else mobile_link
        except:
            worker_link = ""
            mobile_link = ""
            whatsapp = ""
            telegramm = ""


        context = {
            "name": data.get("name"),
            "job": data.get("job"),

            "work_phone": data.get("work_phone"),
            "worker_link": worker_link,
            
            "mobile": data.get("mobile"),
            "mobile_link": mobile_link,
            
            "whatsapp": whatsapp,
            "telegramm": telegramm,

            "banner_images": [],
            "logo": None,
        }

        # print(f"context : { context }")


        if data.get("template"):
            template = SignatureGeneratorModel.objects.filter(id=data.get("template")["id"]).first()
            signature = SignatureSerializer(template, context={"request": request}).data

            context["banner_images"] = signature.get("banner_images", [])
            context["catalogs"] = signature.get("catalogs", [])
            context["logo"] = signature.get("logo", None)

        signature = render_to_string('email.html', context)

        return HttpResponse(signature)



class AccessConfView(APIView):
    """  """
    
    def post(self, request):
        data = request.data

        # service_name service_secret credentials
        qs = AccessConfModel.objects.get(service_name=data.get("service_name"))


        if qs and qs.service_secret == data.get("service_secret"):
            return JsonResponse(qs.credentials)
        
        else:
            key_string = "cNW0FykDvkwDN172hR8y7IbTxXiOSVYDdIMwMkm5cYw"
            data = {
                "ip": f"{randint(1,255)}.{randint(1,255)}.{randint(1,255)}.{randint(1,255)}",
                "key": ''.join(sample(key_string, k=len(key_string)))
            }
            return JsonResponse(data)