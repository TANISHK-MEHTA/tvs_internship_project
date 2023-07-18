# Generated by Django 4.2.1 on 2023-05-30 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excelbase', '0003_alter_testcases_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseInstance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='testcases',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='excelbase.testcaseinstance'),
        ),
    ]
