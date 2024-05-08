from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PrimeNest", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="period",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="tenant",
            name="disambiguator",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
