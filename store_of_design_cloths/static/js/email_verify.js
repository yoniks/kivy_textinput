



$( document ).ready(function() {

    document.getElementById("verify_pass_input").style.display="none";
  document.getElementById("verify_pass_btn").style.display="none";


  const alertPlaceholder = document.getElementById('liveAlertPlaceholder');
const alert = (message, type) => {
  const wrapper = document.createElement('div');
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" id="btn_close" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('');
 // alertPlaceholder = wrapper;
  alertPlaceholder.append(wrapper);
}







  document.querySelector("#verify_email_btn").addEventListener("click",function(){
       document.querySelector("#verify_email_btn").disabled=true;
      const email = document.querySelector('input[name="email_input"]');

      $.ajax({

                  type: "POST",
                  url: "/login/verify",
                  data: JSON.stringify(email.value),
                  contentType: "application/json",
                  dataType: 'json'
       }).done(function(data){
        if (data.status=="ok"){
             display_password();
             alert('Verify Code Sent To Email!', 'success');
             document.querySelector("#verify_email_btn").disabled=false;
        }else if(data.status=="verified"){
          alert('Email Already Verified! To Input New Email, Please Close the Open Pages ','success');
        }else if(data.status<=0) {
              display_email();
              limit_user();
               document.getElementById("liveAlertPlaceholder_msg_user").innerHTML='To Many Attempts!, Please Clear History And Try Again';

        }else if(data.status=="limit_to_4"){
          limit_user();
           document.getElementById("liveAlertPlaceholder_msg_user").innerHTML='Sorry, Verify Email is Limit four Times A day!';
        }else{
           if (data.status==1){
               alert(data.status + " Last To Type The Email",'success');
               document.querySelector("#verify_email_btn").disabled=false;
           }else{
              alert('Email Is Not Valid', 'success');
              document.querySelector("#verify_email_btn").disabled=false;
           }

        }
       });

  });




//password sending!
 document.querySelector("#verify_pass_btn").addEventListener("click",function(){
     document.querySelector("#verify_pass_btn").disabled=true;
     const pass = document.querySelector('input[name="pass_input"]');

     if(pass.value.length<6){
        alert('Password is not valid','success');
     }else{

       $.ajax({
                  type: "POST",
                  url: "/pass/verify",
                  data: JSON.stringify(pass.value),
                  contentType: "application/json",
                  dataType: 'json'

       }).done(function(data){
         if(data.status=="ok"){
         display_email();
             alert('Email verified','success');
             start =  setTimeout(function(){
                document.getElementById("myForm").style.display = "none";
               clearTimeout(start);
                    },1000);
         }else if(data.status=="verified"){
           alert('Email Already Verified','success');
         }else if(data.status=="fail_to_storage_user"){
           alert('Something Went Wrong  Please Try Again!','success');
               start =  setTimeout(function(){
                display_email();
               clearTimeout(start);
                    },500);
         }else if(data.status<=0){//we block the button from user keeping input wrong password
            display_email();
            limit_user();
            document.getElementById("liveAlertPlaceholder_msg_user").innerHTML='To Many Attempts!, Please Clear History And Try Again';

         }else{
           if (data.status==1){
               alert(data.status+" Last To Type The Code",'success');
               document.querySelector("#verify_pass_btn").disabled=false;
           }else{
              alert('Password is not valid','success');
              document.querySelector("#verify_pass_btn").disabled=false;
           }
         }

       });

}//if pass.length
  });


function limit_user(){
   document.getElementById("myForm").style.display = "none";
   document.getElementById("open-form-verify").style.display = "none";

}

function display_password(){
      document.getElementById("verify_email_input").style.display="none";
      document.getElementById("verify_email_btn").style.display="none";
       document.getElementById("verify_pass_input").style.display="block";
       document.getElementById("verify_pass_btn").style.display="block";
}

function display_email(){



    const pass = document.querySelector('input[name="pass_input"]');
    pass.value='';
    document.getElementById("verify_pass_input").style.display="none";
     document.getElementById("verify_pass_btn").style.display="none";
   document.getElementById("verify_email_input").style.display="block";
     document.getElementById("verify_email_btn").style.display="block";
      document.getElementById("verify_email_btn").innerHTML='Verify Email'
      const email = document.querySelector('input[name="email_input"]');
      email.value='';


}

document.querySelector(".open-form").addEventListener("click",function(){
 document.getElementById("myForm").style.display = "block";

});


document.querySelector(".cancel").addEventListener("click",function(){
 //display_email();
document.getElementById("myForm").style.display = "none";

});



});
