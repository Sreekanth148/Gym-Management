from django.contrib import admin
from .models import Add_Gym_Center_Details,Add_Fee_Deatails,Add_Trainee_Details,Home_Images,Feedback,Contact_Us,Registration_Details
class gym_center_details(admin.ModelAdmin):
    list_display = ("center_name","address","contact","image")
    class Meta:
        model=Add_Gym_Center_Details



admin.site.register(Add_Gym_Center_Details,gym_center_details)
class trainee_details(admin.ModelAdmin):
    list_display = ("center","Trainee_name","Trainee_contact","photo","Experience","Trainee_Timings")
    class Meta:
        model=Add_Trainee_Details
class feedback(admin.ModelAdmin):
    list_display = ("name","email","message")
    class Meta:
        model =Feedback
class Contact (admin.ModelAdmin):
    list_display = ("Image","contact","email")
    class Meta:
        model =Contact_Us

class user(admin.ModelAdmin):
    list_display = ("name","contact","email","image")
    class Meta:
        model = Registration_Details

admin.site.register(Add_Trainee_Details,trainee_details)
admin.site.register(Add_Fee_Deatails)
admin.site.register(Home_Images)
admin.site.register(Feedback,feedback)
admin.site.register(Contact_Us,Contact)
admin.site.register(Registration_Details,user)
