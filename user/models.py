from django.db import models

# Create your models here.



#Courses for the students

class Course(models.Model):
    course =models.CharField(max_length=30)






    def __str__(self):
        return self.course










#Teacher Details
class Teacherdetails(models.Model):
    LastName =models.CharField(max_length=20)
    FirstName =models.CharField(max_length=20)
    DOB =models.DateField()
    Email =models.EmailField()
    Salary =models.DecimalField(default=0, decimal_places=2,max_digits =7)

    
    


    
    def __str__(self):
        return f'{self.LastName}  {self.FirstName}  '
    


    class Meta:
        verbose_name_plural ='Teachers Information'
    




#Students Details
class Studentdetails(models.Model):
    FirstName =models.CharField(max_length=20)
    
    LastName =models.CharField(max_length=20)
    Age =models.IntegerField(default=1)
    
    DOB =models.CharField(max_length=30)
    Email =models.EmailField()
    

    PhoneNumber =models.CharField(max_length=12)


    Course =models.ForeignKey(Course,on_delete=models.CASCADE)
    ParentName=models.CharField(max_length=20)

    Address =models.CharField(max_length=70)
    image =models.ImageField(upload_to='images/',null=True)
    

    


    def __str__(self):
        return f'{self.LastName}    {self.FirstName}'
    

    class Meta:
        verbose_name_plural ='Students Information'
        
