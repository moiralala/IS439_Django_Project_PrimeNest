from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Agency(models.Model):
    agency_id = models.AutoField(primary_key=True)
    agency_name = models.CharField(max_length=255)
    disambiguator = models.CharField(max_length=255, blank=True, default='')
    contact = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        # result = ''
        if self.disambiguator == '':
            result = '%s' % self.agency_name
        else:
            result = '%s (%s)' % (self.agency_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('primenest_agency_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('primenest_agency_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('primenest_agency_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = _("Agency")
        verbose_name_plural = _("Agencies")
        ordering = ['agency_name', 'disambiguator']
        constraints = [
            models.UniqueConstraint(fields=['agency_name', 'disambiguator'], name='unique_agency')
        ]


class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    disambiguator = models.CharField(max_length=255, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        # result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('primenest_tenant_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('primenest_tenant_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('primenest_tenant_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")
        ordering = ['last_name', 'first_name']
        constraints = [
            models.UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'], name='unique_tenant')
        ]


class Apartment(models.Model):
    apt_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, blank=True)
    bedroom = models.IntegerField(blank=True, null=True)
    bathroom = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True)
    is_studio = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    agency = models.ForeignKey(Agency, related_name='apartments', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s(%s bad %s bath)' % (self.agency, self.address, self.bedroom, self.bathroom)

    def get_absolute_url(self):
        return reverse('primenest_apartment_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('primenest_apartment_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('primenest_apartment_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = _("Apartment")
        verbose_name_plural = _("Apartments")
        ordering = ['apt_id']


class Period(models.Model):
    period_id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return 'From %s to %s (%s)' % (self.start_date.strftime('%Y-%m-%d %H:%M'),
                                       self.end_date.strftime('%Y-%m-%d %H:%M'),
                                       self.description)

    def get_absolute_url(self):
        return reverse('primenest_period_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('primenest_period_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('primenest_period_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = _("Period")
        verbose_name_plural = _("Periods")
        ordering = ['start_date']


class Availability(models.Model):
    ava_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.ForeignKey(Period, related_name='availabilities', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, related_name='availabilities', on_delete=models.CASCADE)
    is_sold_out = models.BooleanField(default=False)

    def __str__(self):
        sold_out_status = "Sold Out" if self.is_sold_out else "Available"
        return '%s (%s bad %s bath) (%s - $%s) [%s]' % (
            self.apartment.address,
            self.apartment.bedroom,
            self.apartment.bathroom,
            self.period.description,
            int(self.price),
            sold_out_status
        )

    def get_absolute_url(self):
        return reverse('primenest_availability_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('primenest_availability_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('primenest_availability_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = _("Availability")
        verbose_name_plural = _("Availabilities")
        ordering = ['price']


class Application(models.Model):
    app_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)
    availability = models.ForeignKey('Availability', related_name='applications', on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, related_name='applications', on_delete=models.CASCADE)

    def __str__(self):
        if self.tenant.disambiguator == '':
            return '%s, %s - %s (%s bad %s bath) (%s - $%s)' % (
                self.tenant.last_name,
                self.tenant.first_name,
                self.availability.apartment.address,
                self.availability.apartment.bedroom,
                self.availability.apartment.bathroom,
                self.availability.period.description,
                int(self.availability.price)
            )
        else:
            return '%s, %s (%s) - %s (%s bad %s bath) (%s - $%s)' % (
                self.tenant.last_name,
                self.tenant.first_name,
                self.tenant.disambiguator,
                self.availability.apartment.address,
                self.availability.apartment.bedroom,
                self.availability.apartment.bathroom,
                self.availability.period.description,
                int(self.availability.price)
            )

    def get_absolute_url(self):
        return reverse('primenest_application_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('primenest_application_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('primenest_application_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")
        ordering = ['app_id']


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    tenant = models.ForeignKey(Tenant, related_name='ratings', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, related_name='ratings', on_delete=models.CASCADE)

    def __str__(self):
        return 'Rating: %s - %s (by %s)' % (self.score, self.apartment.address, self.tenant.first_name)

    def get_absolute_url(self):
        return reverse('primenest_rating_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('primenest_rating_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('primenest_rating_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")
        ordering = ['score']


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    content = models.TextField()
    tenant = models.ForeignKey(Tenant, related_name='reviews', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return 'Review: %s (by %s)' % (self.apartment.address, self.tenant.first_name)

    def get_absolute_url(self):
        return reverse('primenest_review_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('primenest_review_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('primenest_review_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ['review_id']
