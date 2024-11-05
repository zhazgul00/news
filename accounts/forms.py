from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
        "username",
        "email",
        "age",
        ) 

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )
        exclude = ('password',) 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'password' in self.fields:
            del self.fields['password']
