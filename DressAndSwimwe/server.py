import datetime
import datetime
import time

class Parent:
# this class extends to dresses and swimwear and we user it to add items of users,
#we not use it to aet from server becouse size and color must be list.
    def __init__(self):
        self.sku = ''
        self.title = ''
        self.descript = ''
        self.size = 'size'   #('S' ,'M' ,'L')
        self.color = 'color'
        self.color_text = ''
        self.url_img = ''
        self.available_stock = True
        self.counter = 1
        self.price = 0

    def set_sku(self, sku):
        if isinstance(sku,str):
           self.sku = sku
    def set_price(self, price):
        if isinstance(price,int):
           self.price = price
    def set_title(self, title):
        if isinstance(title, str):
           self.title = title
    def set_size(self, size):
        self.size = size
    def set_colors(self, colors):
        self.colors = colors
    def set_url_img(self,url_img):
        self.url_img = url_img
    def set_counter(self, counter):
        self.counter = counter
    def set_available_stock(self, available_stock):
        if available_stock ==False or available_stock==True:
           self.available_stock = available_stock
    def get_color(self):
        return self.colors
    def get_sku(self):
        return self.sku
    def get_price(self):
        return self.price
    def get_size(self):
        return self.size
    def get_url_img(self):
        return self.url_img
    def get_name_item(self):
        return self.title
    def get_counter(self):
        return self.counter
    def get_available_stock(self):
        return self.available_stock
   # def set_url_img(self, *args):
    #    if args != None:
     #      self.url_img= args



class Swimwear(Parent):
    def print_sw(self):
        return 'sku: ' +self.get_sku()


class Dresses(Parent):
    def print_sw(self):
        return 'sku: ' +self.get_sku()

class General(Parent):
    def print_sw(self):
        return 'sku: ' +self.get_sku()



class Discount:
    def __init__(self,sku,price,name_item,discount_percent):
        self.discount_percent= discount_percent



class Users:
    def __init__(self,name,email,city,address,zip, mobile):
        """uniq id we cant call it"""
        self.__user_id = 0
        self.email = email
        self.name = name
        self.mobile = mobile
        self.city = city
        self.address = address
        self.zip = zip


    def get_user_id(self):
        dt = int(d.day) + int(d.month) + int(d.year)
        self.__user_id = int(time.time()) + dt
        return self.__user_id
    def set_password(self, password):
        self.password = password
    def get_password(self):
        return self.password
        #if email is not exsit in database than  fun create_new_user_id create new id to user
    def set_user(self, email, name, user_id,phone ,city, address):
        self.email = email
        self.name = name
        self.user_id = user_id
        self.city= city
        self.address= address
        self.phone = phone
    def clear_user(self):
        self.name=''
        self.email=''
        self.city=''
        self.user_id=0
        self.city=''
        self.zip=''
        self.mobile=''
        self.address=''
        return True



d = datetime.datetime.now()
class Ordering:

    def __init__(self):
         self.order_id= 0
         self.swimwear_list = []
         self.dresses_list = []
         self.general_list = []
         self.total_price = 0
         self.date = str(d.day) + " " + str(d.strftime("%B")) + " " + str(d.year)

    def get_date(self):
        return self.date
    def set_order_id(self,ID):
        self.order_id = ID

    def get_order_id(self):
        if self.order_id == 0:
           dt = int(d.day)+int(d.month)+int(d.year)
           self.order_id = int(time.time())+dt
        return self.order_id


    def add_dresses_to_bag(self,price, obj):#sku, name_item, size, color, price, link
        self.dresses_list.append(obj)
        self.total_price += price

    def get_dresses_list(self):
        return self.dresses_list

    def remove_at_dresses(self, price, item):
        for itm in self.dresses_list:
            if itm.sku == item['sku'] and itm.color == item['color'] and itm.size == item['size']:
                print("removed dresses...")
                self.dresses_list.remove(itm)
                self.total_price -= price
                return True
        return False


    def add_swimwear_list_to_bag(self,price,obj):
        self.swimwear_list.append(obj)
        self.total_price += price
    def get_swimwear_list(self):
        return self.swimwear_list

    def remove_at_swimwear(self, price, item):
        print("remove_at_swimwear")
        for itm in self.swimwear_list:
            if itm.sku == item['sku'] and itm.color == item['color'] and itm.size == item['size']:
                self.swimwear_list.remove(itm)
                self.total_price -= price
                return True
        return False


    def add_general_list_to_bag(self,price,obj):
        self.general_list.append(obj)
        self.total_price += price
    def get_general_list(self):
        return self.general_list
    def remove_at_general(self,price,item):
        for itm in self.general_list:
            if itm.sku == item['sku'] and itm.color == item['color'] and itm.size == item['size']:
                self.general_list.remove(itm)
                self.total_price -= price
                return True
        return False



    def remove_old_order(self):
        dr = len(self.dresses_list)
        sw = len(self.swimwear_list)
        print(dr)
        if dr > 0:
           self.dresses_list.clear()
        if sw > 0:
           self.swimwear_list.clear()
        self.total_price = 0
        self.order_id = 0
        if len(self.dresses_list)==0 and len(self.swimwear_list)==0 and self.total_price ==0 and self.order_id==0:
            return True
        else:
            return False

    def get_total_price(self):
         return self.total_price





