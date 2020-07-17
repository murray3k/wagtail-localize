# Generated by Django 3.0.6 on 2020-07-17 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('wagtail_localize', '0006_delete_language_model'),
        ('wagtail_localize_translation', '0010_rename_segment_to_string'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SegmentTranslation',
            new_name='StringTranslation',
        ),
        migrations.AlterField(
            model_name='stringtranslation',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='string_translations', to='wagtail_localize.Locale'),
        ),
        migrations.RenameField(
            model_name='stringtranslation',
            old_name='text',
            new_name='data',
        ),
    ]