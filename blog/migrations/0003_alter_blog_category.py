# Generated by Django 4.2.6 on 2023-10-24 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.blogcategories'),
        ),
    ]