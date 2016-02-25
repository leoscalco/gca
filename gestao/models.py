# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import datetime

# Create your models here.


#  o user

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            name=name,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class Student(AbstractBaseUser):
    name = models.CharField(max_length=100, verbose_name='Nome')
    date_of_birth = models.DateField(verbose_name='Data de nascimento')
    email = models.EmailField(max_length=200, unique=True, verbose_name='E-mail')
    rfid = models.CharField(max_length=100, verbose_name='RFID', default="")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    status = models.IntegerField(default=0) # 0 - cursando 1 - formado 2 - cancelado
    start_date = models.DateTimeField(default=datetime.datetime.now)
    course = models.ForeignKey(Course, default=1)
    img = models.ImageField(upload_to=u'files/student', blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=200)
    img = models.ImageField(upload_to=u'files/teacher', blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name


class Discipline(models.Model):
    name = models.CharField(max_length=100, default='')
    tag = models.CharField(max_length=5, default='')
    is_annual = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name


class Class(models.Model):
    year = models.IntegerField()
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, default=1)
    discipline = models.ForeignKey(Discipline, default=1)

    def __str__(self):
        return self.discipline.name + " " + str(self.year)

    def __unicode__(self):
        return u'%s' % self.discipline.name + " " + str(self.year)


class Test(models.Model):
    description = models.CharField(max_length=150, default="")
    bimester = models.CharField(max_length=50)
    file = models.FileField(upload_to=u'files/tests') # vou mudar
    insertion_date = models.DateTimeField(default=datetime.datetime.now)
    discipline = models.ForeignKey(Discipline, default=1)
    teacher = models.ForeignKey(Teacher, default=1)
    subjects = models.ManyToManyField(Subject)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return  self.discipline.name + " - " + self.teacher.name + " - " + self.bimester + "° Bimestre"

    def __unicode__(self):
        return  self.discipline.name + " - " + self.teacher.name + " - " + self.bimester + "° Bimestre"

class EventType(models.Model):
    name = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class Event(models.Model):
    name = models.CharField(max_length=100, default="")
    date = models.DateTimeField(verbose_name='Data do evento')
    site = models.URLField(default='http://www.google.com')
    file = models.ImageField(upload_to=u'files/events', blank=True)
    type = models.ForeignKey(EventType, default=1)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class NewType(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class New(models.Model):
    body = models.CharField(max_length=4000, default='')
    post_date = models.DateTimeField()
    title = models.CharField(max_length=120, default='')
    validate_date = models.DateTimeField()
    img = models.ImageField(upload_to=u'files/news', blank=True)
    typeN = models.ForeignKey(NewType, default=1)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

class DocumentType(models.Model):
    name = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class Document(models.Model):
    name = models.CharField(max_length=100, default='')
    file = models.FileField(upload_to=u'files/docs', blank=True)
    post_date = models.DateTimeField()
    type = models.ForeignKey(DocumentType, default=1)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class Classified(models.Model):
    name = models.CharField(max_length=100, default='')
    desc = models.CharField(max_length=1000, default='')
    student = models.ForeignKey(Student, default=1)
    img = models.ImageField(upload_to=u'files/classified', blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class ProductSize(models.Model):
    name = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class ProductType(models.Model):
    name = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

class Product(models.Model):
    quantity = models.IntegerField()
    desc = models.CharField(max_length=300)
    type = models.ForeignKey(ProductType, default=1)
    img = models.ImageField(upload_to=u'files/classified', blank=True)
    price = models.FloatField(default=0)
    size = models.ForeignKey(ProductSize, default=1)

    def __str__(self):
        return self.type.name + " " + self.size.name

    def __unicode__(self):
        return self.type.name + " " +  self.size.name
