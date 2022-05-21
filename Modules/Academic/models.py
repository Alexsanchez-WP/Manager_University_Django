from django.db import models

class Careers(models.Model):

    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(default=5)

class Student(models.Model):

    document = models.CharField(max_length=8, primary_key=True)      
    last_name_father = models.CharField(max_length=35)
    last_name_mother = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    birth = models.DateField()  
    sexes = [('F', 'Female'),('M', 'Male')]
    sex = models.CharField(max_length=1, choices=sexes, default='F')
    careers = models.ForeignKey(Careers, null=False, blank=False, on_delete=models.CASCADE)
    vigenci = models.BooleanField(default=True)

    def full_name(self):
        txt = "{0} [1}, {2}"
        return txt.format(self.last_name_father, self.last_name_mother, self.name)

class Course(models.Model):

    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=100)

class Enrollment(models.Model):

    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    Enroll_date = models.DateTimeField(auto_now_add=True)

