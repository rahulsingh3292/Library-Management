# Generated by Django 3.2.7 on 2021-09-19 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowedbook',
            old_name='book',
            new_name='books',
        ),
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='BorrowRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]