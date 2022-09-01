
$( document ).ready(function() {



   //this card open new page to display gallery and information on each single item

      const img_cards= document.querySelectorAll("#ToDresses-Card").length
          for(let i=0;i<img_cards;i++){

          document.querySelectorAll("#ToDresses-Card")[i].addEventListener("click",function(){
            const sku = document.querySelectorAll("#ToDresses-Sku-Card")[i].textContent;
           // alert(sku)

            if(sku.length>0){
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



   });
