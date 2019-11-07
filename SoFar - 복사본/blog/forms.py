from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    title = forms.CharField(
        max_length=50,
        label="제목",
        help_text="50자 이내로 작성해주세요.",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "제목을 입력해주세요."
            }
        )
    )

    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                'class' : 'from-control',
                'placeholder' : '내용을 입력해주세요.'
            }
        )
    )

    image = forms.ImageField(
        help_text="그림파일을 업로드해주세요.",
        widget=forms.FileInput(),
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    
    content = forms.CharField(
        max_length=100,
        label="댓글달기",
        help_text="남을 비방하는 댓글은 작성하지 마세요.",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "댓글을 작성해주세요."
            }
        )
    )