class Payment():
    def __init__(self):
        self.user_id = 0
        self.number_order = 0
        self.name_card = ''
        self.number_cart = 0
        self.expires_month = 0
        self.expires_year = 0
        self.cvv_card = 0
        self.total_refund = 0


class Current_Order():

    def __init__(self, _id,user_id,email,date,total_price,
                    delivery, name_card , credit_card, status_order_accept,status_shipping,is_cancel):
        self._id=_id
        self.user_id=user_id
        self.email=email
        self.date=date
        self.total_price=total_price
        self.delivery=delivery
        self.name_card= name_card
        self.credit_card = credit_card
        self.status_order_accept = status_order_accept
        self.status_shipping = status_shipping
        self.is_cancel = is_cancel
        self.st1 = []
        self.st2 = []
        self.st3 = []
        self.cancel = []
        self.not_initialize = True


    def shipping(self, name,city,address,zip,mobile):
        self.name = name
        self.city = city
        self.address = address
        self.zip = zip
        self.mobile = mobile

    def set_st1(self, st1):
        self.st1.append(st1)
    def set_st2(self, st2):
        self.st2.append(st2)
    def set_st3(self, st3):
        self.st3.append(st3)
    def set_cancel(self, cancel_):
        self.cancel.append(cancel_)
    def get_st1(self):
        return self.st1
    def get_st2(self):
        return self.st2
    def get_st3(self):
        return self.st3
    def get_cancel(self):
        return self.cancel
    def remove_all(self):
        if len(self.st1) > 0:
           self.st1.clear()
        if len(self.st2) > 0:
           self.st2.clear()
        if len(self.st3) > 0:
           self.st3.clear()
        if len(self.cancel) > 0:
           self.cancel.clear()
        return True

    def get_initialize(self):
        return self.not_initialize
    def set_initialize(self,is_in):
        self.not_initialize = is_in




class Trigger_Items():
    def __init__(self):
        self.obj_urls = []
        self.sku_product = ''
        self.list_swimwear = []
        self.temp_swimwear = []
        self.list_dress = []
        self.temp_dress = []
        self.list_new_collection = []
        self.temp_new_collection = []

        self.manage_items = []

    def add_single_item(self,it):
        self.manage_items.clear()
        self.manage_items.append(it)

    def get_single_item(self):
        return self.manage_items


    def add_swimwear(self,it):
        self.list_swimwear.append(it)
    def get_swimwear(self):
        return self.list_swimwear
    def add_temp_swimwear(self,it):
        self.temp_swimwear.append(it)
    def get_temp_swimwear(self):
        return self.temp_swimwear


    def add_dress(self,it):
        self.list_dress.append(it)
    def get_dress(self):
        return self.list_dress
    def add_temp_dress(self,it):
        self.temp_dress.append(it)
    def get_temp_dress(self):
        return self.temp_dress


    def add_new_collection(self,it):
        self.list_new_collection.append(it)
    def get_new_collection(self):
        return self.list_new_collection
    def add_temp_new_collection(self,it):
        self.temp_new_collection.append(it)
    def get_temp_new_collection(self):
        return self.temp_new_collection


    def set_sku(self,sku):
        self.sku_product= None
        self.sku_product = sku
    def get_sku(self):
        return self.sku_product

    def add_urls(self,it):
        self.obj_urls.append(it)
    def get_urls(self):
        return self.obj_urls













import time

#from main import Swimwear, Dresses,General, Users, Ordering,Current_Order, Trigger_Items
from aws_server import upload_data
import invoice_pdf
import send_emails
from reportlab.pdfgen import canvas
from pymongo import MongoClient
from pprint import pprint
from flask import Flask, request, render_template, session, redirect, jsonify,url_for
import os
from dotenv import load_dotenv
from twilio.rest import Client
import secrets
import datetime

