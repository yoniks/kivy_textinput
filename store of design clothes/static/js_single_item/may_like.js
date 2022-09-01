



$( document ).ready(function() {





        const img_cards= document.querySelectorAll("#ToDresses-Card").length
          for(let i=0;i<img_cards;i++){

          document.querySelectorAll("#ToDresses-Card")[i].addEventListener("click",function(){
            const sku = document.querySelectorAll("#ToDresses-Sku-Card")[i].textContent;
            alert(sku);

            if(sku[0]=="D" && sku[1]=="R"){
               $.ajax({
                  type: "POST",
                  url: "/home/gallery/photos/dresses/to",
                  data: JSON.stringify(sku),
                  contentType: "application/json",
                  dataType: 'json'
               }).done(function(data){
                if(data.dresses=='ok'){
                       location.href='/home/gallery/photos/dresses/to';
                 }else{
                    alert('something went wrong  please Exit From Page!');
                 }
               });


            }else{
              alert('sku is Empty');
            }

          });
       }







          const swimwear_card= document.querySelectorAll("#ToSwimwear-Card").length;
        for(let i=0;i<swimwear_card;i++){
             document.querySelectorAll("#ToSwimwear-Card")[i].addEventListener("click",function(){
                   const sku = document.querySelectorAll("#ToSwimwear-Sku-Card")[i].textContent;
                   alert(sku);
                   alert(sku[0]);
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