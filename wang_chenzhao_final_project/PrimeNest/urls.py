from django.urls import path

from PrimeNest.views import (
    AgencyList,
    TenantList,
    ApartmentList,
    ApplicationList,
    AvailabilityList,
    PeriodList,
    RatingList,
    ReviewList,
    AgencyDetail,
    TenantDetail,
    ApartmentDetail,
    ApplicationDetail,
    AvailabilityDetail,
    PeriodDetail,
    RatingDetail,
    ReviewDetail,
    AgencyCreate,
    TenantCreate,
    ApartmentCreate,
    ApplicationCreate,
    AvailabilityCreate,
    PeriodCreate,
    RatingCreate,
    ReviewCreate,
    AgencyUpdate,
    TenantUpdate,
    ApartmentUpdate,
    ApplicationUpdate,
    AvailabilityUpdate,
    PeriodUpdate,
    RatingUpdate,
    ReviewUpdate,
    AgencyDelete,
    TenantDelete,
    ApartmentDelete,
    ApplicationDelete,
    AvailabilityDelete,
    PeriodDelete,
    RatingDelete,
    ReviewDelete
)


urlpatterns = [

    path('agency/',
         AgencyList.as_view(),
         name='primenest_agency_list_urlpattern'),

    path('agency/<int:pk>/',
         AgencyDetail.as_view(),
         name='primenest_agency_detail_urlpattern'),

    path('agency/create/',
         AgencyCreate.as_view(),
         name='primenest_agency_create_urlpattern'),

    path('agency/<int:pk>/update/',
         AgencyUpdate.as_view(),
         name='primenest_agency_update_urlpattern'),

    path('agency/<int:pk>/delete/',
         AgencyDelete.as_view(),
         name='primenest_agency_delete_urlpattern'),

    path('tenant/',
         TenantList.as_view(),
         name='primenest_tenant_list_urlpattern'),

    path('tenant/<int:pk>/',
         TenantDetail.as_view(),
         name='primenest_tenant_detail_urlpattern'),

    path('tenant/create/',
         TenantCreate.as_view(),
         name='primenest_tenant_create_urlpattern'),

    path('tenant/<int:pk>/update/',
         TenantUpdate.as_view(),
         name='primenest_tenant_update_urlpattern'),

    path('tenant/<int:pk>/delete/',
         TenantDelete.as_view(),
         name='primenest_tenant_delete_urlpattern'),

    path('apartment/',
         ApartmentList.as_view(),
         name='primenest_apartment_list_urlpattern'),

    path('apartment/<int:pk>/',
         ApartmentDetail.as_view(),
         name='primenest_apartment_detail_urlpattern'),

    path('apartment/create/',
         ApartmentCreate.as_view(),
         name='primenest_apartment_create_urlpattern'),

    path('apartment/<int:pk>/update/',
         ApartmentUpdate.as_view(),
         name='primenest_apartment_update_urlpattern'),

    path('apartment/<int:pk>/delete/',
         ApartmentDelete.as_view(),
         name='primenest_apartment_delete_urlpattern'),

    path('application/',
         ApplicationList.as_view(),
         name='primenest_application_list_urlpattern'),

    path('application/<int:pk>/',
         ApplicationDetail.as_view(),
         name='primenest_application_detail_urlpattern'),

    path('application/create/',
         ApplicationCreate.as_view(),
         name='primenest_application_create_urlpattern'),

    path('application/<int:pk>/update/',
         ApplicationUpdate.as_view(),
         name='primenest_application_update_urlpattern'),

    path('application/<int:pk>/delete/',
         ApplicationDelete.as_view(),
         name='primenest_application_delete_urlpattern'),

    path('availability/',
         AvailabilityList.as_view(),
         name='primenest_availability_list_urlpattern'),

    path('availability/<int:pk>/',
         AvailabilityDetail.as_view(),
         name='primenest_availability_detail_urlpattern'),

    path('availability/create/',
         AvailabilityCreate.as_view(),
         name='primenest_availability_create_urlpattern'),

    path('availability/<int:pk>/update/',
         AvailabilityUpdate.as_view(),
         name='primenest_availability_update_urlpattern'),

    path('availability/<int:pk>/delete/',
         AvailabilityDelete.as_view(),
         name='primenest_availability_delete_urlpattern'),

    path('period/',
         PeriodList.as_view(),
         name='primenest_period_list_urlpattern'),

    path('period/<int:pk>/',
         PeriodDetail.as_view(),
         name='primenest_period_detail_urlpattern'),

    path('period/create/',
         PeriodCreate.as_view(),
         name='primenest_period_create_urlpattern'),

    path('period/<int:pk>/update/',
         PeriodUpdate.as_view(),
         name='primenest_period_update_urlpattern'),

    path('period/<int:pk>/delete/',
         PeriodDelete.as_view(),
         name='primenest_period_delete_urlpattern'),

    path('review/',
         ReviewList.as_view(),
         name='primenest_review_list_urlpattern'),

    path('review/<int:pk>/',
         ReviewDetail.as_view(),
         name='primenest_review_detail_urlpattern'),

    path('review/create/',
         ReviewCreate.as_view(),
         name='primenest_review_create_urlpattern'),

    path('review/<int:pk>/update/',
         ReviewUpdate.as_view(),
         name='primenest_review_update_urlpattern'),

    path('review/<int:pk>/delete/',
         ReviewDelete.as_view(),
         name='primenest_review_delete_urlpattern'),

    path('rating/',
         RatingList.as_view(),
         name='primenest_rating_list_urlpattern'),

    path('rating/<int:pk>/',
         RatingDetail.as_view(),
         name='primenest_rating_detail_urlpattern'),

    path('rating/create/',
         RatingCreate.as_view(),
         name='primenest_rating_create_urlpattern'),

    path('rating/<int:pk>/update/',
         RatingUpdate.as_view(),
         name='primenest_rating_update_urlpattern'),

    path('rating/<int:pk>/delete/',
         RatingDelete.as_view(),
         name='primenest_rating_delete_urlpattern'),
]
