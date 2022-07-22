



$( document ).ready(function() {




  document.querySelector("#verify_email_btn").addEventListener("click",function(){
      alert('verify code sent your email!', 'success')
      const email = document.querySelector('input[name="email_input"]');
     document.getElementById("verify_email_input").style.display="none";
     document.getElementById("verify_email_btn").style.display="none";
     document.getElementById("verify_pass_input").style.display="block";
     document.getElementById("verify_pass_btn").style.display="block";

      $.ajax({

                  type: "POST",
                  url: "/login/verify",
                  data: JSON.stringify(email.value),
                  contentType: "application/json",
                  dataType: 'json'
       });

  });


const alertPlaceholder = document.getElementById('liveAlertPlaceholder');
const alert = (message, type) => {
  const wrapper = document.createElement('div');
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('');

  alertPlaceholder.append(wrapper);
}


 document.querySelector("#verify_pass_btn").addEventListener("click",function(){
     const pass = document.querySelector('input[name="pass_input"]');
       $.ajax({
                  type: "POST",
                  url: "/pass/verify",
                  data: JSON.stringify(pass.value),
                  contentType: "application/json",
                  dataType: 'json'

       });
       alert('email verified', 'success');
       display_email();

  });

function display_email(){
   document.getElementById("verify_email_input").style.display="block";
     document.getElementById("verify_email_btn").style.display="block";
     document.getElementById("verify_pass_input").style.display="none";
     document.getElementById("verify_pass_btn").style.display="none";
}

document.querySelector(".open-button").addEventListener("click",function(){
 document.getElementById("myForm").style.display = "block";
 document.getElementById("verify_pass_input").style.display="none";
  document.getElementById("verify_pass_btn").style.display="none";
});


document.querySelector(".cancel").addEventListener("click",function(){
document.getElementById("myForm").style.display = "none";
document.getElementById("verify_pass_input").style.display="none";
  document.getElementById("verify_pass_btn").style.display="none";
});



});
