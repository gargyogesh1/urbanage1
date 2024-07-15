from django import forms
from .models import Contact_us
from .validators import is_basic_valid_indian_number



class ContactForm(forms.ModelForm):
    phone_no = forms.CharField(
        max_length=10,
        required=True,
        validators=[is_basic_valid_indian_number],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'})
    )
    
    class Meta:
        model = Contact_us
        fields = ['name', 'phone_no','email', 'amount']
        # list_display = ('name', 'phone_no','email', 'properties', 'investment')
        # search_fields = ('name', 'email', 'subject')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            # 'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number' }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            # 'property': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.Textarea(attrs={ 'class': 'form-control',  'placeholder': 'Your Message', 'rows': 4}),
        }