"""
#Note:  server start again every change we doing at the code   
#session['id_item'] is not affect on change in code and refresh, the value saved at server
session.pop('user_id', None)
"""

load_dotenv()
app = Flask(__name__)
#  Set the secret key to some random bytes. Keep this really secret!
app.secret_key = secrets.token_hex()  # b'_5#y2L"F4Q8z\n\xec]/'
#print(app.secret_key)


TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN= os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_VERIFY_SERVICE = os.environ.get('TWILIO_VERIFY_SERVICE')
SENDGRID_API_KEY= os.environ.get('SENDGRID_API_KEY')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


pass_to = os.environ.get('MDB_URL')
print(pass_to)
os.environ['MDB_URL'] = pass_to
"""this class holding the order of items user and delete items """
clients = MongoClient(os.environ['MDB_URL'])
ord = Ordering()
mng = Trigger_Items()
user = Users("","","","","","")
@app.route('/')#add to list
def open_home():

    if 'user_id' in session:
        if len(user.email) > 0:
            print("user exist: ",user.email,"-",session["user_id"],"-",user.name)
        elif session['user_id'] > 0:
            print("try find by user id")
            set_user_with_id()
       
    if len(mng.get_new_collection()) == 0:
        with MongoClient(os.environ['MDB_URL']) as client:
            counter = 0
            cursor = client.DesignerClothes.home_img_url.find({})
            for it in cursor:
                if counter == 0:
                    counter = 1
                    mng.add_urls(it)
                else:
                   doc = {"title": it['title'], "sku": it['sku'], "url_img": it['url_img'][0]['img'][0],
                          "price": it['price']}
                   mng.add_temp_new_collection(doc)
                   mng.add_new_collection(it)

    return render_template('Home.html', list_home_new_product=mng.get_temp_new_collection(),url_img=mng.get_urls())



"""
1)list_dresses_to and list_first_group_dresses_to 
initialize one time from database mongoDB to fill the html.
2)temp_first_group holding some of value- title,sku,one url img, and price
when user click on the img we display all the photos with description
"""


@app.route('/home/dresses/db/download')#methods=['GET']
def start_download_dresses():
    if len(mng.get_dress()) == 0:
         db = clients['DesignerClothes']
         """this database storage multiple colors to each ticket and sizes"""
         b_dresses = db['first_group_dresses']
         cursor = b_dresses.find({})  # bring all Documents
         for it in cursor:
             doc = {"title":it['title'] ,"sku": it['sku'],"url_img":it['url_img'][0]['img'][0],"price":it['price']}
             mng.add_temp_dress(doc)
             mng.add_dress(it)
    return render_template('Dresses.html',temp_list_dresses=mng.get_temp_dress())


""" list_swimwear_to 
initialize one time from database mongoDB to fill the html"""

@app.route('/home/swimwear/db/download')
def start_download_swimwear():
    if len(mng.get_swimwear()) == 0:
         """get_database()"""
         db = clients['DesignerClothes']
         swimwear = db['swimwear']
         cursor = swimwear.find({})  # bring all Documents
         for it in cursor:
             doc = {"title":it['title'] ,"sku": it['sku'],"url_img":it['url_img'][0]['img'][0],"price":it['price']}
             mng.add_temp_swimwear(doc)
             mng.add_swimwear(it)
    return render_template('Swimwear.html',list_swimwear=mng.get_temp_swimwear())


@app.route('/home/dresses/to',methods=['POST'])
def set_dresses():
    if request.method == 'POST':# user add to cart
        list_dress = request.get_json()
        for it in list_dress:
            print("added to set_dresses() ", it['sku'])
            add_to_cart = Dresses()
            add_to_cart.title = it['title']
            add_to_cart.descript = it['descript']
            add_to_cart.sku = it['sku']
            add_to_cart.size = it['size']
            add_to_cart.color = it['color']
            add_to_cart.price = int(it['price'])
            add_to_cart.counter = int(it['counter'])
            add_to_cart.url_img = it['url_img']
            temp_price= add_to_cart.price * add_to_cart.counter
            """we add the item to list that user sent """
            ord.add_dresses_to_bag(temp_price,add_to_cart)
        return jsonify({'data': 'ok'})



