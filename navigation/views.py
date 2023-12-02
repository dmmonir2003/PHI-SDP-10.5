from django.shortcuts import render

# Create your views here.
def about(request):
    days=[
{'name': 'Dave', 'age': 22},
{'name': 'Joe', 'age': 31},
{'name': 'Josh', 'age': 19},
]
    return render(request,('about.html'),{'daya':days})

def contact(request):
    return render(request,('contact.html'))