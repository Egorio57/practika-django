from django import forms

from .models import ContactRequest


class ContactForm(forms.ModelForm):

    captcha = forms.IntegerField(
        label='Сколько будет 7 + 5?',
        error_messages={
            'required': 'Введите ответ.'
        }
    )

    class Meta:
        model = ContactRequest

        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ваше имя'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Ваш Email'
                }
            ),

            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Тема сообщения'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Введите сообщение...',
                    'rows': 6
                }
            ),
        }

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')

        if captcha != 12:
            raise forms.ValidationError(
                'Неверный ответ.'
            )

        return captcha