"""add item"""
@app.route('/home/swimwear/to',methods=['POST'])
def set_swimwear():
    if request.method == 'POST':
        list_swimwear = request.get_json()
        for it in list_swimwear:
           add_to_cart = Swimwear()
           add_to_cart.title = it['title']
           add_to_cart.descript = it['descript']
           add_to_cart.sku = it['sku']
           add_to_cart.size = it['size']
           add_to_cart.color = it['color']
           add_to_cart.price = int(it['price'])
           add_to_cart.counter = int(it['counter'])
           add_to_cart.url_img = it['url_img']
           temp_price = add_to_cart.price * add_to_cart.counter
           ord.add_swimwear_list_to_bag(temp_price, add_to_cart)
        return jsonify({'data': 'ok'})

"""add item"""
@app.route('/home/general/to',methods=['POST'])
def set_general():
    if request.method == 'POST':
        list_general = request.get_json()
        for it in list_general:
           add_to_cart = General()
           add_to_cart.title = it['title']
           add_to_cart.descript = it['descript']
           add_to_cart.sku = it['sku']
           add_to_cart.size = it['size']
           add_to_cart.color = it['color']
           add_to_cart.price = int(it['price'])
           add_to_cart.counter = int(it['counter'])
           add_to_cart.url_img = it['url_img']
           temp_price = add_to_cart.price * add_to_cart.counter
           ord.add_general_list_to_bag(temp_price, add_to_cart)
        return jsonify({'data': 'ok'})





"""
 set_ticket_swimwear(): and set_ticket_dresses(): use to Display the particular ticket
 trigger it:
 1) user click on img ticket we send sku to function (dresses or swimwear)
 2) we search with sku the ticket to display user single item, 
 item including colors, sizes,photos, price,description and button to add cart,
if user add to cart we send to set_swimwear(): or  set_dresses(): function
 and the class Dresses()  or Swimwear() hold the object than 
 class Ordering() has lists of both of class to add the single object 
"""





@app.route('/home/products/display/item', methods=['POST'])
def set_single_item_without_refresh():
    if request.method == 'POST':  # user add to cart
        """ 'we get id sku and  search in list of all dresses than send to Page SingleItem '"""
        sku = request.form['sku']
        if len(sku) > 0:
            """ 'initialize sku of product' """
            init = sku[0]+sku[1]
            mng.set_sku(init)
            print("sku", mng.get_sku(),sku)
            if sku[0] == 'D' and sku[1] == 'R' and len(mng.get_dress())>0:
              for it in mng.get_dress():
                  if sku == it['sku']:
                      mng.add_single_item(it)
                      return render_template('TempSingleItem.html', single_item=mng.get_single_item(),
                                             may_like_=mng.get_temp_dress())

            elif sku[0] == 'S' and sku[1] == 'W' and len(mng.get_swimwear())>0:
                for it in mng.get_swimwear():
                    if sku == it['sku']:
                        mng.add_single_item(it)
                        return render_template('TempSingleItem.html', single_item=mng.get_single_item(),
                                               may_like_=mng.get_temp_dress())

            elif sku[0] == 'N' and sku[1] == 'W'  and len(mng.get_new_collection())>0:
                 for it in mng.get_new_collection():
                     if sku == it['sku']:
                         mng.add_single_item(it)
                         return render_template('TempSingleItem.html', single_item=mng.get_single_item(),
                                                may_like_=mng.get_temp_new_collection())
            return jsonify({'this_item': 'error'})


@app.route('/home/products/display/item/shown',methods=['POST','GET'])#methods=['GET']
def set_single_item():

    sku = str(request.args.get('sku'))
    global isit
    print(sku)
    """ 'initialize sku of product' """
    if len(sku)>0:
             isit = sku[0] + sku[1]
             print(isit)
             if isit == "DR" and len(mng.get_dress()) > 0:
                 for it in mng.get_dress():
                     if sku == it['sku']:
                         mng.add_single_item(it)
                         return render_template('SingleItem.html', single_item=mng.get_single_item(),
                                                may_like_=mng.get_temp_dress())

             elif isit =="SW" and len(mng.get_swimwear()) > 0:
                 for it in mng.get_swimwear():
                     if sku == it['sku']:
                         mng.add_single_item(it)
                         return render_template('SingleItem.html', single_item=mng.get_single_item(),
                                                may_like_=mng.get_temp_swimwear())

             elif isit == 'NW' and len(mng.get_new_collection()) > 0:
                 for it in mng.get_new_collection():
                     if sku == it['sku']:
                         mng.add_single_item(it)
                         return render_template('SingleItem.html', single_item=mng.get_single_item(),
                                                may_like_=mng.get_temp_new_collection())







        






#lest step




############






