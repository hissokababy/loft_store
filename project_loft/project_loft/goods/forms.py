from django_svg_image_form_field import SvgAndImageFormField
from django import forms

from goods.models import Category

class GetIcon(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []
        field_classes = {
            'icon': SvgAndImageFormField,
        }