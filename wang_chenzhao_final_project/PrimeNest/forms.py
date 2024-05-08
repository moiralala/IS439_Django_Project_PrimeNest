from django import forms
from .models import Agency, Tenant, Apartment, Application, Review, Rating, Availability, Period


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'

    def clean_agency_name(self):
        return self.cleaned_data['agency_name'].strip()

    def clean_disambiguator(self):
        return self.cleaned_data['disambiguator'].strip()


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

    def clean_address(self):
        return self.cleaned_data['address'].strip()


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = '__all__'


class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = '__all__'

    def clean_description(self):
        return self.cleaned_data['description'].strip()
