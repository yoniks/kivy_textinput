
$( document ).ready(function() {


          const doc = {sku:"",title:"",descript:"",size:"",color:"",url_img:"",available_stock:true,
                        counter:1,price:0};


          let list_size = document.querySelectorAll("li.size-item").length;
          for(let i=0;i<list_size;i++){
             document.querySelectorAll("li.size-item")[i].addEventListener("click",function(){

                         document.querySelector("#add-item-size").innerHTML=this.textContent;// this.textContent;
                        doc.size = this.textContent;
                                alert(doc.size);
                });
          }

          //add-item-color
            let btn_colors = document.querySelectorAll(".add-item-color").length;
          for(let i=0;i<btn_colors;i++){
             document.querySelectorAll(".add-item-color")[i].addEventListener("click",function(){
                        for(let i=0;i<btn_colors;i++){
                           document.querySelectorAll(".add-item-color")[i].style.width = "25px";
                           document.querySelectorAll(".add-item-color")[i].style.height = "25px";
                           document.querySelectorAll(".add-item-color")[i].style.border="0.5px solid #000000";
                        }

                        
                        document.querySelectorAll(".add-item-color")[i].style.border="1px solid #000000";
                         document.querySelectorAll(".add-item-color")[i].style.width = "30px";
                         document.querySelectorAll(".add-item-color")[i].style.height = "30px";
                       
                        doc.color = this.style.backgroundColor;
                        doc.url_img = document.querySelectorAll("#search-img")[i].textContent;

                               // alert(doc.color);

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
                     document.querySelector("#add-item-cart").innerHTML='Added';
                    start =  setTimeout(function(){// play delay 1 second
                     document.querySelector("#add-item-cart").innerHTML='ADD TO CARD';
                     document.querySelector("#add-item-size").innerHTML='SIZE';

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
                     document.querySelector("#add-item-cart").innerHTML='Added';
                    start =  setTimeout(function(){// play delay 1 second
                     document.querySelector("#add-item-cart").innerHTML='ADD TO CARD';
                     document.querySelector("#add-item-size").innerHTML='SIZE';
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
              let btn_colors = document.querySelectorAll(".add-item-color").length;
              for(let i=0;i<btn_colors;i++){
                           document.querySelectorAll(".add-item-color")[i].style.width = "25px";
                           document.querySelectorAll(".add-item-color")[i].style.height = "25px";
                           document.querySelectorAll(".add-item-color")[i].style.border="0.5px solid #000000";
                        }
              }



         });//CLOSE add  function








 });
