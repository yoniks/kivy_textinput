

$( document ).ready(function() {


        const home_cards= document.querySelectorAll("#home-may-like-items").length
        for(let i=0;i<home_cards;i++){
          document.querySelectorAll("#home-may-like-items")[i].addEventListener("click",function(){
            const sku = document.querySelectorAll("#Home-Items-Sku-Card")[i].textContent;
            alert(sku);

               $.ajax({
                  type: "POST",
                  url: "/home/new/items/display",
                  data: JSON.stringify(sku),
                  contentType: "application/json",
                  dataType: 'json'
               }).done(function(data){
                if(data.this_item=='ok'){
                       location.href='/home/new/items/display';
                 }else{
                      location.href='/';
                 }
               });

          });
       }


   });