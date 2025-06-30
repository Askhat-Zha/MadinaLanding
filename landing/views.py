from django.shortcuts import render
from .forms import ApplicationForm
from django.http import HttpResponse
from django.template import loader
import requests

def home(request):
    success = False

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Проверка honeypot-поля: если оно заполнено, игнорируем (бот)
            if form.cleaned_data.get('honeypot'):
                return render(request, 'landing/home.html', {
                    'form': ApplicationForm(),
                    'success': False
                })

            application = form.save()

            # Отправка в Telegram
            token = "8168444570:AAGveh-3h2GO9xPuj4QqhdSZsbfsWG0jaS4"
            chat_id = "289418091"
            text = f"📥 Новая заявка:\n\n👤 {application.name}\n📱 {application.contact}\n🎯 {application.goal or 'Без указания цели'}"

            url = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.post(url, data={"chat_id": chat_id, "text": text})

            success = True
            form = ApplicationForm()  # Очистка формы

    else:
        form = ApplicationForm()

    return render(request, 'landing/home.html', {
        'form': form,
        'success': success
    })

def robots_view(request):
    content = loader.render_to_string('robots.txt')
    return HttpResponse(content, content_type='text/plain')
