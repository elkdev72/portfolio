from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=200)
    date_created = models.DateField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('PROG', 'Programming Languages'),
        ('FRAM', 'Frameworks'),
        ('TOOL', 'Tools & Technologies'),
        ('SOFT', 'Soft Skills'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 rating

    def __str__(self):
        return self.name

class PersonalInfo(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)  # e.g., "Full Stack Developer"
    bio = models.TextField()
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    resume = models.FileField(upload_to='documents/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Personal Info"
        