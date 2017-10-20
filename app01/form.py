#!/user/bin/env python
# -*-coding:utf-8-*-
from django import forms

class Photo(forms.Form):
    photo = forms.ImageField()
    choic= [
        (1,'第一次 青岛'),
        (2,'第二次 南京'),
        (3,'第三次 青岛'),
        (4,'第四次 南京'),
        (5,'第五次 青岛'),
    ]
    type = forms.ChoiceField(choices=choic)
    address = forms.CharField(max_length=32)