@app.route('/home/cart/add/order/user/orders',methods=['POST','GET'])
def set_cart():
    # the list of swimwear and Dresses snding to cart when click on it
    # user can delete item at cart page and we upData with property
    # class of Ordering
    sku = str(request.args.get('sku'))
    color = str(request.args.get('color'))
    size = str(request.args.get('size'))
    price = str(request.args.get('price'))
    print("set cart sku=",sku, price)
    if len(sku) > 0 and len(price) > 0:
        obj = {"sku": sku, "color": color, "size": size, "price": price}
        """function identifier_item_of_cart() find if it is ticket of 
        dresses or swimwear by id sku with letters DR OR SW"""
        is_group = identifier_item_of_cart(sku)
        print(">", is_group)
        if is_group == "dresses":
            ord.remove_at_dresses(int(price), obj)
        elif is_group == "swimwear":
            ord.remove_at_swimwear(int(price), obj)
        elif is_group == "general":
            ord.remove_at_general(int(price), obj)

    is_login = False
    if "user_id" in session and len(user.email) > 0:
         is_login = True
    cities = {"city": ["Tel Aviv", "Ramat gan", "Givatayim"]}
    name_card = {"card": ["MasterCard", "Visa", "American Express"]}
    return render_template('Cart.html', dresses=ord.get_dresses_list(),
                    swimwear=ord.get_swimwear_list(), general=ord.get_general_list(), total=ord.get_total_price(), user_=user,
                    cities=cities, is_login=is_login, name_card=name_card)




"""
 if user remove item from cart i must updata the list but this function return the 
 name of list to search, (group dresses,dresses,swimwear) by sku we defined.  
"""
def identifier_item_of_cart(sku):
    text = ''
    for at in sku:
        if at.isdigit():
            pass
        else:
            text += at
    print("identifier: ", text)
    if text == "DR":
        return "dresses"
    elif text == "SW":
        return "swimwear"
    elif text == "NW":
        return "general"

"""we send email with invoice after we have sent the to database"""
@app.route("/home/order/invoice/send/email", methods=['POST'])
def convert_to_pdf():
    """
    const doc_credit_card = {"order_id":0,"name_card":name_card,"number_card":number_card.value,
     "exp_month":exp_month.value,"exp_year":exp_year.value,"cvv":cvv.value }
    """
    if request.method == "POST":
        if "id_order" in session:
           if session['id_order'] == 0:
               return jsonify({"invoice": "error"})
           pay = request.get_json()
           pay['id_order'] = session['id_order']
           session['id_order'] = 0
           upload_data(pay['id_order'])#AWS

           if ord.remove_old_order():
             print("order removed after sent")
           else:
             print("error. order don't removed")
           print("payment: ", pay)
           if send_emails.send_email_with_pdf(user.email,pay['id_order']):
              if user.clear_user():
                  print("cleared the User")
              return jsonify({"invoice": "ok"})
           else:
              print("error")
              return jsonify({"invoice": "error"})


