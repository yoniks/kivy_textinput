



$( document ).ready(function() {





        const img_cards= document.querySelectorAll("#may-like-items").length
          for(let i=0;i<img_cards;i++){

          document.querySelectorAll("#may-like-items")[i].addEventListener("click",function(){
            const sku = document.querySelectorAll("#Items-Sku-Card")[i].textContent;
           // alert(sku);

               $.ajax({
                  type: "POST",
                  url: "/home/products/display/item",
                  data: JSON.stringify(sku),
                  contentType: "application/json",
                  dataType: 'json'
               }).done(function(data){
                if(data.this_item=='ok'){
                       location.href='/home/products/display/item';
                 }else{
                      location.href='/';
                 }
               });

          });
       }







   });