# Generated by Django 4.0.4 on 2022-04-22 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('published_at', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('authors', models.ManyToManyField(related_name='books', to='library.author')),
            ],
        ),
        migrations.CreateModel(
            name='BookCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='book_covers')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='covers', to='library.book')),
            ],
        ),
    ]
