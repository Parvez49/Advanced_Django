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
