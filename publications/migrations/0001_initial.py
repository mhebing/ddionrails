# Generated by Django 2.1.7 on 2019-03-22 11:41

import ddionrails.mixins
from django.db import migrations, models
import django.db.models.deletion
import elastic.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instruments', '0001_initial'),
        ('studies', '0001_initial'),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True)),
                ('url_text', models.TextField(blank=True)),
                ('context_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_attachments', to='studies.Study')),
                ('dataset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='data.Dataset')),
                ('instrument', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='instruments.Instrument')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='instruments.Question')),
                ('study', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='studies.Study')),
                ('variable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='data.Variable')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('sub_type', models.CharField(blank=True, max_length=255)),
                ('title', models.TextField(blank=True)),
                ('author', models.TextField(blank=True)),
                ('year', models.TextField(blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('cite', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('doi', models.TextField(blank=True)),
                ('studies', models.TextField(blank=True)),
                ('study', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='studies.Study')),
            ],
            bases=(elastic.mixins.ModelMixin, ddionrails.mixins.ModelMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='publication',
            unique_together={('study', 'name')},
        ),
    ]
