# Generated by Django 4.2.1 on 2023-07-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_like_count_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(choices=[(True, '공개'), (False, '비공개')], default=True),
        ),
    ]
