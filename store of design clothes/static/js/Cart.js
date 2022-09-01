
$( document ).ready(function() {


const city = {city:""};
const is_exist = document.querySelector("#payment-order");
if(is_exist){

   document.querySelector("#payment-order").addEventListener("click",function(){
      document.querySelector("#payment-order").disabled=true;
      document.querySelector("#play-spinners").hidden=false;
      document.querySelector("#text-status").innerHTML="Sending Your Email Please Wait";


      const Name = document.querySelector('input[name="name"]');
      const Address = document.querySelector('input[name="address"]');
      const City = city.city;
      const Zip = document.querySelector('input[name="zip"]');
      const Phone = document.querySelector('input[name="phone"]');


      const name_card = document.querySelector('input[name="get_card_name"]');
      const number_card = document.querySelector('input[name="get_card_number"]');
      const exp_month = document.querySelector('input[name="get_month"]');
      const exp_year = document.querySelector('input[name="get_year"]');
      const cvv = document.querySelector('input[name="get_cvv"]');

      //condition if the value are digit if the filed not empty
      number_card.value = number_card.value.slice(-4);

      let is_not_digit = false;
      for(let i=0;i<number_card.value.length;i++){
          if(number_card.value.charCodeAt(i)<48 || number_card.value.charCodeAt(i)>57){
           is_not_digit = true;
           break;
          }
      }
      if(is_not_digit){
        alert("some of input invalid")
      }else{


        const doc_credit_card = {"id_order":0,"name_card":name_card.value,"number_card":number_card.value,
        "exp_month":exp_month.value,"exp_year":exp_year.value,"cvv":cvv.value }

        const doc = {"name":Name.value,"city":City,"address":Address.value,"zip":Zip.value,
        "mobile":Phone.value,"name_card":name_card.value,"credit_card":number_card.value}
      //condition if not empty send the order
        $.ajax({
            type: "POST",
            url: "/home/send/order/to/database",
            data: JSON.stringify(doc),
            contentType: "application/json",
            dataType: 'json'
            }).done(function(data){
          if(data.order=="sent"){
            //than  we can send the the invoice
          //   location.href='/home/cart/add/to';
                  $.ajax({
                       type: "POST",
                        url: "/home/order/invoice/send/email",
                        data: JSON.stringify(doc_credit_card),
                        contentType: "application/json",
                        dataType: 'json'
                      }).done(function(data){
                         if(data.invoice=="ok"){
                            document.querySelector("#text-status").innerHTML="invoice sent to email";
                            start =  setTimeout(function(){
                              document.querySelector("#payment-order").disabled=false;
                              document.querySelector("#play-spinners").hidden=true;
                              document.querySelector("#text-status").innerHTML="Pay";
                              location.href='/';
                              clearTimeout(start);
                            },1000);
                         }else{
                          alert("failed to send Document to email")
                         }

                      });

          }else if(data.order=="not_register"){
              alert("Please Login")
              location.href='/';
          }else{
            alert("something went wrong");
            location.href='/';
          }

         });//close ajax

         }//else if  values are valid

   });//listen to payment-order
}//is exist payment-order

let list_city= document.querySelectorAll("li.list_city").length;
 for(let i=0;i<list_city;i++){
    document.querySelectorAll("li.list_city")[i].addEventListener("click",function(){

        city.city = this.textContent;
        document.querySelector("#cart-add-city").innerHTML = this.textContent;
    });
 }





//cart-delete-dr
  let list_order= document.querySelectorAll("#cart-delete-dr").length;
   for(let i=0;i<list_order;i++){
 document.querySelectorAll("#cart-delete-dr")[i].addEventListener("click",function(){
      // alert("dress");
   const sku = document.querySelectorAll("#cart-sku-dr")[i].textContent;
   const color = document.querySelectorAll("#cart-color-dr")[i].textContent;
   const size = document.querySelectorAll("#cart-size-dr")[i].textContent;
   const price = document.querySelectorAll("#cart-price-dr")[i].textContent;
   const counter = parseInt(document.querySelectorAll("#cart-counter-dr")[i].textContent);
   const doc = {"sku":sku,"color":color,"size":size,"price":(price*counter)};

      $.ajax({
          type: "POST",
           url: "/home/cart/delete/to",
           data: JSON.stringify(doc),
           contentType: "application/json",
           dataType: 'json'
          }).done(function(data){
          if(data.deletes==true){
             location.href='/home/cart/add/to';
            /*  start =  setTimeout(function(){// play delay 1 second
              clearTimeout(start);
              },1000);*/

          }else{
           alert("something went wrong");
          }

         });//close ajax

 });
 }

 //cart-delete-sw
   let list_order_sw= document.querySelectorAll("#cart-delete-sw").length;
   for(let i=0;i<list_order_sw;i++){
 document.querySelectorAll("#cart-delete-sw")[i].addEventListener("click",function(){

   const sku = document.querySelectorAll("#cart-sku-sw")[i].textContent;
   const color = document.querySelectorAll("#cart-color-sw")[i].textContent;
   const size = document.querySelectorAll("#cart-size-sw")[i].textContent;
   const price = document.querySelectorAll("#cart-price-sw")[i].textContent;
   const counter = parseInt(document.querySelectorAll("#cart-counter-sw")[i].textContent);
   const doc = {"sku":sku,"color":color,"size":size,"price":(price*counter)};

      $.ajax({
          type: "POST",
           url: "/home/cart/delete/to",
           data: JSON.stringify(doc),
           contentType: "application/json",
           dataType: 'json'
          }).done(function(data){
          if(data.deletes==true){
             location.href='/home/cart/add/to';
             /* start =  setTimeout(function(){// play delay 1 second
              clearTimeout(start);
              },1000);*/

          }

         });//close ajax

 });
 }




});