from django.db import models

class Registration_Details(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    contact = models.IntegerField()
    email = models.EmailField(default=False)
    image = models.ImageField(upload_to="Register_Images")
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    def __str__(self):
        return self.name
class Add_Gym_Center_Details(models.Model):
    id=models.AutoField(primary_key=True)
    center_name=models.CharField(max_length=20)
    address=models.TextField()
    contact=models.IntegerField()
    image=models.ImageField(upload_to="Gym_center_Images")

    def __str__(self):
        return self.center_name

class Add_Trainee_Details(models.Model):
    id=models.AutoField(primary_key=True)
    center=models.ForeignKey(Add_Gym_Center_Details,on_delete=models.CASCADE)
    Trainee_name=models.CharField(max_length=20)
    Trainee_contact=models.IntegerField()
    photo=models.ImageField(upload_to="Trainee_images/")
    Experience=models.IntegerField()
    Trainee_Timings=models.TimeField()

    def __str__(self):
        return self.Trainee_name

class Add_Fee_Deatails(models.Model):
    fee=models.IntegerField()
class Home_Images(models.Model):
    image=models.ImageField(upload_to='home_images')
    def __str__(self):
        return self.image



class Feedback(models.Model):
    name = models.CharField(max_length=20,default=False)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.email
class Contact_Us(models.Model):
    Image=models.ImageField(upload_to="contactUs")
    contact=models.IntegerField(default=False)
    email=models.EmailField(default=False)
    def __str__(self):
        return self.email



