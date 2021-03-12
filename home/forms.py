from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,label='Your Name')
    email = forms.EmailField(label='Email')
    body = forms.CharField(min_length=10,max_length=1000,label='Message',widget=forms.Textarea(attrs={'rows':5,'col':2}))
    mail_subject = forms.CharField(max_length=100, label='Subject')


    def __init__(self, *args, **kwargs):

        for field_name, field in self.fields.items():
            if field_name in self._placeholders:
                self.fields[field_name].widget.attrs['placeholder'] = \
                self.fields[field_name].label

        super(ContactForm, self).__init__(*args, **kwargs)


