from django import forms
from django.contrib.auth.models import User
from webapp.models import Transaction_Pairs
from webapp.models import Transaction_history
#from webapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields = ('username','email','password')

class TransactionForm(forms.ModelForm):

    people=forms.CharField(widget=forms.TextInput(attrs={'class':'inputField'}))
    reason=forms.CharField(widget=forms.TextInput(attrs={'class':'inputField'}))
    
    class Meta():
        model=Transaction_Pairs
        fields=('amount',)

class TransactionHistory(forms.Form):
    person_name=forms.CharField()

#class UserProfileInfoForm(forms.ModelForm):
   # class Meta():
      #  model=UserProfileInfoFormfields=('portfolio_site','profile_pic')
