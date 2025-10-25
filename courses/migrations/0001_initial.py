from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('title', models.CharField(max_length=255)),('preview', models.ImageField(blank=True, null=True, upload_to='courses/')),('description', models.TextField(blank=True)),('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='users.user')),],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('title', models.CharField(max_length=255)),('description', models.TextField(blank=True)),('preview', models.ImageField(blank=True, null=True, upload_to='lessons/')),('video_url', models.URLField(blank=True)),('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='users.user')),('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course')),],
        ),
    ]
