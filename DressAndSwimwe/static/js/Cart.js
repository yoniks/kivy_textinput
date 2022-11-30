
$( document ).ready(function() {


const data_order = {city:"",name_card:""};
const is_exist = document.querySelector("#payment-order");
if(is_exist){

   document.querySelector("#payment-order").addEventListener("click",function(){


     
      const Name = document.querySelector('input[name="name"]');
       const email = document.querySelector('input[name="email"]');
      const Address = document.querySelector('input[name="address"]');
      const City = data_order.city;
      const Zip = document.querySelector('input[name="zip"]');
      const Phone = document.querySelector('input[name="phone"]');



      const name_card = data_order.name_card;//document.querySelector('input[name="get_card_name"]');
      const number_card = document.querySelector('input[name="get_card_number"]');
      const exp_month = document.querySelector('input[name="get_month"]');
      const exp_year = document.querySelector('input[name="get_year"]');
      const cvv = document.querySelector('input[name="get_cvv"]');

      //condition if the value are digit if the filed not empty
       let is_illegal = false;
       let message  = ''
      //number_card.value = number_card.value.slice(-4);
     if(Name.value.length<2 ||email.value.length<10||Address.value.length<2||City.length<2||Zip.value.length<3){
       is_illegal = true;
       message = 'One Field is left Empty or illegal. ';
     }

      for(let i=0;i<Phone.value.length;i++){
          if(Phone.value.charCodeAt(i)<48 || Phone.value.charCodeAt(i)>57){
             if((i==3||i==2)&&Phone.value.charCodeAt(i)==45){
              continue;
             }
             message += 'Field of Phone Must be Numbers. ';
             is_illegal = true;
              break;
          }
      }

      if(is_illegal){
        alert(message);
      }else{
        document.querySelector("#payment-order").disabled=true;
        document.querySelector("#play-spinners").hidden=false;
        document.querySelector("#text-status").innerHTML="Process...";



       /* const doc = {"name":Name.value,"city":City,"address":Address.value,"zip":Zip.value,
        "mobile":Phone.value,"name_card":name_card,"credit_card":number_card.value}*/
        const doc = {"name":Name.value,"email":email.value,"city":City,"address":Address.value,"zip":Zip.value,
        "mobile":Phone.value,"name_card":"","credit_card":""}
        // than send payment
        const doc_credit_card = {"id_order":0,"name":Name.value,"name_card":name_card,"number_card":number_card.value,
        "exp_month":exp_month.value,"exp_year":exp_year.value,"cvv":cvv.value }
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
                  $.ajax({
                       type: "POST",
                        url: "/home/order/invoice/send/email",
                        data: JSON.stringify(doc_credit_card),
                        contentType: "application/json",
                        dataType: 'json'
                      }).done(function(data){
                         if(data.invoice=="ok"){
                            document.querySelector("#text-status").innerHTML="Order Received. we Sent To Email";
                            start =  setTimeout(function(){
                              document.querySelector("#payment-order").disabled=false;
                              document.querySelector("#play-spinners").hidden=true;
                              document.querySelector("#text-status").innerHTML="Pay";
                              window.location.href='/';
                              
                              clearTimeout(start);
                            },1000);
                         }else{
                          alert("Something went wrong to send Email.");
                          document.querySelector("#payment-order").disabled=false;
                          document.querySelector("#play-spinners").hidden=true;
                          document.querySelector("#text-status").innerHTML="Pay";
                          window.location.href='/';
                         }

                      });

          }else if(data.order=="not_register"){
              alert("Please Login");
              window.location.href='/';
          }else{
            alert("Something went wrong. Try again later.");
            window.location.href='/';
          }
         
         });//close ajax

         }//else if  values are valid
         window.location.reload(); 
   });//listen to payment-order
}//is exist payment-order

let list_city= document.querySelectorAll("li.list_city").length;
 for(let i=0;i<list_city;i++){
    document.querySelectorAll("li.list_city")[i].addEventListener("click",function(){

        data_order.city = this.textContent;
        document.querySelector("#added-city").innerHTML = this.textContent;
    });
 }

let list_card= document.querySelectorAll("li.list_cards").length;
 for(let i=0;i<list_card;i++){
    document.querySelectorAll("li.list_cards")[i].addEventListener("click",function(){

        data_order.name_card = this.textContent;
        document.querySelector("#added-name-card").innerHTML = this.textContent;
    });
 }











});
