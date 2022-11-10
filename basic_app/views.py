from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView,CreateView
from .import models,forms
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import requests

bot_token="AAH1DaBPvloDLDJZzmu78TnZk-UQvZLyIKk"
chats = [5080816748]
# Create your views here.

class Index(CreateView):
    template_name='index.html'
    model=models.Contact
    form_class=forms.ContactForm
    success_url=reverse_lazy('basic_app:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Services"] = models.Services.objects.all()
        context["Facts"] = models.Facts.objects.all()
        context["Team"] = models.Team.objects.all()
        context["Price"] = models.Price.objects.all()
        # context["Blog"] = models.Blog.objects.all()
        context["blog"] = models.Blog2.objects.all()
        context["Testimonial"] = models.Testimonial.objects.all()

        return context

# class Blog(TemplateView):
#     template_name = "blog.html"


def Blog(request, id=None):
    com = models.comment.objects.all()
    context = {
        "contact":com,
    }
    
    if request.method=="POST":
        form = forms.commentForm(request.POST)
        if form.is_valid():
            obj = models.comment() #gets new object
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            obj.message = form.cleaned_data['message']
            #finally save the object in db
            obj.save()
            
        token = "5463911309:AAH1DaBPvloDLDJZzmu78TnZk-UQvZLyIKk"
        text = "Sizga xabar yuborishdi: \n\n Ism: " + request.POST.get("name") + "\n Email: "+ str(request.POST.get("email")) + "\n Message: "+ request.POST.get("message")
        url = "https://api.telegram.org/bot" + token + "/sendMessage?chat_id="
        requests.get(url + str(5080816748) + "&text="+ text)
        
    Comment1=forms.commentForm()
            
    if id:
        try: 
            blog = models.Blog2.objects.get(id=id)
        except models.Blog2.DoesNotExist:
            blog = get_object_or_404(models.Blog2, id=id)
            blog = None      
    else:
        blog = models.Blog2.objects.order_by('?').first()
    return render(request, 'blog.html', {'blog': blog, 'Comment':Comment1, "com":com, "context":context})






# class Blog2(TemplateView):
#     template_name='blog.html'
#     model=models.comment
#     # form_class=forms.commentForm
#     # success_url=reverse_lazy('basic_app:blog')
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["comment"] = models.comment.objects.all()

#         return context