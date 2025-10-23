from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('method', models.CharField(choices=[('cash','Cash'),('transfer','Bank transfer')], max_length=20)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=models.deletion.SET_NULL, related_name='payments', to='courses.course')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=models.deletion.SET_NULL, related_name='payments', to='courses.lesson')),
                ('user', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='payments', to='users.user')),
            ],
        ),
    ]
