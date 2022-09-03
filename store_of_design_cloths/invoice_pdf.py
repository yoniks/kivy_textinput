from reportlab.pdfgen import canvas
from reportlab.lib.colors import pink, green, brown, white,black,magenta
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from main import Swimwear, Dresses, Users, Ordering

import datetime


width , height = letter
d = datetime.datetime.now()
date = str(d.day) + " " + str(d.strftime("%B")) + " " + str(d.year)
doc = {"sku":"1234","color":"black","size":"S","price":"100"}
def add_items(canvas,num, it):


   canvas.drawImage(it.url_img, inch / 2, (inch * num), 100, 100, mask=None)

   """title coloe and size"""
   textobject = canvas.beginText()
   textobject.setTextOrigin(100+inch, (inch * (num+1)))
   move_to_y = textobject.getY()+14
   textobject.setFont("Helvetica-Oblique", 9)

   textobject.setFillGray(0.4)
   textobject.textLines(str(it.title))
   move_to_x = textobject.getX()

   textobject.textLine("")
   textobject.textLines("Color: "+ str(it.color_text)+"/"+str(it.color))

   textobject.textLine("")
   textobject.textLines("Size: "+ str(it.size))
   canvas.drawText(textobject)
   move_to_total_y = textobject.getY()

   """counter"""

   counter = 1
   textobject = canvas.beginText()
   textobject.setTextOrigin(move_to_x+inch*2, move_to_y)#100 + inch + move*6
   textobject.setFont("Helvetica-Oblique", 10)
   move_to_y = textobject.getY()
   textobject.textLine("QTY ")
   textobject.setFillGray(0.4)
   textobject.textLine("")
   textobject.textLine("")
   textobject.textLines(str(it.counter))
   canvas.drawText(textobject)


   """subtotal"""
   move_to_x = textobject.getX()
   textobject = canvas.beginText()
   textobject.setTextOrigin(move_to_x+inch, move_to_y)
   textobject.setFont("Helvetica-Oblique", 10)
   textobject.textLine("SUBTOTAL ")
   textobject.setFillGray(0.4)
   textobject.textLine("")
   textobject.textLine("")
   textobject.textLines(str(it.price))
   canvas.drawText(textobject)
   print(textobject.getX(),", ",textobject.getY(),", ",height - (inch * 4))
   global save_height
   save_height = textobject.getY()







def data_to_canvas(c, width, height,id_order, user):
   # c.setFillColorRGB(255, 153, 255)
   c.setFillColorRGB(0, 0, 0)
   c.setFont("Helvetica", 10)
   c.drawString(inch / 2, height, "No Order:")
   c.drawString(inch * 1.3, height , str(id_order))
   c.line(inch * 1.3, height-3 , inch * 2, height-3)

   of_height = height+25
   c.setFillColorRGB(0, 0, 0)
   c.setFont("Helvetica", 10)
   c.drawString(inch / 2, of_height , "Date:")
   c.drawString(inch, of_height, date)
   c.line(inch, of_height-3  , inch * 2, of_height-3  )

   of_height+=25
   c.setFillColorRGB(0, 0, 0)
   c.setFont("Helvetica", 10)
   c.drawString(inch / 2, of_height, "Email:")
   c.drawString(inch, of_height, user.email)
   c.line(inch, of_height-3, inch * 2.4,of_height-3)

   of_height += 25
   c.setFillColorRGB(0, 0, 0)
   c.setFont("Helvetica", 10)
   c.drawString(inch/2, of_height, "Name:")
   c.drawString(inch, of_height , user.name_user)
   c.line(inch, of_height-3 , inch*1.7, of_height-3)

   of_height +=25
   c.setFillColor(magenta)
   c.setFont("Helvetica-Bold", 24)
   c.drawString(width/2.5,of_height, "Hani's Design")  # 612.0 792.0

   of_height -= 20
   c.setFont("Helvetica-Bold", 9)
   c.drawString(width / 2.5, of_height, '''contact us: hani_shitrit@hanisdesign.com''')

   of_height -= 15
   c.setFont("Helvetica-Bold", 9)
   c.drawString(width/2.5, of_height,  '''Exempt Dealer: #######''')







def credit_card(canvas,num_cradit_card,total_price,name,Address,City,Zip,Mobile):
   textobject = canvas.beginText()
   textobject.setTextOrigin(inch, inch+5)
   textobject.setFont("Helvetica-Oblique", 10)
   textobject.setFillGray(0.4)
   textobject.textLines("Delivery: ")
   textobject.setTextOrigin((inch+5), inch)
   textobject.setFont("Helvetica-Oblique", 9)
   textobject.textLine("Address: "+Address)
   textobject.textLine("City: " + City)
   textobject.textLine("Zip: " + Zip)
   textobject.textLine("Mobile: "+Mobile)


   """cradit card"""
   textobject.setTextOrigin(width / 2.5, (inch-15))
   textobject.setFont("Helvetica-Oblique", 10)
   textobject.textLines("Total: " + str(total_price))
   textobject.setTextOrigin(width / 2.5, inch)
   textobject.setFont("Helvetica-Oblique", 9)
   textobject.setFillGray(0.4)
   textobject.textLines("Master Card: " + "**** **** **** "+num_cradit_card)
   textobject.setTextOrigin(width / 2.2, inch+15)
   textobject.setFont("Helvetica-Oblique", 10)
   textobject.textLines(name)



   """SUMMART TOTAL after tickets
   textobject.setTextOrigin(inch, inch)
   textobject.setFont("Helvetica-Oblique", 9)
   textobject.textLines("Total: " + str(total_price))
   textobject.setTextOrigin(inch, inch + 15)
   textobject.textLine("SUMMART: ")
   textobject.setFillGray(0.4)
   """

   textobject.setTextOrigin(width / 2.2, inch+70)
   charspace = 0.5
   textobject.setCharSpace(charspace)
   textobject.setFont("Helvetica-Oblique", 15)
   textobject.textLines("PayMent")
   canvas.drawText(textobject)

   canvas.setLineWidth(0.5)
   canvas.line(inch, inch +100, width - inch, inch +100)
   print(textobject.getY(), "-", height)




def create_pdf(items, id_to_order,get_user,shipping):
   last_item = len(items.get_dresses_list())
   last_item += len(items.get_swimwear_list())
   total_price = str(items.get_total_price())
   print("last item", last_item,"- ",total_price)
   if  len(items.get_dresses_list()) > 0 or len(items.get_swimwear_list()) > 0:
        my_canvas = canvas.Canvas('invoice.pdf', pagesize=letter)
        print("w: ", width, "h: ", height, "shipping_to: ", shipping)#updata to database and if name is empty than
        """shipping_to is object sent from js when user sent the order"""
        credit_card(my_canvas,shipping['credit_card'],total_price,shipping['name'],
                    shipping['address'],shipping['city'],shipping['zip'],shipping['mobile'])
        start_y = 3

        for it in items.get_dresses_list():
              add_items(my_canvas, start_y, it)
              start_y += 1.5

        for it in items.get_swimwear_list():
              add_items(my_canvas, start_y, it)
              start_y += 1.5

        my_canvas.setPageSize((width, (save_height + 300)))
        data_to_canvas(my_canvas, width,save_height+100 , id_to_order, get_user)
        my_canvas.showPage()
        my_canvas.save()








