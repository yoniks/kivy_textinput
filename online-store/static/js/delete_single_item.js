


$( document ).ready(function() {

//cart-delete-dr
  let list_order= document.querySelectorAll("#cart-delete-dr").length;
   for(let i=0;i<list_order;i++){
 document.querySelectorAll("#cart-delete-dr")[i].addEventListener("click",function(){
      // alert("dress");
    document.querySelectorAll("#cart-delete-dr").disabled=true;
   const sku = document.querySelectorAll("#cart-sku-dr")[i].textContent;
   const color = document.querySelectorAll("#cart-color-dr")[i].textContent;
   const size = document.querySelectorAll("#cart-size-dr")[i].textContent;
   const price = document.querySelectorAll("#cart-price-dr")[i].textContent;
   const counter = parseInt(document.querySelectorAll("#cart-counter-dr")[i].textContent);
   //const doc = {"sku":sku,"color":color,"size":size,"price":(price*counter)};



          ref = $.ajax({
          type: "POST",
           url: "/home/cart/delete/to",
           data:{sku:sku,color:color,size:size,price:(price*counter)}
          });
         ref.done(function(data){

             window.location.href="/home/cart/add/order/user";
         });//close ajax
         document.querySelectorAll("#cart-delete-dr").disabled=false;


 });
 }

 //cart-delete-sw
   let list_order_sw= document.querySelectorAll("#cart-delete-sw").length;
   for(let i=0;i<list_order_sw;i++){
 document.querySelectorAll("#cart-delete-sw")[i].addEventListener("click",function(){
    document.querySelectorAll("#cart-delete-sw").disabled=true;

   const sku = document.querySelectorAll("#cart-sku-sw")[i].textContent;
   const color = document.querySelectorAll("#cart-color-sw")[i].textContent;
   const size = document.querySelectorAll("#cart-size-sw")[i].textContent;
   const price = document.querySelectorAll("#cart-price-sw")[i].textContent;
   const counter = parseInt(document.querySelectorAll("#cart-counter-sw")[i].textContent);
   //const doc = {"sku":sku,"color":color,"size":size,"price":(price*counter)};

      ref = $.ajax({
          type: "POST",
           url: "/home/cart/delete/to",
           data:{sku:sku,color:color,size:size,price:(price*counter)}
          });
         ref.done(function(data){

             window.location.href="/home/cart/add/order/user";
         });//close ajax
       document.querySelectorAll("#cart-delete-sw").disabled=false;
 });
 }


 //general list
 //cart-delete-nw
   let list_order_nw= document.querySelectorAll("#cart-delete-nw").length;
   for(let i=0;i<list_order_nw;i++){
 document.querySelectorAll("#cart-delete-nw")[i].addEventListener("click",function(){
    document.querySelectorAll("#cart-delete-nw").disabled=true;

   const sku = document.querySelectorAll("#cart-sku-nw")[i].textContent;
   const color = document.querySelectorAll("#cart-color-nw")[i].textContent;
   const size = document.querySelectorAll("#cart-size-nw")[i].textContent;
   const price = document.querySelectorAll("#cart-price-nw")[i].textContent;
   const counter = parseInt(document.querySelectorAll("#cart-counter-nw")[i].textContent);
   //const doc = {"sku":sku,"color":color,"size":size,"price":(price*counter)};

      ref = $.ajax({
          type: "POST",
           url: "/home/cart/delete/to",
           data:{sku:sku,color:color,size:size,price:(price*counter)}
          });
         ref.done(function(data){

             window.location.href="/home/cart/add/order/user";
         });//close ajax
       document.querySelectorAll("#cart-delete-nw").disabled=false;
 });
 }

});