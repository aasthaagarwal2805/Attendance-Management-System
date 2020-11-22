from __future__ import unicode_literals

from django.db import models


# Create your models here.




class teacher_user(models.Model):
	first_name= models.CharField(max_length=100, null=True)
	last_name= models.CharField(max_length=100, null=True)
	personal_email=models.CharField(max_length=100, null=True)
	official_mail=models.CharField(max_length=100, null=True)
	phone_num=models.CharField(max_length=100, null=True)
	aadhar_num=models.CharField(max_length=100, null=True)
	father_name=models.CharField(max_length=100, null=True)
	father_official_mail=models.CharField(max_length=100, null=True)
	mother_name=models.CharField(max_length=100, null=True)
	mother_official_mail=models.CharField(max_length=100, null=True)
	sibling_name=models.CharField(max_length=100, null=True)
	sibling_mail=models.CharField(max_length=100, null=True)
	sibling_num=models.CharField(max_length=100,null=True)
	address=models.CharField(max_length=500, null=True)
	date_created=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.first_name



class student_user(models.Model):
	university_roll_num=models.CharField(max_length=20, null=True)
	first_name= models.CharField(max_length=100, null=True)
	last_name= models.CharField(max_length=100, null=True)
	personal_email=models.CharField(max_length=100, null=True)
	official_mail=models.CharField(max_length=100, null=True)
	phone_num=models.CharField(max_length=100, null=True)
	aadhar_num=models.CharField(max_length=100, null=True)
	father_name=models.CharField(max_length=100, null=True)
	father_official_mail=models.CharField(max_length=100, null=True)
	mother_name=models.CharField(max_length=100, null=True)
	mother_official_mail=models.CharField(max_length=100, null=True)
	sibling_name=models.CharField(max_length=100, null=True)
	sibling_mail=models.CharField(max_length=100, null=True)
	sibling_num=models.CharField(max_length=100,null=True)
	date_created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name



class communication_student(models.Model):
	present_add=models.CharField(max_length=100, null=True)
	pemanent_add=models.CharField(max_length=100, null=True)
	guardian_name=models.CharField(max_length=100, null=True)
	guardian_contact=models.CharField(max_length=100, null=True)
	relation_with_local_guardian=models.CharField(max_length=100, null=True)
	date_created=models.DateTimeField(auto_now_add=True)

	emergency_contact_person_num=models.CharField(max_length=100, null=True)



class leave(models.Model):

	STATUS=(
		('Pending','Pending'),
		('Rejected' , 'Rejected'),
		('Accepted', 'Accepted'),
		)

	MODE=(
		('half', 'half'),
		('full', 'full'),
		)



	first_name=models.CharField(max_length=100, null=True)
	last_name=models.CharField(max_length=100, null=True)
	subject=models.CharField(max_length=100, null=True)
	mode=models.CharField(max_length=100, null=True, choices=MODE)
	date_created=models.DateTimeField(auto_now_add=True)
	status=models.CharField(max_length=100, null=True, choices=STATUS)


class Faculty(models.Model):
    faculty_id = models.CharField(max_length=10,default="")
    name = models.CharField(max_length=32,default="")
    def __unicode__(self):
        return self.name

class Subject(models.Model):
    subject_id = models.CharField(max_length=10,default="")
    subject_name = models.CharField(max_length=32,default="")
    # faculty = models.ForeignKey(Faculty, on_delete=models.SET_DEFAULT)
    def __unicode__(self):
        return self.subject_name


# class DailyTimeTable(models.Model):
#     period1 = models.OneToOneField(Subject,related_name='period1', on_delete=models.SET_NULL)
#     period2 = models.OneToOneField(Subject,related_name='period2', on_delete=models.SET_NULL)
#     period3 = models.OneToOneField(Subject,related_name='period3', on_delete=models.SET_NULL)
#     period4 = models.OneToOneField(Subject,related_name='period4', on_delete=models.SET_NULL)
#     period5 = models.OneToOneField(Subject,related_name='period5', on_delete=models.SET_NULL)
#     period6 = models.OneToOneField(Subject,related_name='period6', on_delete=models.SET_NULL)
#     period7 = models.OneToOneField(Subject,related_name='period7', on_delete=models.SET_NULL)


# class WeeklyTimeTable(models.Model):
#     monday = models.OneToOneField(DailyTimeTable,related_name='monday', on_delete=models.SET_NULL)
#     tuesday = models.OneToOneField(DailyTimeTable,related_name='tuesday', on_delete=models.SET_NULL)
#     wednesday = models.OneToOneField(DailyTimeTable,related_name='wednesday', on_delete=models.SET_NULL)
#     thursday = models.OneToOneField(DailyTimeTable,related_name='thursday', on_delete=models.SET_NULL)
#     friday = models.OneToOneField(DailyTimeTable,related_name='friday', on_delete=models.SET_NULL)


class Class(models.Model):
    branch = models.CharField(max_length=5,default="")
    section = models.CharField(max_length=1,default="")
    year = models.IntegerField(default=1)
    no_of_students = models.IntegerField(default=60)
    # time_table = models.OneToOneField(WeeklyTimeTable, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.branch+" "+self.year+self.section


class SubjectAttendenceTable(models.Model):
    # subject = models.OneToOneField(Subject, on_delete=models.SET_NULL)
    attendence_count = models.IntegerField(default=0)

# class StudentAttendenceTable(models.Model):
#     subject1 = models.OneToOneField(SubjectAttendenceTable,related_name='subject1', on_delete=models.SET_NULL)
#     subject2 = models.OneToOneField(SubjectAttendenceTable,related_name='subject2', on_delete=models.SET_NULL)
#     subject3 = models.OneToOneField(SubjectAttendenceTable,related_name='subject3', on_delete=models.SET_NULL)
#     subject4 = models.OneToOneField(SubjectAttendenceTable,related_name='subject4', on_delete=models.SET_NULL)
#     subject5 = models.OneToOneField(SubjectAttendenceTable,related_name='subject5', on_delete=models.SET_NULL)
#     subject6 = models.OneToOneField(SubjectAttendenceTable,related_name='subject6', on_delete=models.SET_NULL)

