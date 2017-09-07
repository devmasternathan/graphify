from django import forms

class GraphifyForm(forms.Form):
    file_input = forms.FileField(required=True,
                                 widget=forms.FileInput(attrs={
                                     'class': 'form-control',
                                      'name': 'file'
                                      }))
    display_num = forms.ChoiceField(required=True,
                                    choices = (
                                    (5,"five"),
                                    (10, "ten")
                                    ),
                                    label="",
                                    initial="FIVE",
                                    widget=forms.Select(attrs={
                                        'class': 'form-control',
                                         'name': 'display_num'
                                         }))
