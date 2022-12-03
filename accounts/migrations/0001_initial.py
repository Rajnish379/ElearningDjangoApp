# Generated by Django 4.0.5 on 2022-10-16 12:23

import accounts.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False, verbose_name='student status')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='teacher status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Unit Name')),
                ('code', models.SlugField(default=accounts.models.string_generator, max_length=10, unique=True, verbose_name='Unit Code')),
                ('semester', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)])),
                ('created_timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'classroom_table',
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Stream Name')),
            ],
            options={
                'db_table': 'stream_table',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='section title')),
                ('created_timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='accounts.classroom')),
            ],
            options={
                'db_table': 'section_break_table',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='resource title')),
                ('text', models.TextField()),
                ('created_timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('file', models.FileField(blank=True, max_length=999, upload_to='files/resources/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='accounts.section')),
            ],
            options={
                'db_table': 'resources_table',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(default=2022, validators=[django.core.validators.MaxValueValidator(2030), django.core.validators.MinValueValidator(2022)])),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='student_class')),
                ('semester', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)])),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='accounts.stream')),
            ],
            options={
                'db_table': 'class_table',
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='section title')),
                ('text', models.TextField()),
                ('created_timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(blank=True, max_length=999, upload_to='files/assignments/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='accounts.section')),
            ],
            options={
                'db_table': 'assignment_table',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teachers', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='accounts.stream')),
            ],
            options={
                'db_table': 'teachers_table',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='students', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('roll_no', models.PositiveIntegerField(verbose_name='Roll No.')),
                ('student_id', models.CharField(max_length=50, unique=True, verbose_name='Student ID')),
                ('classrooms', models.ManyToManyField(blank=True, related_name='students', to='accounts.classroom')),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='accounts.class', verbose_name='Class')),
            ],
            options={
                'db_table': 'student_table',
                'unique_together': {('roll_no', 'current_class')},
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='accounts.teacher'),
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=999, upload_to='files/submissions/')),
                ('submission_timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_submissions', to='accounts.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_submissions', to='accounts.student', verbose_name='student submited')),
            ],
            options={
                'db_table': 'submission_table',
                'unique_together': {('student', 'assignment')},
            },
        ),
    ]