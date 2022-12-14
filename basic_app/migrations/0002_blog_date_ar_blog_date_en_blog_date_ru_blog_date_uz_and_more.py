# Generated by Django 4.1.3 on 2022-11-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_ar',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='date_en',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='date_ru',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='date_uz',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='des_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='des_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='des_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='des_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_ar',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_en',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_ru',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_uz',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_ar',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_en',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_ru',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_uz',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='message_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='message_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='message_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='message_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name_ar',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name_en',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name_ru',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name_uz',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_ar',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_en',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_ru',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_uz',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='name_ar',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='name_en',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='name_ru',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='name_uz',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='number_ar',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='number_en',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='number_ru',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='number_uz',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition1_ar',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition1_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition1_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition1_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition2_ar',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition2_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition2_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition2_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition3_ar',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition3_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition3_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition3_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition4_ar',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition4_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition4_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition4_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition5_ar',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition5_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition5_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='addition5_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='month_ar',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='month_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='month_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='month_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='name_ar',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='name_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='name_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='name_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='price_ar',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='price_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='price_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='price_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_uz',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='des_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='des_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='des_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='des_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name_ar',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name_en',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name_ru',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name_uz',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='prof_ar',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='prof_en',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='prof_ru',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='prof_uz',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='des_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='des_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='des_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='des_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_ar',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_en',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_ru',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_uz',
            field=models.CharField(max_length=89, null=True),
        ),
    ]
