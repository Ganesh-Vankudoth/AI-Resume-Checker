from django.db import models

# Create your models here.
class Resume(models.Model):
    ROLE_CHOICES=[
        ('python_dev','Python Developer'),
        ('frontend_dev','Frontend Developer'),
        ('data_analyst','Data Analyst')
    ]
    file=models.FileField(upload_to='resumes/')
    job_role=models.CharField(max_length=50,choices=ROLE_CHOICES,default='python_dev')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    extracted_text=models.TextField(blank=True)
    score=models.IntegerField(default=0)
    matched_keywords=models.TextField(blank=True)
    def __str__(self):
        return f"{self.get_job_role_display()} - {self.score}%"