"""create pdf invoice and send order to database """
@app.route('/home/send/order/to/database', methods=['POST'])
def send_order_to_database():
    #1 we check if user made login
    #2 we create uniq id order
    #3 we send the order
    if request.method == "POST":
       print('send order to')
       if 'user_id' in session and len(user.email) > 0:
         if session["user_id"] < 11000:
            return jsonify({"order":"error"})
         else:
            ship_to = request.get_json()#(self,name,city,address,zip, phone):

            to = Users(ship_to['name'],ship_to['email'],ship_to['city'],ship_to['address'],ship_to['zip'],ship_to['mobile'])
            shipping = {"name":to.name , "city":to.city, "address":to.address, "zip":to.zip, "mobile":to.mobile}

            print("shipping_to: ",to.email, user.email)
            db = clients['orders']
            items = db['items']
            """create id order,with time of second, we initialize list for database"""
            id_to_order = ord.get_order_id()
            session['id_order'] = id_to_order
            items_dresses = []
            items_swimwear = []
            items_general = []

            if len(ord.get_dresses_list()) > 0 or len(ord.get_swimwear_list()) > 0 or len(ord.get_general_list())>0: #or len(ord.rent_list)>0:
               if id_to_order > 0:
                   """ just with class of Ordring we add or remove  object"""
                   for d in ord.get_dresses_list():
                       items_dresses.append({"sku":d.sku,"title":d.title,"size":d.size,"color":d.color,
                                             "url_img":d.url_img,"available_stock":d.available_stock,
                                             "counter":d.counter,"price":d.price})
                   for s in ord.get_swimwear_list():
                       items_swimwear.append({"sku":s.sku,"title":s.title,"size":s.size,"color":s.color,
                                             "url_img":s.url_img,"available_stock":s.available_stock,
                                             "counter":s.counter,"price":s.price})
                   for g in ord.get_general_list():
                       items_general.append({"sku":g.sku,"title":g.title,"size":g.size,"color":g.color,
                                             "url_img":g.url_img,"available_stock":g.available_stock,
                                             "counter":g.counter,"price":g.price})

                   """evey new order we create new document in database, email not change"""
                   items.insert_one({'_id':id_to_order,'user_id':session["user_id"],'email':to.email,
                                 'shipping':shipping,
                                 'date':ord.get_date(),
                                 'list_dress':items_dresses,
                                  'list_swimwear':items_swimwear,
                                  'list_general':items_general,
                                 'total_price':ord.get_total_price(),
                                 'name_card':ship_to['name_card'],
                                 'credit_card':ship_to['credit_card'],
                                 'is_cancel':False,
                                 'status_order_accept':False,
                                 'status_shipping':False})
                   """we also need to check if user change address of delivery  we update it """

                   if items.count_documents({"_id":id_to_order}) > 0:
                       """to update the last address at user database"""
                       if update_shipping_to_address(ship_to):
                          print("order sent to database")
                          """if name user not in database but the user input the name in credit card so initialize for invoice"""
                          ord.set_order_id(id_to_order)
                          user.name = ship_to['name']
                          invoice_pdf.create_pdf(ord, user,ship_to)#create pdf invoice to user
                          return jsonify({"order": "sent"})
                       else:
                           return jsonify({"order": "error"})
                   else:
                       return jsonify({"order": "error"})
       else:
           return jsonify({"order": "not_register"})




"""
  def __init__(self, _id,user_id,email,name,date,total_price,city,address,
                    zip,phone,delivery,status_order_accept,status_shipping,is_cancel):
"""


history = Current_Order(0, 0, "", "", "", "", "", "", False, False, False)
"""status shipping order and cancel order in online if the order didn't delivery to customer int(session['user_id'])"""
@app.route("/home/shipping/order/")#methods=['GET']
def current_order():
    #session['user_id'] = 11000
    #user.email = 'yoni.ch@icloud.com'
    if 'user_id' in session and len(user.email) > 0 and history.get_initialize():

       db =  clients['orders']
       items = db['items']
       user_id = session['user_id']
       st1 =  items.find({"user_id":user_id,"status_order_accept":False,"status_shipping": False,"is_cancel":False})
       for it in st1:

           o1 = Current_Order(it['_id'],it['user_id'],it['email'],it['date'],
                             it['total_price'],
                             "yes",it['name_card'],it['credit_card'],it['status_order_accept'],it['status_shipping'],
                             it['is_cancel'])
           o1.shipping(it['shipping']['name'],it['shipping']['city'],it['shipping']['address'],
                       it['shipping']['zip'],it['shipping']['mobile'])
           history.set_st1(o1)
       st2 = items.find({"user_id": user_id,"status_order_accept":True ,"status_shipping": False,"is_cancel":False})
       for it in st2:
           o2 = Current_Order(it['_id'],it['user_id'],it['email'],it['date'],
                             it['total_price'],
                             "yes",it['name_card'],it['credit_card'], it['status_order_accept'],it['status_shipping'],
                             it['is_cancel'])
           o2.shipping(it['shipping']['name'],it['shipping']['city'],it['shipping']['address'],
                       it['shipping']['zip'],it['shipping']['mobile'])
           history.set_st2(o2)
       st3 = items.find({"user_id": user_id, "status_order_accept": True, "status_shipping": True,"is_cancel":False})
       """ST3 WE MUST HIDDEN THE BUTTON"""
       for it in st3:
           o3 = Current_Order(it['_id'],it['user_id'],it['email'],it['date'],
                             it['total_price'],
                             "yes", it['name_card'],it['credit_card'],it['status_order_accept'],it['status_shipping'],
                             it['is_cancel'])
           o3.shipping(it['shipping']['name'],it['shipping']['city'],it['shipping']['address'],
                                   it['shipping']['zip'],it['shipping']['mobile'])
           history.set_st3(o3)
       CANCEL = items.find({"user_id":user_id,"is_cancel":True})
       for it in CANCEL:
           cancel_ = Current_Order(it['_id'], it['user_id'], it['email'], it['date'],
                              it['total_price'],
                              "canceled",it['name_card'],it['credit_card'], it['status_order_accept'], it['status_shipping'],
                              it['is_cancel'])
           cancel_.shipping(it['shipping']['name'],it['shipping']['city'],it['shipping']['address'],
                       it['shipping']['zip'],it['shipping']['mobile'])
           history.set_cancel(cancel_)
       if len(history.get_st1())>0 or len(history.get_st2())>0 or len(history.get_st3())>0 or len(history.get_cancel())>0:
           history.set_initialize(False)
    return render_template("Status_Shipping.html", st1=history.get_st1(), st2=history.get_st2(),
                           st3=history.get_st3(), canceled=history.get_cancel(),user=user)



