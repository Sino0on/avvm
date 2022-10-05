from django.contrib import admin
from django import forms

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Events
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm


class PageAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = OtherPage
        fields = '__all__'


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm


admin.site.register(Events, EventAdmin)
admin.site.register(EventCategory)
admin.site.register(User)
admin.site.register(OtherPage, PageAdmin)
admin.site.register(Mention)
admin.site.register(News, NewsAdmin)
admin.site.register(NewsImage)
admin.site.register(Article)
admin.site.register(ArticleFile)
admin.site.register(Partner)

