

$( document ).ready(function() {


          const swimwear_card= document.querySelectorAll("#ToSwimwear-Card").length;
        for(let i=0;i<swimwear_card;i++){
             document.querySelectorAll("#ToSwimwear-Card")[i].addEventListener("click",function(){
                   const sku = document.querySelectorAll("#ToSwimwear-Sku-Card")[i].textContent;
                   // alert(sku);
              if(sku.length>0){
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
                         location.href = '/';
                      //alert('something went wrong');
                    }
               });//of ajax


              }

          });
       }//for




   });