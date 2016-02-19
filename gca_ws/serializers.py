from django.contrib.gis import serializers

from gestao.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'name', 'email', 'date_of_birth')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'name', 'email')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'date', 'site')

class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discipline
        fields = ('url', 'name', 'is_annual')

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'name')

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    students = UserSerializer(many=True, read_only=True)
    disciplines = DisciplineSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ('url', 'year', 'teachers', 'students', 'disciplines')

class TestSerializer(serializers.HyperlinkedModelSerializer):
    teacher = TeacherSerializer()
    discipline = DisciplineSerializer()
    subjects = SubjectSerializer(many=True, read_only=True)
    download_link = serializers.SerializerMethodField()

    def get_download_link(self, obj):
        aux = "http://localhost:8000/gestao/provas/"+str(obj.id)+"/download"
        return aux

    class Meta:
        model = Test
        fields = ('url', 'name', 'description', 'insertion_date', 'discipline', 'teacher', 'subjects', 'download_link')