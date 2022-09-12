$( document ).ready(function() {


const is_exist = document.querySelectorAll("#status-shipping-1").length;
if(is_exist){
  const SIZE = document.querySelectorAll("#status-shipping-1").length;
  for(let i=0;i < SIZE; i++){
      document.querySelectorAll("#status-shipping-1")[i].addEventListener("click",function(){
           let order_id = document.querySelectorAll("#order-id-1")[i].textContent;


         if(order_id.length > 0){
            document.querySelectorAll("#status-shipping-1")[i].disabled=true;
            document.querySelectorAll("#play-spinners")[i].hidden=false;
           $.ajax({
             type: "POST",
             url: "/home/items/current/order/to/cancel",
             data: JSON.stringify(order_id),
             contentType: "application/json",
             dataType: 'json'
            }).done(function(data){
              if(data.canceled){//it is true
                 //alert("order is canceled");
                 window.location.href='/home/shipping/order/';
                 window.location.href='/home/shipping/order/';
              }else{//else it is not update
                alert("Please Try Again!");
                document.querySelectorAll("#status-shipping-1")[i].disabled=false;
                document.querySelectorAll("#play-spinners")[i].hidden=true;
              }

            });//done and order_id
            }

     });//listen to click
  }// loop of html array

}//condition if exist



// status accepet but not sent


const is_exist2 = document.querySelectorAll("#status-shipping-2").length;
if(is_exist2){
  const SIZE_ = document.querySelectorAll("#status-shipping-2").length;
  for(let i=0;i < SIZE_; i++){
      document.querySelectorAll("#status-shipping-2")[i].addEventListener("click",function(){
           let order_id = document.querySelectorAll("#order-id-2")[i].textContent;


         if(order_id.length > 0){
            document.querySelectorAll("#status-shipping-2")[i].disabled=true;
            document.querySelectorAll("#play-spinners-2")[i].hidden=false;
           $.ajax({
             type: "POST",
             url: "/home/items/current/order/to/cancel",
             data: JSON.stringify(order_id),
             contentType: "application/json",
             dataType: 'json'
            }).done(function(data){
              if(data.canceled){//it is true

                 window.location.href='/home/shipping/order/';
                  window.location.href='/home/shipping/order/';
              }else{//else it is not update
                alert("Please Try Again!");
                document.querySelectorAll("#status-shipping-2")[i].disabled=false;
                document.querySelectorAll("#play-spinners")[i].hidden=true;
              }

            });//done and order_id
            }

     });//listen to click
  }// loop of html array

}//condition if exist


});