"""if user want to cancel the order than we return id of order and
 search in database to set true in field of is_cancel, the order must be 
 exist in DATABASE because we first download the order id and create button to option of cancel
  than when the user sent we refresh the page and call again to documents of database """
@app.route("/home/items/current/order/to/cancel", methods=['POST'])
def cancel_order_do_not_shipped():

    if request.method == "POST":
       order_id = request.get_json()
       order_id = int(order_id)
       print("id_order_:",order_id)
       db = clients['orders']
       items = db['items']
       items.update_one({"_id": order_id}, {'$set': {"is_cancel": True}})
       item = items.find_one({"_id": order_id})
       for it in item:
           print(item[it])
           if len(it) ==0:
               print("000")
       if items.count_documents({"_id": order_id}) > 0:
           history.set_initialize(True)
           print(history.remove_all())
           return jsonify({"canceled": True})
       else:
           return jsonify({"error_to_update": True})








#verify Email
@app.route('/login/verify', methods=['POST'])
def login():
    # _email = request.form['email']

    if request.method == 'POST':
        _email = request.get_json()
        _email = _email.strip().replace(" ", "")
        if "user_id" in session:  # Email already verified
            return jsonify({'status': 'verified'})
        if "counter_attempts" in session and "today_date" in session:
            td = session["today_date"]
            if td != str(datetime.date.today()) and len(td) > 1 and session["counter_attempts"] < 3:
                session["counter_attempts"] = 3
        else:
            """#given to user 3 times a day to input some email that is not valid
             if the variable is zero we none/block sending"""
            session["counter_attempts"] = 3
            session["today_date"] = str(datetime.date.today())
        if session["counter_attempts"] <= 0:
            """if refresh the page counter session still live we block again"""
            return jsonify({'status': 0})
        """go database to counter if bigger from 4 sends a single day"""
        if listen_to_sender(_email) >= 4:
            session["counter_attempts"] = 0
            return jsonify({'status': "limit_to_4"})
        is_valid = send_verification(_email)
        if is_valid:
            """# so now you should input password you have 3 time again"""
            session["_email"] = _email
            return jsonify({'status': 'ok'})
        else:
            session["counter_attempts"] -= 1
            return jsonify({'status': session["counter_attempts"]})



def send_verification(to_email):
    verification = client.verify.services(TWILIO_VERIFY_SERVICE).verifications.create(to=to_email, channel='email')
    print("No verification ", verification.sid, "-", verification)
    if verification.sid:
        return True
    else:
        return False





@app.route('/pass/verify', methods=['POST'])
def generate_verification_code():
    """  verification_code = request.form['']"""
    if request.method == 'POST':
        verify_code = request.get_json()
        verify_code = verify_code.strip().replace(" ", "")
        if "user_id" in session:  # Email already verified
            return jsonify({'status': 'verified'})
        if "counter_pass_attempts" in session and "today_date" in session:
            td = session["today_date"]
            if td != str(datetime.date.today()) and len(td)>1 and session["counter_pass_attempts"] < 3:
                session["counter_pass_attempts"] = 3
            else:
                """#given to user 3 times to input some pass if the variable is zero we none/block sending"""
                session["counter_pass_attempts"] = 3

        if "_email" in session:
            _email = session['_email']
            if check_verification_token(_email, verify_code):# if verification return true
               """set_user() storage new user or set data from mongo and initialize the constractor of usr"""
               if set_user(_email):
                  return jsonify({'status': 'ok'})
               else:
                   return jsonify({'status': 'fail_to_storage_user'})
            else:
                session["counter_pass_attempts"] -= 1
                return jsonify({'status': session["counter_pass_attempts"]})
        else:
            return jsonify({'status': 'fail_to_storage_user'})



def check_verification_token(email, token):
    check = client.verify \
        .services(TWILIO_VERIFY_SERVICE) \
        .verification_checks \
        .create(to=email, code=token)
    return check.status == 'approved'



