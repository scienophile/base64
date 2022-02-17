from django.shortcuts import render

import base64

def index(request):
    context = {}
    if request.method == 'POST':
        text = request.POST.get('input')
        charset = request.POST.get('charset')
        print(text)
        print(charset)
        if text and charset:
            if request.POST.get('decode'):
                data = base64.b64decode(text)
                context['output'] = data.decode(charset)
            elif request.POST.get('encode'):
                encoded_text = text.encode(charset)
                output_text = base64.b64encode(encoded_text)
                context['output'] = output_text.decode(charset)

    return render(request, 'bin2text/index.html', context)

