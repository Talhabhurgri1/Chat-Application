// Sign Form Validation
var validator;
var form = $(".signup")
validator = form.validate({
    rules : {
        username : {
            required : true, 
            minlength : 6,
        },
        email : {
            required : true,
            email : true, 
        },
        password1 : {
            required : true,
            minlength : 7,
        },
        password2 : {
            required : true, 
            minlength : 7,
            equalTo : "#password1",
        }

    },
    messages : {
        username : {
            required : "Please enter your username",
            minlength : "username should be of atleast 6 characters",
        }, 
        email : {
            required : "Please enter your email address",
            email : "Your email address is not valid",
        },
        password1 : {
            required : "Please enter your password",
            minlength : "Password should be of atleast 6 in length."
        },
        password2 : {
            required : "Please enter your password",
            equalTo : "Password and Confirm Password must be same"
        }
    },
    
});


$("#signup").on('click',function(){

    form.submit(function(e){

        e.preventDefault();
        console.log('is_form_valid', form.valid())
        var username = $("#inputName").val()
        var email = $("#inputEmail").val()
        var password1 = $("#password1").val()
        var password2 = $("#password2").val()
        var mydata = {'username': username, 'email' : email, 'password1' : password1, 'password2' : password2}
        console.log(mydata)
        if (form.valid()){
                $.ajax(
                    {
                        method : "POST",
                        url : "/signup/",
                        headers: { "X-CSRFToken": getCookie("csrftoken") },
                        data : {
                            "data": mydata,
                            "csrfmiddlewaretoken": token,
                        },
                        success : function(data){
                            console.log("success")
                        }        
                    }
                )
        }  
    });
    
})