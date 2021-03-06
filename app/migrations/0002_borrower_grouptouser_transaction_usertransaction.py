# Generated by Django 2.0.6 on 2018-06-09 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_to_repay', models.FloatField(default=0)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Expense')),
            ],
        ),
        migrations.CreateModel(
            name='GroupToUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_date', models.CharField(max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Group')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Transaction')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]
