from django.contrib import admin
from django import forms
from main.models.company import Company
from main.models.district import District


class CompanyForm(forms.ModelForm):
    model=Company
    fields='__all__'

    def __init__(self, *args, **kwargs):
        super(CompanyForm,self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.filter(city_id=self.instance.city.id)

class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    list_display=['name', 'enterprise_name', 'district_name', 'created']

    def enterprise_name(self, obj):
         return obj.enterprise.name

    def district_name(self, obj):
        if obj.district is None:
            return '----'
        return obj.district.name
