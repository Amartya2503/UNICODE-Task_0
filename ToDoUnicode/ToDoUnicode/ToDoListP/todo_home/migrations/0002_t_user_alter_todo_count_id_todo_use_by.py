# Generated by Django 4.1 on 2022-10-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_user',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='count_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='todo',
            name='use_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_home.t_user'),
        ),
    ]