# Generated by Django 4.1.1 on 2022-09-07 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="new",
            name="body",
            field=models.TextField(verbose_name="body"),
        ),
        migrations.AlterField(
            model_name="new",
            name="body_en",
            field=models.TextField(null=True, verbose_name="body"),
        ),
        migrations.AlterField(
            model_name="new",
            name="body_uz",
            field=models.TextField(null=True, verbose_name="body"),
        ),
        migrations.AlterField(
            model_name="new",
            name="date",
            field=models.DateField(verbose_name="date"),
        ),
        migrations.AlterField(
            model_name="new",
            name="title",
            field=models.CharField(max_length=150, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="new",
            name="title_en",
            field=models.CharField(max_length=150, null=True, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="new",
            name="title_uz",
            field=models.CharField(max_length=150, null=True, verbose_name="title"),
        ),
    ]
