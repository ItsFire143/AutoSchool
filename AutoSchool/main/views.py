from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import FileResponse, Http404, HttpResponse


def homepage(request):
    return render(request, 'main/home.html')


def applications(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        try:
            send_mail(
                'Новая заявка',
                f'Fullname:{full_name}\nphone:{phone}\nemail:{email}',
                'omegaschool@mail.ru',
                ['omegaschool@mail.ru'],
                fail_silently=False,
            )
            print(full_name, phone, email)
        except BadHeaderError:
            return HttpResponse('Некорректный заголовок письма.')
        return render(request, 'main/apps.html')
    return render(request, 'main/apps.html')


def contact(request):
    return render(request, 'main/contacts.html')


def programs(request):
    return render(request, 'main/programs.html')


def org(request):
    return render(request, 'main/organis.html')


def shcool(request):
    return render(request, 'main/school.html')


def prof(request):
    return render(request, 'main/profile.html')