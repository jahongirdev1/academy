from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    courses = models.ManyToManyField('CourseModel', related_name='students', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CourseModel(models.Model):
    title = models.CharField(max_length=255)
    teacher_full_name = models.CharField(max_length=255)
    teacher_image = models.ImageField(upload_to='teachers/', blank=True)
    lessons = models.ManyToManyField('LessonModel', related_name='courses', blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class LessonModel(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title
