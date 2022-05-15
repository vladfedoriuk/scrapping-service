# Generated by Django 4.0.4 on 2022-05-15 14:25

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Integration",
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
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from="title",
                        verbose_name="slug",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "hook_url",
                    models.URLField(
                        help_text="This url will be used to post scrapped data.",
                        verbose_name="resource url",
                    ),
                ),
            ],
            options={
                "ordering": ("status", "-activate_date"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="IntegrationConsumption",
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
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "integration",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data_consumptions",
                        related_query_name="data_consumption",
                        to="scrapper.integration",
                        verbose_name="integration",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Resource",
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
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from="title",
                        verbose_name="slug",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="This url will be used to start scrapping process.",
                        verbose_name="resource url",
                    ),
                ),
                (
                    "priority",
                    models.SmallIntegerField(
                        choices=[(0, "Low"), (1, "Moderate"), (2, "High")],
                        default=0,
                        help_text="The priorities define the order in which the resources will be getting scrapped.",
                        verbose_name="resource priority",
                    ),
                ),
            ],
            options={
                "ordering": ("status", "-activate_date"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Topic",
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
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from="title",
                        verbose_name="slug",
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ScrappedData",
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
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict,
                        help_text="The scrapped data.",
                        verbose_name="data",
                    ),
                ),
                (
                    "consumers",
                    models.ManyToManyField(
                        help_text="The integrations which have already consumed this data.",
                        related_name="consumed_data",
                        through="scrapper.IntegrationConsumption",
                        to="scrapper.integration",
                        verbose_name="consumers",
                    ),
                ),
                (
                    "resource",
                    models.ForeignKey(
                        help_text="The related resource.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="scrapped_data",
                        to="scrapper.resource",
                        verbose_name="resource",
                    ),
                ),
            ],
            options={
                "verbose_name": "Scrapped Data",
                "verbose_name_plural": "Scrapped Data",
            },
        ),
        migrations.AddField(
            model_name="resource",
            name="topic",
            field=models.ForeignKey(
                help_text="The related topic.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resources",
                related_query_name="resource",
                to="scrapper.topic",
                verbose_name="topic",
            ),
        ),
        migrations.AddField(
            model_name="integrationconsumption",
            name="scrapped_data",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="integration_consumptions",
                related_query_name="integration_consumption",
                to="scrapper.scrappeddata",
                verbose_name="scrapped data",
            ),
        ),
        migrations.AddField(
            model_name="integration",
            name="topic",
            field=models.ForeignKey(
                help_text="The related topic.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="integrations",
                related_query_name="integration",
                to="scrapper.topic",
                verbose_name="topic",
            ),
        ),
    ]
