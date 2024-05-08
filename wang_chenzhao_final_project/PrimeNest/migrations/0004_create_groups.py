from django.db import migrations

GROUPS = [
    {'name': 'ci_user'},
    {'name': 'ci_agency'},
    {'name': 'ci_viewer'},
]


def add_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_model_class.objects.create(name=group['name'])


def remove_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.get(name=group['name'])
        group_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeNest', '0003_remove_application_apartment_and_more'),
    ]

    operations = [
        migrations.RunPython(
            add_group_data,
            remove_group_data
        )
    ]
