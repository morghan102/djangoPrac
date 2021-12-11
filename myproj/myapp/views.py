from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # name = 'Morghan'
    # context = {
    #     'name': 'Morghan',
    #     'age': 23,
    #     'nationality':'American'
    # }
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_trus = True
    feature1.details = 'Our service is quick'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Smart'
    feature4.is_trus = False
    feature4.details = 'Our service is smart'
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Cool'
    feature3.is_trus = True
    feature3.details = 'Our service is cool'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_trus = True
    feature2.details = 'Our service is reliable'

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features': features})# context) #last param is for sending in dynamic data

def counter(request):
    text = request.POST['text'] #its getting the textarea in index.html bc its name is text and storing the text in this var. make sure the post/get matches w wats in whatever is sending to it
    num_words = len(text.split())
    return render(request, 'counter.html', {'num': num_words})