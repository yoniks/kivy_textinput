




          const img_cards= document.querySelectorAll("#ToSwimwear-Card").length
          for(let i=0;i<img_cards;i++){
          document.querySelectorAll("#ToSwimwear-Card")[i].addEventListener("click",function(){
           let sku = document.querySelector("#ToSwimwear-Sku-Card").textContent;

            if(sku.length>0){
               $.ajax({
                  type: "POST",
                  url: "/home/gallery/photos/swimwear/to",
                  data: JSON.stringify(sku),
                  contentType: "application/json",
                  dataType: 'json'
               }).done(function(data){
                if(data.swimwear=='ok'){
                    start =  setTimeout(function(){// play delay 1 second
                     clearTimeout(start);

                       location.href='/home/gallery/photos/swimwear/to';
                    },1000);

                }else{
                 alert('something went wrong');
                }
               });


            }

          });
   }