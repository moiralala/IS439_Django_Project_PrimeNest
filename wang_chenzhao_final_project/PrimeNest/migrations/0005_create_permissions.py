from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    # Collect permissions based on the models available in the PrimeNest app
    period_permissions = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                         content_type__model='period')

    agency_permissions = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                         content_type__model='agency')

    tenant_permissions = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                         content_type__model='tenant')

    apartment_permissions = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                            content_type__model='apartment')

    application_permissions = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                              content_type__model='application')

    availability_permissions = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                               content_type__model='availability')

    review_permissions = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                         content_type__model='review')

    rating_permissions = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                         content_type__model='rating')

    # Collect only view permissions for each model
    perm_view_period = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                       content_type__model='period',
                                                       codename='view_period')

    perm_view_agency = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                       content_type__model='agency',
                                                       codename='view_agency')

    perm_view_tenant = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                       content_type__model='tenant',
                                                       codename='view_tenant')

    perm_view_apartment = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                          content_type__model='apartment',
                                                          codename='view_apartment')

    perm_view_application = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                            content_type__model='application',
                                                            codename='view_application')

    perm_view_availability = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                             content_type__model='availability',
                                                             codename='view_availability')

    perm_view_review = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                       content_type__model='review',
                                                       codename='view_review')

    perm_view_rating = permission_class.objects.filter(content_type__app_label='PrimeNest',
                                                       content_type__model='rating',
                                                       codename='view_rating')

    ci_user_permissions = chain(perm_view_period,
                                perm_view_agency,
                                tenant_permissions,
                                perm_view_apartment,
                                application_permissions,
                                perm_view_availability,
                                review_permissions,
                                rating_permissions)

    ci_agency_permissions = chain(agency_permissions,
                                  perm_view_tenant,
                                  apartment_permissions,
                                  perm_view_application,
                                  availability_permissions,
                                  perm_view_review,
                                  perm_view_rating,
                                  period_permissions)

    ci_viewer_permissions = chain(perm_view_period,
                                  perm_view_agency,
                                  perm_view_tenant,
                                  perm_view_apartment,
                                  perm_view_application,
                                  perm_view_availability,
                                  perm_view_review,
                                  perm_view_rating)

    my_groups_initialization_list = [
        {
            "name": "ci_user",
            "permissions_list": ci_user_permissions,
        },
        {
            "name": "ci_agency",
            "permissions_list": ci_agency_permissions,
        },
        {
            "name": "ci_viewer",
            "permissions_list": ci_viewer_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('PrimeNest', '0004_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
