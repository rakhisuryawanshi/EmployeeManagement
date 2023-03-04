# Generated by Django 4.1.5 on 2023-02-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmployeeManagement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("First_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("EmailId", models.CharField(max_length=40)),
                ("Mobile", models.IntegerField()),
                ("Address", models.CharField(max_length=30)),
                ("Blood_Group", models.CharField(max_length=30)),
            ],
        ),
    ]