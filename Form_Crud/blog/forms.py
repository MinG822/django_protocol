from django import forms

class ArticleForm(forms.Form):
    # simple
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea())

    # options
    title = forms.CharField(
        max_length=50,
        label="제목",
        help_text="50자 이내로 작성해주세요",
        widget = forms.TextInput(
            attrs={
            "class" : "form-control",
            "placeholder" : "제목을 입력해주세요.",
            }
        )
    )
    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                "class" : "form-control",
                "placeholder" : "내용을 입력해주세요.",
            }
        )
    )
