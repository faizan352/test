# Generated by Django 2.1.7 on 2020-01-09 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CommentTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('parent_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Class')),
            ],
        ),
        migrations.CreateModel(
            name='TaskDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('due_date', models.DateTimeField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('priority', models.TextField(max_length=20)),
                ('assign_to', models.CharField(max_length=30)),
                ('created_by', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='taskdetails',
            name='Users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Users'),
        ),
        migrations.AddField(
            model_name='commenttask',
            name='TaskDetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.TaskDetails'),
        ),
        migrations.AddField(
            model_name='commenttask',
            name='Users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Users'),
        ),
    ]
