from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # name = 'Morghan'
    # context = {
    #     'name': 'Morghan',
    #     'age': 23,
    #     'nationality':'American'
    # }
    return render(request, 'index.html')# context) #last param is for sending in dynamic data

def counter(request):
    text = request.POST['text'] #its getting the textarea in index.html bc its name is text and storing the text in this var. make sure the post/get matches w wats in whatever is sending to it
    num_words = len(text.split())
    return render(request, 'counter.html', {'num': num_words})