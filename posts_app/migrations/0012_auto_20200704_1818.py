# Generated by Django 3.0.6 on 2020-07-04 22:18

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_app', '0011_auto_20200612_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='application_questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, default=list, size=None),
        ),
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, default=''), blank=True, default=list, size=None)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_app.PostModel')),
            ],
        ),
    ]