from django import forms
from .import models
import requests
bot_token="5463911309:AAH1DaBPvloDLDJZzmu78TnZk-UQvZLyIKk"



class ContactForm(forms.ModelForm):
    class Meta:
        model=models.Contact
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={ "type":"text", 'class': 'form-control', 'placeholder': 'Your Name'}),
            'email':forms.EmailInput(attrs={ "type":"email", 'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone':forms.TextInput(attrs={ "type":"text", 'class': 'form-control', 'placeholder': 'Your number'}),
            'message':forms.Textarea(attrs={ "type":"text", 'class': 'form-control',"rows":"3", 'placeholder': 'Your Message'}),
        }
        
        def Contact(request):
            context = {
                'contact':models.Contact
            }
            
            # if request.method == "POST":
            #     models.Contact.objects.create(
            #         name = request.POST.get("name"),
            #         email = request.POST.get("email"),
            #         phone = request.POST.get("phone"),
            #         message = request.POST.get("message"),
            #     )
            #     token = "5463911309:AAH1DaBPvloDLDJZzmu78TnZk-UQvZLyIKk"
            #     text = "Sizga xabar yuborishdi: \n\n Name: " + request.POST.get("name") + "\n Email: " + request.POST.get("email") + "\n Phone: "+ str(request.POST.get("phone")) + "\n Message: "+ request.POST.get("message")
            #     url = "https://api.telegram.org/bot" + token + "/sendMessage?chat_id="
            #     requests.get(url + str(5080816748) + "&text="+ text)
            #     return context
        
class commentForm(forms.ModelForm):
    class Meta:
        model=models.comment
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={ "type":"text", 'class': 'form-control', 'placeholder': 'Your Name'}),
            'email':forms.EmailInput(attrs={ "type":"email", 'class': 'form-control', 'placeholder': 'Your Email'}),
            'message':forms.Textarea(attrs={ "type":"text", 'class': 'form-control',"rows":"3", 'placeholder': 'Your Message'}),
        }
        