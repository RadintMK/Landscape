from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='Ваш email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    subject = forms.ChoiceField(choices=[
        ('Вопрос', 'Вопрос'),
        ('Предложение', 'Предложение'),
        ('Отзыв', 'Отзыв'),
        ('Консультация по заказу', 'Консультация по заказу')
    ], label='Тема сообщения')
