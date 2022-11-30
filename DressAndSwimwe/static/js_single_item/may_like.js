



$( document ).ready(function() {





        const img_cards= document.querySelectorAll("#may-like-items").length
          for(let i=0;i<img_cards;i++){

            document.querySelectorAll("#may-like-items")[i].addEventListener("click",function(){
            //disabled=true;
            document.querySelectorAll("#may-like-items").disabled=true;
            const sku = document.querySelectorAll("#Items-Sku-Card")[i].textContent;

               
               ref = $.ajax({
                  type: "POST",
                  url: "/home/products/display/item",
                  data: {sku:sku}
               });
               ref.done(function(data){
                    $('#refresh-single-item').fadeOut(500).fadeIn(500);
                    $('#refresh-single-item').html(data);
                    document.querySelectorAll("#may-like-items").disabled=false;
                     

               });


          });
       }



      

//email
      document.querySelector("#form-submit").addEventListener("click",function(){
           const subscript_email = document.querySelector('input[name="email-subscript"]');
             window.location.reload(); 
             $.ajax({
             type: "POST",
             url: "/home/send/email/to/subscript",
             data: JSON.stringify(subscript_email.value),
             contentType: "application/json",
             dataType: 'json'
           }).done(function(data){
              if(data.received=="sent"){
                  
              }else{
                 
              }        
           });
      });







   });
