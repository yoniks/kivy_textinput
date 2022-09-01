

$( document ).ready(function() {


          const swimwear_card= document.querySelectorAll("#ToSwimwear-Card").length;
        for(let i=0;i<swimwear_card;i++){
             document.querySelectorAll("#ToSwimwear-Card")[i].addEventListener("click",function(){
                   const sku = document.querySelectorAll("#ToSwimwear-Sku-Card")[i].textContent;
                   // alert(sku);
              if(sku[0]=="S" && sku[1]=="W"){
                   $.ajax({
                    type: "POST",
                     url: "/home/gallery/photos/swimwear/to",
                     data: JSON.stringify(sku),
                     contentType: "application/json",
                    dataType: 'json'
                  }).done(function(data){
                    if(data.swimwear=='ok'){
                   /* start =  setTimeout(function(){// play delay 1 second
                     clearTimeout(start);
                      },500);*/
                       location.href='/home/gallery/photos/swimwear/to';

                    }else{
                      alert('something went wrong');
                    }
               });//of ajax


              }

          });
       }//for




   });