from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index_view(requests):
    return render(requests,'website/index.html')
    
def about_view(requests):
    return render(requests,'website/about.html')

#def about_view2(requests):
#    template = loader.get_template('website/about2.html')
#    return HttpResponse(template.render())


def contact_view(requests):
    return render(requests,'website/contact.html')