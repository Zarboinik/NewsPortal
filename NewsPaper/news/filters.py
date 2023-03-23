from django.forms import DateTimeInput
from django import forms
from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Post, Category


class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label="Все Категории",
        label="Категории",
        widget=forms.Select(attrs={'class': 'form-control'}),

    )

    added_after = DateTimeFilter(
        label='Сатьи позже указываемой даты',
        field_name='time_create',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
