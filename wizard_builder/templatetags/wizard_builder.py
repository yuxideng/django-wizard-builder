from django import template


register = template.Library()


@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg}, label_suffix="")


# TODO: pull request against django-widget-tweaks ?
@register.filter(is_safe=True)
def add_aria_tags_to_field(field):
    attrs = []
    if field.help_text or field.label:
        attrs.append("aria-describedby:help-" + field.id_for_label)
    if field.field.required:
        attrs.append("aria-required:true")
    if field.errors:
        attrs.append("aria-invalid:true")
        attrs.append("aria-describedby:error-" + field.id_for_label)
    for attr in attrs:
        append_attr(field, attr)
    return field


# TODO: smell
@register.filter(name='is_extra')
def is_extra(field):
    return 'extra' in field.id_for_label


# TODO: remove, replace with widget
@register.filter(name='is_multiple_choice')
def is_multiple_choice(field):
    widget_name = field.field.widget.__class__.__name__
    return (widget_name == CheckboxInput().__class__.__name__ or
            widget_name == CheckboxSelectMultiple().__class__.__name__ or
            widget_name == RadioSelect().__class__.__name__)


# TODO: remove, replace with widget
@register.filter(name='is_checkbox')
def is_checkbox(field):
    widget_name = field.field.widget.__class__.__name__
    return (widget_name == CheckboxInput().__class__.__name__ or
            widget_name == CheckboxSelectMultiple().__class__.__name__)


# TODO: remove, replace with widget
@register.filter(name='is_multiple_choice')
def is_multiple_choice(field):
    widget_name = field.field.widget.__class__.__name__
    return (widget_name == CheckboxInput().__class__.__name__ or
            widget_name == CheckboxSelectMultiple().__class__.__name__ or
            widget_name == RadioSelect().__class__.__name__)


# TODO: remove, replace with widget
@register.filter(name='is_textarea')
def is_textarea(field):
    widget_name = field.field.widget.__class__.__name__
    return (widget_name == Textarea().__class__.__name__)


# TODO: remove, replace with widget
@register.filter(name='get_field_type', is_safe=True)
def get_field_type(field):
    widget_name = field.field.widget.__class__.__name__
    if (widget_name == CheckboxInput().__class__.__name__ or
            widget_name == CheckboxSelectMultiple().__class__.__name__):
        return "checkbox"
    elif widget_name == RadioSelect().__class__.__name__:
        return "radio"
    else:
        return ""


