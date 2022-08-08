
$( document ).ready(function() {
          const doc = {sku:"",title:"",descript:"",size:"",color:"",url_img:"",available_stock:true,
                        counter:0,price:0}
          const doc_list = [];


        //to add size
         let ref_to=0,count_element=0,uniq_sku='';
         let  select_size = document.querySelectorAll("#ToSizeDress").length;
          for(let i=0;i<select_size;i++){
              document.querySelectorAll("#ToSizeDress")[i].addEventListener("click",function(){
              count_element = document.querySelectorAll("#ToAddDress")[i].textContent;
              uniq_sku = document.querySelectorAll("#sku_id_item")[ref_to].textContent;//uniq id of item
              ref_to=i;
             });
          }

         let list_size = document.querySelectorAll("li.size_dress").length;
          for(let i=0;i<list_size;i++){
             document.querySelectorAll("li.size_dress")[i].addEventListener("click",function(){
                 //3)if user want change the size ,

                 // document.querySelectorAll("#ToSizeDress")[ref_to].innerHTML= "";
                if(count_element>0){

                   for(let ref in doc_list){
                      if(doc_list[ref].sku==uniq_sku){//includes(uniq_sku)
                          doc_list[ref].size = this.textContent;
                         //let temp = doc_list[ref].split(',');
                         //doc_list.splice(ref,1)

                         document.querySelectorAll("#ToSizeDress")[ref_to].innerHTML=doc_list[ref].size;
                         }
                   }
                }else{
                  doc.title = document.querySelectorAll("#name_dress")[ref_to].textContent;//name dress
                  doc.descript = document.querySelectorAll("#descript")[ref_to].textContent;//name dress
                  doc.price = document.querySelectorAll("#price_dress")[ref_to].textContent;//add price
                  doc.url_img = document.querySelectorAll("#link_dress")[ref_to].src; //add link img
                  doc.size = this.textContent;// from list of size
                  document.querySelectorAll("#ToSizeDress")[ref_to].innerHTML=this.innerHTML;//upData
                }
             });
          }






          //colors
          let select_color = document.querySelectorAll("#ToColorDress").length;
          for(let i=0;i<select_color;i++){
            document.querySelectorAll("#ToColorDress")[i].addEventListener("click",function(){
               // doc.color = document.querySelectorAll("#ToColorDress")[i].style.backgroundColor;
                doc.color = this.style.backgroundColor;

                alert(doc.color)

             });
          }









            // add_dress

             let list_select_dress = document.querySelectorAll("#ToAddDress").length;
          for(let i=0;i<list_select_dress;i++){
            document.querySelectorAll("#ToAddDress")[i].addEventListener("click",function(){
                ref_to = i;
             });
          }

          let list_add_dress = document.querySelectorAll("li.add_dress").length;
          for(let i=0;i<list_add_dress;i++){
             document.querySelectorAll("li.add_dress")[i].addEventListener("click",function(){

             //if user selected the properties than add to list and counter it
             if(doc.size.length>0 && doc.color.length>0 &&doc.title.length>0){
                 doc.sku =  document.querySelectorAll("#sku_id_item")[ref_to].textContent;//uniq id of item
                 doc.counter = 1;

                 const temp_doc = {sku:doc.sku,title:doc.title,descript:doc.descript,
                                   size:doc.size,color:doc.color,url_img:doc.url_img,available_stock:true,
                                    counter:doc.counter,price:doc.price}
                 doc_list.push(temp_doc);
              for(let ref in doc){
               // delete doc[ref];// delete obj
                doc[ref] = "";
               }
                document.querySelectorAll("#ToAddDress")[ref_to].innerHTML=1;
                document.querySelector("#floating_btn_prc").style.display = 'block';


         }else{  //close of doc.size.length

         //1)check if item is exists in list and if size and color eq to list, if yes increase the counter and element html,
              if(parseInt(document.querySelectorAll("#ToAddDress")[ref_to].textContent)>0){//if there exist order in element
                    counter=parseInt(document.querySelectorAll("#ToAddDress")[ref_to].textContent)+1;
                    document.querySelectorAll("#ToAddDress")[ref_to].innerHTML =counter;
                    let uniq_sku = document.querySelectorAll("#sku_id_item")[ref_to].textContent;
                    for(let ref in doc_list){
                    if(doc_list[ref].sku==uniq_sku){
                       doc_list[ref].counter+=1;}
                    }
                }


         }
             });
          }







         // remove item of dress
          let list_less_dress = document.querySelectorAll("li.less_dress").length;
          for(let i=0;i<list_less_dress;i++){
             document.querySelectorAll("li.less_dress")[i].addEventListener("click",function(){

             let uniq_sku = document.querySelectorAll("#sku_id_item")[ref_to].textContent;//uniq id of item
               for(let ref in doc_list){
                   //let words = doc_list[ref].split(',')
                  if(doc_list[ref].sku==uniq_sku){// delete object with uniq of sku
                      if(doc_list[ref].counter>1){doc_list[ref].counter-=1; }else{// if bigger than 1 just counter it
                          doc_list.splice(ref,1)// if eq to one delete the object and upData element of html
                        }
                      if(parseInt(document.querySelectorAll("#ToAddDress")[ref_to].textContent) > 0){//less one in element
                         let counter = 0;
                         counter=parseInt(document.querySelectorAll("#ToAddDress")[ref_to].textContent);
                         if(counter>1){
                          document.querySelectorAll("#ToAddDress")[ref_to].innerHTML =(counter-1);
                         }else{
                          document.querySelectorAll("#ToAddDress")[ref_to].innerHTML ='Add';
                          document.querySelectorAll("#ToColorDress")[ref_to].innerHTML ='color';
                          document.querySelectorAll("#ToSizeDress")[ref_to].innerHTML = 'size';
                          document.querySelector("#floating_btn_prc").style.display = 'none';
                        }}

                  break;// to loop
               }  }//close for and if



             });
          }// close for of less dress



          //send the list to python
          document.querySelector("#floating_btn_prc").addEventListener("click",function(){

            if(doc_list.length>0){
               //document.querySelector(".floating_btn_prc").innerHTML='sent';
               $.ajax({
                  type: "POST",
                  url: "/home/dresses/to",///home/dresses/to
                  data: JSON.stringify(doc_list),
                  contentType: "application/json",
                  dataType: 'json'
               })
               .done(function(data){
                if(data.dresses=='ok'){
                    document.querySelector("#floating_btn_prc").innerHTML='Saved';
                    start =  setTimeout(function(){// play delay 1 second
                     document.querySelector("#floating_btn_prc").innerHTML='SAVE AND ADD TO BAG';
                     clearTimeout(start);
                      document.querySelector("#floating_btn_prc").style.display = 'none';
                    let list_select_dress = document.querySelectorAll("#ToAddDress").length;
                    for(let i=0;i<list_select_dress;i++){
                        document.querySelectorAll("#ToAddDress")[i].innerHTML ='Add';
                        document.querySelectorAll("#ToColorDress")[i].innerHTML ='color';
                        document.querySelectorAll("#ToSizeDress")[i].innerHTML = 'size';
                       }
                    for(let ref in doc_list){
                         doc_list.splice(ref,1);
                       }
                       location.href='/home/gallery/photos/dresses/to';
                    },1000);

                }else{
                  document.querySelector("#floating_btn_prc").style.display = 'please try again';
                }
               });


            }

          });





  //   document.querySelector("#to_dresses_link").addEventListener("click",function(){

   //  location.href='http://127.0.0.1:5000/home/dresses/to';
   // });

   //this card open new page to display gallery and information on each single item

      const img_cards= document.querySelectorAll("#ToDresses-Card").length
          for(let i=0;i<img_cards;i++){

          document.querySelectorAll("#ToDresses-Card")[i].addEventListener("click",function(){
            const sku = document.querySelectorAll("#ToDresses-Sku-Card")[i].textContent;
            alert(sku)

            if(sku.length>0){
               $.ajax({
                  type: "POST",
                  url: "/home/gallery/photos/dresses/to",
                  data: JSON.stringify(sku),
                  contentType: "application/json",
                  dataType: 'json'
               }).done(function(data){
                if(data.dresses=='ok'){
                    start =  setTimeout(function(){// play delay 1 second
                     clearTimeout(start);

                       location.href='/home/gallery/photos/dresses/to';
                    },1000);

                }else{
                 alert('something went wrong');
                }
               });


            }else{
              alert('sku is Empty');
            }

          });
   }



   });
