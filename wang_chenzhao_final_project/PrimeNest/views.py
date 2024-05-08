from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    Agency,
    Tenant,
    Apartment,
    Application,
    Availability,
    Period,
    Rating,
    Review
)
from PrimeNest.forms import (AgencyForm,
                             ApartmentForm,
                             TenantForm,
                             ApplicationForm,
                             AvailabilityForm,
                             PeriodForm,
                             RatingForm,
                             ReviewForm)
from .utils import PageLinksMixin


class AgencyList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Agency
    permission_required = 'PrimeNest.view_agency'


class AgencyDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Agency
    permission_required = 'PrimeNest.view_agency'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agency = self.get_object()
        context['apartments'] = agency.apartments.all()
        return context


class AgencyCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AgencyForm
    model = Agency
    permission_required = 'PrimeNest.add_agency'


class AgencyUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AgencyForm
    model = Agency
    template_name = 'PrimeNest/agency_form_update.html'
    permission_required = 'PrimeNest.change_agency'


class AgencyDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Agency
    success_url = reverse_lazy('primenest_agency_list_urlpattern')
    permission_required = 'PrimeNest.delete_agency'

    def get(self, request, *args, **kwargs):
        agency = get_object_or_404(Agency, pk=kwargs['pk'])
        apartments = agency.apartments.all()
        if apartments.count() > 0:
            return render(
                request,
                'PrimeNest/agency_refuse_delete.html',
                {'agency': agency, 'apartments': apartments}
            )
        else:
            return render(
                request,
                'PrimeNest/agency_confirm_delete.html',
                {'agency': agency}
            )


class TenantList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Tenant
    permission_required = 'PrimeNest.view_tenant'


class TenantDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Tenant
    permission_required = 'PrimeNest.view_tenant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tenant = self.get_object()
        context['applications'] = tenant.applications.all()
        context['reviews'] = tenant.reviews.all()
        context['ratings'] = tenant.ratings.all()
        return context


class TenantCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TenantForm
    model = Tenant
    permission_required = 'PrimeNest.add_tenant'


class TenantUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TenantForm
    model = Tenant
    template_name = 'PrimeNest/tenant_form_update.html'
    permission_required = 'PrimeNest.change_tenant'


class TenantDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Tenant
    success_url = reverse_lazy('primenest_tenant_list_urlpattern')
    permission_required = 'PrimeNest.delete_tenant'

    def get(self, request, *args, **kwargs):
        tenant = get_object_or_404(Tenant, pk=kwargs['pk'])
        applications = tenant.applications.all()
        if applications.count() > 0:
            return render(
                request,
                'PrimeNest/tenant_refuse_delete.html',
                {'tenant': tenant, 'applications': applications}
            )
        else:
            return render(
                request,
                'PrimeNest/tenant_confirm_delete.html',
                {'tenant': tenant}
            )


class ApartmentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Apartment
    permission_required = 'PrimeNest.view_apartment'


class ApartmentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Apartment
    permission_required = 'PrimeNest.view_apartment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apartment = self.get_object()
        context['availabilities'] = apartment.availabilities.all()
        context['reviews'] = apartment.reviews.all()
        context['ratings'] = apartment.ratings.all()
        return context


class ApartmentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ApartmentForm
    model = Apartment
    permission_required = 'PrimeNest.add_apartment'


class ApartmentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ApartmentForm
    model = Apartment
    template_name = 'PrimeNest/apartment_form_update.html'
    permission_required = 'PrimeNest.change_apartment'


class ApartmentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Apartment
    success_url = reverse_lazy('primenest_apartment_list_urlpattern')
    permission_required = 'PrimeNest.delete_apartment'

    def get(self, request, *args, **kwargs):
        apartment = get_object_or_404(Apartment, pk=kwargs['pk'])
        availabilities = apartment.availabilities.all()
        reviews = apartment.reviews.all()
        ratings = apartment.ratings.all()
        if availabilities.count() > 0 or reviews.count() > 0 or ratings.count() > 0:
            return render(
                request,
                'PrimeNest/apartment_refuse_delete.html',
                {'apartment': apartment, 'availabilities': availabilities, 'reviews': reviews, 'ratings': ratings}
            )
        else:
            return render(
                request,
                'PrimeNest/apartment_confirm_delete.html',
                {'apartment': apartment}
            )


class ApplicationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Application
    permission_required = 'PrimeNest.view_application'


class ApplicationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Application
    permission_required = 'PrimeNest.view_application'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = self.get_object()
        context['tenant'] = application.tenant
        context['availability'] = application.availability
        return context


class ApplicationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ApplicationForm
    model = Application
    permission_required = 'PrimeNest.add_application'


class ApplicationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ApplicationForm
    model = Application
    template_name = 'PrimeNest/application_form_update.html'
    permission_required = 'PrimeNest.change_application'


class ApplicationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('primenest_application_list_urlpattern')
    permission_required = 'PrimeNest.delete_application'

    def get(self, request, *args, **kwargs):
        application = get_object_or_404(Application, pk=kwargs['pk'])
        return render(
            request,
            'PrimeNest/application_confirm_delete.html',
            {'application': application}
        )


class AvailabilityList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Availability
    permission_required = 'PrimeNest.view_availability'


class AvailabilityDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Availability
    permission_required = 'PrimeNest.view_availability'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        availability = self.get_object()
        context['applications'] = availability.applications.all()
        return context


class AvailabilityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AvailabilityForm
    model = Availability
    permission_required = 'PrimeNest.add_availability'


class AvailabilityUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AvailabilityForm
    model = Availability
    template_name = 'PrimeNest/availability_form_update.html'
    permission_required = 'PrimeNest.change_availability'


class AvailabilityDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Availability
    success_url = reverse_lazy('primenest_availability_list_urlpattern')
    permission_required = 'PrimeNest.delete_availability'

    def get(self, request, *args, **kwargs):
        availability = get_object_or_404(Availability, pk=kwargs['pk'])
        applications = availability.applications.all()
        if applications.count() > 0:
            return render(
                request,
                'PrimeNest/availability_refuse_delete.html',
                {'availability': availability, 'applications': applications}
            )
        else:
            return render(
                request,
                'PrimeNest/availability_confirm_delete.html',
                {'availability': availability}
            )


class PeriodList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Period
    permission_required = 'PrimeNest.view_period'


class PeriodDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Period
    permission_required = 'PrimeNest.view_period'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        period = self.get_object()
        context['availabilities'] = period.availabilities.all()
        return context


class PeriodCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PeriodForm
    model = Period
    permission_required = 'PrimeNest.add_period'


class PeriodUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PeriodForm
    model = Period
    template_name = 'PrimeNest/period_form_update.html'
    permission_required = 'PrimeNest.change_period'


class PeriodDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Period
    success_url = reverse_lazy('primenest_period_list_urlpattern')
    permission_required = 'PrimeNest.delete_period'

    def get(self, request, *args, **kwargs):
        period = get_object_or_404(Period, pk=kwargs['pk'])
        availabilities = period.availabilities.all()
        if availabilities.count() > 0:
            return render(
                request,
                'PrimeNest/period_refuse_delete.html',
                {'period': period, 'availabilities': availabilities}
            )
        else:
            return render(
                request,
                'PrimeNest/period_confirm_delete.html',
                {'period': period}
            )


class RatingList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Rating
    permission_required = 'PrimeNest.view_rating'


class RatingDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Rating
    permission_required = 'PrimeNest.view_rating'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rating = self.get_object()
        context['tenant'] = rating.tenant
        context['apartment'] = rating.apartment
        return context


class RatingCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RatingForm
    model = Rating
    permission_required = 'PrimeNest.add_rating'


class RatingUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RatingForm
    model = Rating
    template_name = 'PrimeNest/rating_form_update.html'
    permission_required = 'PrimeNest.change_rating'


class RatingDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Rating
    success_url = reverse_lazy('primenest_rating_list_urlpattern')
    permission_required = 'PrimeNest.delete_rating'

    def get(self, request, *args, **kwargs):
        rating = get_object_or_404(Rating, pk=kwargs['pk'])
        return render(
            request,
            'PrimeNest/rating_confirm_delete.html',
            {'rating': rating}
        )


class ReviewList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Review
    permission_required = 'PrimeNest.view_review'


class ReviewDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Review
    permission_required = 'PrimeNest.view_review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = self.get_object()
        context['tenant'] = review.tenant
        context['apartment'] = review.apartment
        return context


class ReviewCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ReviewForm
    model = Review
    permission_required = 'PrimeNest.add_review'


class ReviewUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ReviewForm
    model = Review
    template_name = 'PrimeNest/review_form_update.html'
    permission_required = 'PrimeNest.change_review'


class ReviewDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('primenest_review_list_urlpattern')
    permission_required = 'PrimeNest.delete_review'

    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs['pk'])
        return render(
            request,
            'PrimeNest/review_confirm_delete.html',
            {'review': review}
        )
