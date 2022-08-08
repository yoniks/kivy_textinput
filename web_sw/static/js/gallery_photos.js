
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

                        doc.color = this.style.backgroundColor;
                        document.querySelectorAll(".add-item-color")[i].style.border="1px solid #000000";
                         document.querySelectorAll(".add-item-color")[i].style.width = "30px";
                         document.querySelectorAll(".add-item-color")[i].style.height = "30px";

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
              const test = document.querySelector("#search-img").textContent;
              alert(doc.price);

              alert(doc.color)
              temp_list.push(doc)

           if(doc.sku[0]=='D' && doc.sku[1]=='R'){
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

            }else if(doc.sku[0]=='S' && doc.sku[1]=='W'){




            }





         });//CLOSE click function








 });