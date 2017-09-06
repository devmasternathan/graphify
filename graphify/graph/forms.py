from django import forms

class GraphifyForm(forms.Form):
    file_input = forms.FileField(required=True,
                                 widget=forms.FileInput(attrs={
                                     'class': 'form-control',
                                      'name': 'file'
                                      }))
    display_num = forms.ChoiceField(required=True,
                                    choices = (
                                    ("FIVE",5),
                                    ("TEN", 10)
                                    ),
                                    label="",
                                    initial="FIVE",
                                    widget=forms.Select(attrs={
                                        'class': 'form-control',
                                         'name': 'display_num'
                                         }))
