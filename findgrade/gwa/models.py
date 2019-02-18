from django.db import models

# Create your models here.

class users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name    = models.CharField(max_length=50)

    def __str__(self):
        return "Something"
    
class subject(models.Model):
    subject_id          = models.BigAutoField(primary_key=True)
    subject_name        = models.CharField(max_length=50)
    units               = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return "Something"
    
class grade(models.Model):
    grade_id    = models.BigAutoField(primary_key=True)
    grade       = models.DecimalField(max_digits=3, decimal_places=2)
    subject_id  = models.ForeignKey(subject, on_delete=models.CASCADE)
    user_id     = models.ForeignKey(users, on_delete=models.CASCADE)
    

    def __str__(self):
        return "self."
    


    

