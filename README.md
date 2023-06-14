# Advanced_Django

-[Form Submission without reload](#Form)

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