"""
 # go from new doc to old
 id_doc = collection.find().limit(1).sort([('_id', -1)])  # or $natural
 user_id = int(id_doc[0]['_id'])
 user_id+= 1
"""
def temp_find_user(email):
    """delete it later hot.cup.espresso@gmail.com"""
    if len(email) > 0:
        """clients = get_database()"""
        with MongoClient(os.environ['MDB_URL']) as client:
             _it = client.Users.user.find_one({"email":email})
             if _it!=None:
               print("user initialized")
               session['user_id'] = _it['_id']  # from database
               user.email = _it['email']
               user.name = _it['name']
               user.phone = _it['mobile']
               user.address = _it['address']
               print("--",user.name)
               return True

def set_user(email):

 if len(email) > 0:
     """clients = get_database()"""
     with MongoClient(os.environ['MDB_URL']) as client:
         _it = client.Users.user.find_one({"email": email})
         if _it != None:
             print("user initialized")
             session['user_id'] = _it['_id']  # from database
             user.email = _it['email']
             user.name = _it['name']
             user.phone = _it['mobile']
             user.address = _it['address']
             print("--", user)
             return True
         else: #the user not exsit in database
           """user get one time id that we create by time and date"""
           user_id = user.get_user_id()
           doc = {"_id":user_id, "name":"", "email": email, "mobile": "", "city": "", "address": ""}
           client.Users.user.insert_one(doc)
           if client.Users.user.count_documents({"_id": user_id}) > 0:#if there success to create new account
              get_user = client.Users.user.find_one({"email": email})
              session['user_id'] = get_user['_id']
              user.email = get_user['email']
              session['_email'] = user.email
              return True
           else:
               return False
 else:
    return False


def set_user_with_id():
    if 'user_id' in session:
        user_id = session['user_id']
        db = clients["Users"]
        users = db["user"]
        _user = users.find_one({"_id":user_id})
        if _user!=None:
           if len(_user['email']) > 0 and _user['_id']>0:#must return str and int and >1000
              session['user_id'] = _user['_id']#from database
              user.email = _user['email']
              user.name = _user['name']
              user.phone = _user['mobile']
              user.address = _user['address']
              print("666 set_user_with_id():", user)
              return True
    return False




"""WE UPDATE THE ADDRESS CITY ZIP WHEN USER SEND ORDER WE NOT UPDATE THE EMAIL"""
def update_shipping_to_address(data):
    #email,name,city ,address,zip, user.email is initialize when user login,
    if "user_id" in session and len(user.email) > 0:
       db = clients["Users"]
       tuser = db["user"]
       user_id = session['user_id']
       update = tuser.find_one({"_id":user_id})
       if update!=None:
          tuser.update_one({"_id":user_id},{'$set':{"name":data['name'],"mobile":data['mobile'],
                               "city":data['city'],"address":data['address'],"zip":data['zip'] }})
          if tuser.count_documents({"email":user.email}) > 0:
                return True
          else:
              return True
    return False

def listen_to_sender(email):
    print("listen to sender", email)
    d = str(datetime.date.today())
    db = clients["Users"]
    listen = db["Listen_To_Sender"]
    _sender = listen.find_one({"email": email})
    if _sender != None:
       print("exists")
       for it in _sender['sender']:
           if it['date']==d:
               print("eq: ",it['date'])
               count = int(it['counter'])
               to_update = {"date": d, "counter": (count+1)}
               print(to_update["counter"])
               listen.update_one({"email": email,"sender.date":d}, {'$set': {"sender":[to_update]} })#"sender":[exists]
               return to_update["counter"]
       this_day = {"date": d, "counter": 1}
       listen.update_one({"email": email}, {'$push': {"sender": this_day}})# add one obj to list
       return 1
    else:
        print("not exists")
        this_day = {"date":d,"counter":1}
        doc = {"email": email,"sender":[this_day]}
        listen.insert_one(doc)
        return 1






@app.route('/home/send/email/to/subscript', methods=['POST'])
def set_email_subscript():
    if request.method == 'POST':
        get_email = request.get_json()

        if len(get_email)>0:
            d = datetime.datetime.now()
            dmy = str(d.day) +"/"+ str(d.month)+"/"+str(d.year)
            subscript = {"date":dmy,"email":get_email}
            with MongoClient(os.environ['MDB_URL']) as client:
                _it = client.Users.subscript.insert_one(subscript)
            return jsonify({"received":"sent"})
        else:
            return jsonify({"received": "error"})

if __name__ == "__main__":
    app.debug = True
    app.run(port=5500)
   






