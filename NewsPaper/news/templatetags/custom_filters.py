from django import template

register = template.Library()


@register.filter()
def censor(value):
    bad_words = [("плохой", "*"),
                 ("дурак", "*"),
                 ("плохоеслово", "*")
                 ]
    text = str(value)
    for i in bad_words:
        old, new = i
        text = text.replace(old, new)

    return f'{text}'
