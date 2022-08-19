# Copyright 2022 user
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .models import Details
from django.forms import ModelForm
from django import forms

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'message': 'Message',
        }
        help_texts = {
            'name': '',
            'email': '',
            'phone': '',
            'message': '',
        }
        error_messages = {
            'name': {
                'required': 'Name is required.',
            },
            'email': {
                'required': 'Email is required.',
            },
            'phone': {
                'required': 'Phone is required.',
            },
            'message': {
                'required': 'Message is required.',
            },
        }
        field_classes = {
            'name': forms.CharField,
            'email': forms.EmailField,
            'phone': forms.CharField,
            'message': forms.CharField,
        }
        localized_fields = {
            'name': 'name',
            'email': 'email',
            'phone': 'phone',
            'message': 'message',
        }
        localized_labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'message': 'Message',
        }
        localized_help_texts = {
            'name': '',
            'email': '',
            'phone': '',
            'message': '',
        }
        