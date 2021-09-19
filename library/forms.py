from django import forms 
from .models import * 
  
class AddBookForm(forms.ModelForm):
  class Meta:
    model = Book 
    fields = ["book_name","author","category"]
    
    