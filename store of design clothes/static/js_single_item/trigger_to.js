
$( document ).ready(function() {
// add item to cart, this html get the first group dresses and swimwear

          const doc = {sku:"",title:"",descript:"",size:"",color:"",color_text:"",url_img:"",available_stock:true,
                        counter:1,price:0};



          //add size

              const obj_size = document.querySelectorAll(".add-size").length;
          for(let i=0;i<obj_size;i++){
             document.querySelectorAll(".add-size")[i].addEventListener("click",function(){
                        for(let i=0;i<obj_size;i++){
                           document.querySelectorAll(".add-size")[i].style.width = "25px";
                           document.querySelectorAll(".add-size")[i].style.height = "25px";
                           document.querySelectorAll(".add-size")[i].style.border="0.5px solid #000000";
                        }

                       doc.size = document.querySelectorAll("#add-single-size")[i].textContent;
                       // alert(doc.size);
                       // doc.color = this.style.backgroundColor;
                        document.querySelectorAll(".add-size")[i].style.border="1px solid #000000";
                         document.querySelectorAll(".add-size")[i].style.width = "30px";
                         document.querySelectorAll(".add-size")[i].style.height = "30px";


                });
          }





          //add-item-color

          const  obj_colors = document.querySelectorAll(".add-item-color").length;
          for(let i=0;i<obj_colors;i++){
             document.querySelectorAll(".add-item-color")[i].addEventListener("click",function(){
                        for(let i=0;i<obj_colors;i++){
                           document.querySelectorAll(".add-item-color")[i].style.width = "25px";
                           document.querySelectorAll(".add-item-color")[i].style.height = "25px";
                           document.querySelectorAll(".add-item-color")[i].style.border="0.5px solid #000000";
                        }

                        doc.url_img = document.querySelectorAll("#search-img")[i].textContent;
                        doc.color = document.querySelectorAll("#gallery-item-color")[i].textContent;
                        doc.color_text = document.querySelectorAll("#gallery-item-color-text")[i].textContent;
                       // doc.color = this.style.backgroundColor;
                        document.querySelectorAll(".add-item-color")[i].style.border="1px solid #000000";
                         document.querySelectorAll(".add-item-color")[i].style.width = "30px";
                         document.querySelectorAll(".add-item-color")[i].style.height = "30px";


                });
          }




          //send the list to python
          document.querySelector("#add-item-cart").addEventListener("click",function(){
            //we get ref of size color  add-item-sku
             const temp_list = []
             doc.sku = document.querySelector("#add-item-sku").textContent;
             doc.price = parseInt(document.querySelector("#add-item-price").textContent);
              doc.title = document.querySelector("#add-item-title").textContent;


              temp_list.push(doc)

           if(doc.sku[0]=='D' && doc.sku[1]=='R' && doc.color.length>0 && doc.size.length>0){
               $.ajax({
                  type: "POST",
                  url: "/home/dresses/to",
                  data: JSON.stringify(temp_list),
                  contentType: "application/json",
                  dataType: 'json'
               }).done(function(data){
                if(data.dresses=='ok'){
                     document.querySelector('input[name="add-item"]').value='Added';

                    start =  setTimeout(function(){// play delay 1 second
                     document.querySelector('input[name="add-item"]').value='ADD TO CARD';
                     clearTimeout(start);

                    },1000);

                }

                });//close ajax

            }else if(doc.sku[0]=='S' && doc.sku[1]=='W' && doc.color.length>0 && doc.size.length>0){


                  $.ajax({
                  type: "POST",
                  url: "/home/swimwear/to",
                  data: JSON.stringify(temp_list),
                  contentType: "application/json",
                  dataType: 'json'
               }).done(function(data){
                if(data.dresses=='ok'){
                     document.querySelector('input[name="add-item"]').value='Added';
                    start =  setTimeout(function(){// play delay 1 second
                     document.querySelector('input[name="add-item"]').value='ADD TO CARD';

                     clearTimeout(start);

                    },1000);
                }

                });//close ajax




            }else{
             alert('Please Select Color and  Size');
            }

             if(doc.color.length>0 && doc.size.length>0){// clean anyway if the item sent or not
                doc.color="";
                doc.size ="";
                doc.url_img="";

              for(let i=0;i<obj_colors;i++){
                           document.querySelectorAll(".add-item-color")[i].style.width = "25px";
                           document.querySelectorAll(".add-item-color")[i].style.height = "25px";
                           document.querySelectorAll(".add-item-color")[i].style.border="0.5px solid #000000";


                        }
              }
               for(let i=0;i<obj_size;i++){
                           document.querySelectorAll(".add-size")[i].style.width = "25px";
                           document.querySelectorAll(".add-size")[i].style.height = "25px";
                           document.querySelectorAll(".add-size")[i].style.border="0.5px solid #000000";
                        }



         });//CLOSE add  function








 });