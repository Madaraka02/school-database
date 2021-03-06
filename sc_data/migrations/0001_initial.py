# Generated by Django 3.2 on 2021-08-01 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_type', models.CharField(choices=[('W', 'Wall-mounted'), ('M', 'Mobile whiteboard'), ('G', 'Glassboard'), ('C', 'Chalkboard')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_type', models.CharField(choices=[('N', 'Network'), ('W', 'Web design'), ('S', 'Software development')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('rank', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_description', models.TextField()),
                ('unit_credits', models.CharField(max_length=1000)),
                ('prerequisites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.prerequisites')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THUR', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], max_length=1000)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.schedule')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.building')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('P', 'Projector'), ('M', 'Microphone'), ('O', 'Online media stream'), ('T', 'Tv'), ('R', 'Printer')], max_length=1000)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('memory_size', models.CharField(max_length=1000)),
                ('processor_speed', models.CharField(max_length=1000)),
                ('computer_type', models.CharField(choices=[('A', 'Apple'), ('W', 'Windows PC'), ('L', 'Linux PC'), ('T', 'Tablet')], max_length=100)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.lab')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_limit', models.IntegerField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.schedule')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.teacher')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_data.unit')),
            ],
        ),
    ]
