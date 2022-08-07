
$( document ).ready(function() {


          const doc = {sku:"",title:"",descript:"",size:"",color:"",url_img:"",available_stock:true,
                        counter:0,price:0};


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


                        doc.color = this.style.backgroundColor;
                       // document.querySelectorAll(".add-item-color")[i].style.backgroundColor=doc.color;
                                alert(doc.color);

                });
          }




          //send the list to python
          document.querySelector("#add-item-cart").addEventListener("click",function(){
            //we get ref of size color  add-item-sku
             const temp_list = []
             temp_list.push(doc)
             doc.sku = document.querySelector("#add-item-sku").textContent;

             alert(doc.sku[0]);
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