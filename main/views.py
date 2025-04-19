from django.shortcuts import render, redirect
from .form import ContactForm
import requests

TELEGRAM_BOT_TOKEN = '7909679143:AAFoYpbSBajeDYognd0gYTNRMSdxyjTRxg0'
TELEGRAM_CHAT_ID = '7608366780'

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            text = f"""
📩 Новое сообщение с портфолио:
👤 Имя: {contact.name}
✉️ Email: {contact.email}
📌 Тема: {contact.subject}
🌐 Телеграм: {contact.telegram_username}
📝 Сообщение: {contact.message}
"""
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            requests.post(url, data={'chat_id': TELEGRAM_CHAT_ID, 'text': text})

            return redirect('success')
        else:
            print(form.errors)
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

def success(request):
    return render(request, 'success.html')
