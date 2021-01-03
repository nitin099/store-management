from django import forms


class WebhookForm(forms.Form):
    topic = forms.CharField()
    address = forms.URLField()
    format_type = forms.CharField()

    def clean(self):
        data = self.cleaned_data
        form_data = {
            'webhook': {
                'topic': data['topic'],
                'address': data['address'],
                'format': data['format_type']
            }
        }
        return form_data
