from django.contrib import admin
from .models import Project, noticias, post, RichText, Download,Article
from content_editor.admin import ContentEditor, ContentEditorInline
from django import forms
from django.db import models
from django_quill.fields import QuillField

# Register your models here.
admin.site.register(Article),
admin.site.register(Project),
admin.site.register(noticias),
admin.site.register(post),

class QuillPostAdmin(admin.ModelAdmin):
    pass

class RichTextarea(forms.Textarea):
    def __init__(self, attrs=None):
        # Provide class so that the code in plugin_ckeditor.js knows
        # which text areas should be enhanced with a rich text
        # control:
        default_attrs = {"data-type": "ckeditortype"}
        if attrs:
            default_attrs.update(attrs)
        super(RichTextarea, self).__init__(default_attrs)


class RichTextInline(ContentEditorInline):
    model = RichText
    formfield_overrides = {
        models.TextField: {"widget": RichTextarea},
    }

    class Media:
        js = (
            "//cdn.ckeditor.com/4.5.6/standard/ckeditor.js",
            "app/plugin_ckeditor.js",
        )


class ArticleAdmin(ContentEditor):
    inlines = [
        RichTextInline,
        # The create method serves as a shortcut; for quickly
        # creating inlines:
        ContentEditorInline.create(model=Download),
    ]
