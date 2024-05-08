from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("PrimeNest", "0002_period_description_alter_tenant_disambiguator"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="application",
            name="apartment",
        ),
        migrations.AddField(
            model_name="application",
            name="availability",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="PrimeNest.availability",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="availability",
            name="is_sold_out",
            field=models.BooleanField(default=False),
        ),
    ]
