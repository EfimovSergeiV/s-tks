from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

'''
def signature_generator(request):
    """ Генератор электронных подписей для сотрудников """

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            worker_link = data['worker'].replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11]
            private_link = data['private'].replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11]

            whatsapp = data['whatsapp'].replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11] if data['whatsapp'] != 'None' else private_link
            telegramm = data['telegramm'].replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")[0: 11] if data['telegramm'] != 'None' else private_link

            context = {
                    'name': data['name'],
                    'job': data['job'],
                    'worker': data['worker'],
                    'private': data['private'],
                    'worker_link': worker_link,
                    'private_link': private_link,
                    'whatsapp': whatsapp,
                    'telegramm': telegramm,
                }

            signature = render_to_string('sb.html', context)

            with open('files/signature.html', 'w') as static_file:
                static_file.write(signature)

            return render(request, 'sb.html', context)

    else:
        form = NameForm()


    return render(request, 'sb-generator.html', {})

'''



def signature_generator(request):

    context = {
            'name': "data['name']",
            'job': "data['job']",
            'worker': "data['worker']",
            'private': "data['private']",
            'worker_link': "worker_link",
            'private_link': "private_link",
            'whatsapp': "whatsapp",
            'telegramm': "telegramm",
        }

    signature = render_to_string('email.html', context)

    # with open('files/signature.html', 'w') as static_file:
    #     static_file.write(signature)

    # return render(request, 'email.html', context)
    return HttpResponse(signature)
