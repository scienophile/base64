from django.shortcuts import render
from .models import CryptData
from datetime import datetime

import base64


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    context = {}
    if request.method == 'POST':
        text = request.POST.get('input')
        charset = request.POST.get('charset')
        crypt_type = ''
        if text and charset:
            if request.POST.get('decode'):
                data = base64.b64decode(text)
                context['output'] = data.decode(charset)
                crypt_type = 'de'
            elif request.POST.get('encode'):
                encoded_text = text.encode(charset)
                output_text = base64.b64encode(encoded_text)
                context['output'] = output_text.decode(charset)
                crypt_type = 'en'

            crypt_data = CryptData(input_text = text, crypt = crypt_type, crypt_date = datetime.now(), guess_ip = get_client_ip(request), output_text = context['output'])
            crypt_data.save()

    return render(request, 'bin2text/index.html', context)
