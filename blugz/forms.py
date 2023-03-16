from django import forms
from .models import Post, Category





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden' }),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=Category.objects.all().values_list('id', 'name')),
            'body': forms.Textarea(attrs={'class': 'form-control'}),           
        }



from django import forms
from .models import Post


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  ('title', 'title_tag', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
    
    