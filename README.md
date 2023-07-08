# Advanced_Django

-[Form Submission without reload](#Form)
-[Rest Framework](#RestAPI)

## Form
add ajax code with form (index.html)
```
<script type="text/javascript">
    $(document).on('submit','#post-form',function(e){
        e.preventDefault();
        $.ajax({
            type:'post',
            url:'create/',
            data:{
                name:$('#idname').val(),
                email:$('#idemail').val(),
                bio:$('#idbio').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },
            success:function(message){
                $('h5').html(message);

            }
        });
    });
</script>
```

## RestAPI

What is REST API? ------>
REST is an acronym name of Representational State Transfer, a standardized way to provide data to other applications.It is the best way to transfer data across the applications and can be used by the application. It mandates resources on the web are represented in JSON, HTML, or XML.

An API is an acronym for Application Programming Interface, an interface that defines the interaction between different software components.
REST API allows the front end to communicate with the backend.

What is Django Rest Framework? --------> It provides the most extensive features of Django, Object Relational Mapper (ORM), which allows the interaction of databases in a Pythonic way.

```
pip install django
pip install djangorestframework
```

What are serializers/Deserializers? --------> Serializers are used to represent the model data in JSON format and convert object instances to a more transferable format. It makes the process of parsing data from our API easy. On the other hand, Deserializers convert the JSON data into our model as an object instance.

# CRUD operation in django REST API

models.py
```
class Students(models.Model):  
    name = models.CharField(max_length=200)  
    age=models.IntegerField()
    address = models.CharField(max_length=200)  
    roll_number = models.IntegerField()  
    mobile = models.CharField(max_length=15)  
    date_enrolled=models.DateTimeField( auto_now=True)  
    def __str__(self):  
        return self.name
```
serializer.py
```
from rest_framework import serializers  
from .models import Students  
class StudentSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Students  
        fields = ('__all__')
```
urls.py
```
path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
```
views.py
```
from django.shortcuts import render
from .models import Students  
from .serializers import StudentSerializer  
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404  

class StudentList(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
the post() method, we created the serialized object from the request.data using StudentSeriliazer. The post request sends data to the server enclosed in the request body.
"""

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student=Students.objects.get(pk=pk)
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
Note: The PUT and PATCH methods in HTTP are not the same.The PUT method is used to update an entire resource. When making a PUT request, you typically send the complete representation of the resource in the request payload. This means that if any fields are omitted in the payload, they will be set to their default or empty values.
On the other hand, the PATCH method is used to partially update a resource. With a PATCH request, you only need to send the fields that you want to update in the request payload. The rest of the fields will remain unchanged.









