
$( document ).ready(function() {
          const  doc = {name:"" ,sku:"",price:0,size:"",colors:"",url_img:"",counter:0};
          const doc_list = [];


        //to add size
         let ref_to=0,count_element=0,uniq_sku='';
         let  select_size = document.querySelectorAll("#ToSizeDress").length;
          for(let i=0;i<select_size;i++){
            document.querySelectorAll("#ToSizeDress")[i].addEventListener("click",function(){
                console.log("index", i);
                count_element = document.querySelectorAll("#ToAddDress")[i].textContent;
                uniq_sku = document.querySelectorAll("#sku_id_item")[ref_to].textContent;//uniq id of item
                ref_to=i;
             });
          }

         let list_size = document.querySelectorAll("li.size_dress").length;
          for(let i=0;i<list_size;i++){
             document.querySelectorAll("li.size_dress")[i].addEventListener("click",function(){
                 //3)if user want change the size ,


                if(count_element>0){

                   for(let ref in doc_list){
                      if(doc_list[ref].sku==uniq_sku){//includes(uniq_sku)
                          doc_list[ref].size = this.textContent;
                         //let temp = doc_list[ref].split(',');
                         //doc_list.splice(ref,1)
                        // temp[3]  =  this.textContent;
                        // doc_list[ref]='temp[0]+","+temp[1]+","+temp[2] +","+temp[3] +","+temp[4]+","+temp[5]+","+temp[6]';
                         document.querySelectorAll("#ToSizeDress")[ref_to].innerHTML=doc_list[ref].size;
                         }
                   }
                }else{
                  doc.name = document.querySelectorAll("#name_dress")[ref_to].textContent;//name dress
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
                count_element = document.querySelectorAll("#ToAddDress")[i].textContent;
                uniq_sku = document.querySelectorAll("#sku_id_item")[ref_to].textContent;//uniq id of item
                ref_to=i;
             });
          }

         let list_color = document.querySelectorAll("li.color_dress").length;
          for(let i=0;i<list_color;i++){
             document.querySelectorAll("li.color_dress")[i].addEventListener("click",function(){
                   //3)if user want change the  color,
                  if(count_element>0){ //if the element of html bigger than 0 than the object exists in list
                     for(let ref in doc_list){
                         if(doc_list[ref].sku==uniq_sku){
                           doc_list[ref].color = this.textContent; //upData in object of list
                           document.querySelectorAll("#ToColorDress")[ref_to].innerHTML=doc_list[ref].color;
                         }
                     }
                }else{
                   document.querySelectorAll("#ToColorDress")[ref_to].innerHTML=this.innerHTML;
                   doc.colors = this.textContent;
                }
             });
          }







            // add_dress
            let counter=0;// for element of html
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
             if(doc.size.length>0 && doc.colors.length>0 &&doc.name.length>0){
                doc.sku =  document.querySelectorAll("#sku_id_item")[ref_to].textContent;//uniq id of item
                 doc.counter = 1;
                let name = doc.name,sku=doc.sku,price=doc.price,size=doc.size,color=doc.colors,url=doc.url_img,con=doc.counter;
                 doc_list.push({name:name,sku:sku,price:price,size:size,color:color,url:url,con:con});
             for(let ref in doc){
               // delete doc[ref];// delete obj
                doc[ref] = "";
              }
                document.querySelectorAll("#ToAddDress")[ref_to].innerHTML=1;


         }else{  //close of doc.size.length

         //1)check if item is exists in list and if size and color eq to list, if yes increase the counter and element html,
              if(parseInt(document.querySelectorAll("#ToAddDress")[ref_to].textContent)>0){//if there exist order in element
                    counter=parseInt(document.querySelectorAll("#ToAddDress")[ref_to].textContent)+1;
                    document.querySelectorAll("#ToAddDress")[ref_to].innerHTML =counter;
                    let uniq_sku = document.querySelectorAll("#sku_id_item")[ref_to].textContent;
                    for(let ref in doc_list){
                    if(doc_list[ref].sku==uniq_sku){
                       doc_list[ref].con+=1;}
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
                      if(doc_list[ref].con>1){doc_list[ref].con-=1; }else{// if bigger than 1 just counter it
                          doc_list.splice(ref,1)// if eq to one delete the object and upData element of html
                        }

                     if(parseInt(document.querySelectorAll("#ToAddDress")[ref_to].textContent) > 0){//less one in element
                        counter=parseInt(document.querySelectorAll("#ToAddDress")[ref_to].textContent);

                        if(counter>1){
                          document.querySelectorAll("#ToAddDress")[ref_to].innerHTML =(counter-1);
                        }else{
                          document.querySelectorAll("#ToAddDress")[ref_to].innerHTML ='Add';
                          document.querySelectorAll("#ToColorDress")[ref_to].innerHTML ='color';
                          document.querySelectorAll("#ToSizeDress")[ref_to].innerHTML = 'size';

                        }}

                  break;// to loop
               }  }//close for and if



             });
          }// close for of less dress





          //send the list to python
          document.querySelector(".floating_btn_prc").addEventListener("click",function(){

            if(doc_list.length>0){
               //document.querySelector(".floating_btn_prc").innerHTML='sent';
               $.ajax({
                  type: "POST",
                  url: "/home/nav/dress",
                  data: JSON.stringify(doc_list),
                  contentType: "application/json",
                  dataType: 'json'
               });
             //document.querySelector(".floating_btn_prc").innerHTML='Add To Card';

          let list_select_dress = document.querySelectorAll("#ToAddDress").length;
          for(let i=0;i<list_select_dress;i++){
              document.querySelectorAll("#ToAddDress")[i].innerHTML ='Add';
              document.querySelectorAll("#ToColorDress")[i].innerHTML ='color';
              document.querySelectorAll("#ToSizeDress")[i].innerHTML = 'size';
          }
              for(let ref in doc_list){
                  doc_list.splice(ref,1);
              }


            }else{
              document.querySelector(".floating_btn_prc").innerHTML = 'Empty List';
            }

          });

   });
        //dresses-tab "#home-tab", "#dresses-tab" document.querySelector(

