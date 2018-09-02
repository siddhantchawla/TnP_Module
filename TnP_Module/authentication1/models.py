from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext


# def upload_image_path(instance, filename):
#     # print(instance)
#     #print(filename)
#     new_filename = random.randint(1,3910209312)
#     name, ext = get_filename_ext(filename)
#     final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
#     return "products/{new_filename}/{final_filename}".format(
#             new_filename=new_filename, 
#             final_filename=final_filename
#             )


class UserProfile(models.Model) : 
	branch_choices = (
		('-','---SELECT---'),
		('CSE','Computer Science & Engineering'),
		('ECE','Electronics and Communication Engineering'),
		('MECH','Mechanical Engineering'),
		('MME','Metallurgy Engineering'),
		('CHE','Chemical Engineering'),
		('CIVIL','Civil Engineering'),
		('EEE','Electrical and Electronics Engineering'),
		('BIO','Biotechnology'),
	)

	course_choices = (
		('BTech','B.Tech'),
		('MTech','M.Tech'),
		('MCA','MCA'),
		('MBA','MBA'),
		('PHD','Phd'),
	)

	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	first = models.CharField(max_length=20, blank = True, null = True)
	last = models.CharField(max_length=20, blank = True, null = True)
	regNum = models.CharField(max_length=10)
	course = models.CharField(max_length=20,choices = course_choices,default='BTech')
	branch = models.CharField(max_length=20,choices = branch_choices)
	contact = models.CharField(max_length=20)
	cgpa = models.DecimalField(decimal_places=2,max_digits=4,default = 0.00)
	profilePic = models.ImageField(upload_to='documents/',null=True,blank=True)
	resume = models.FileField(upload_to='documents/',null=True,blank=True)
	isPlaced = models.BooleanField(default=False) 

	def __str__(self):
		return f'{self.regNum}'