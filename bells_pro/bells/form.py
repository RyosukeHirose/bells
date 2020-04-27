from django import forms
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from mdeditor.fields import MDTextFormField # 追加

User = get_user_model()


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )

    username = forms.CharField(
        label="ユーザーネーム",
        strip=False
    )


    class Meta:
        model = User
        # if User.USERNAME_FIELD == 'email':
        fields = ('username', 'email')
        # else:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='メールアドレス'
    )

    
 
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'detail', 'trainer')


# mediumeditorの場合のフォーム
# from mediumeditor.widgets import MediumEditorTextarea
class MyForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # widgets = {
        #     'detail': MediumEditorTextarea(),
        # }
        fields = ('title', 'detail',)