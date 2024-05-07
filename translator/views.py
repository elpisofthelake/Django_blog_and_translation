from django.shortcuts import render
from . import translate

# Create your views here.
def translator_view(request):
    if request.method == 'POST':
        origin_text = request.POST['my_textarea']
        output = translate.translate(origin_text)
        return render(request, 'translator.html',{'output_text':output, 'original_text':origin_text})
            
    else:
        return render(request,'translator.html')