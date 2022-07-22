import pymongo
from  pymongo import MongoClient
from pprint import pprint
from flask import Flask, request, url_for,render_template,session,redirect,escape
import secrets
import jinja2
app = Flask(__name__)
app.secret_key = secrets.token_hex()





# of js  {name:"" ,sku:"",price:0,size:"",colors:"",url_img:"",counter:0};
class Parent:

    def __init__(self):
        self.name_item = 0
        self.sku = ''
        self.price = 0
        self.size = 'size'   #('S' ,'M' ,'L')
        self.colors = 'color'
        self.url_img = ''
        self.available_stock = False
        self.counter = 0

    def set_sku(self, sku):
        if isinstance(sku,str):
           self.sku = sku
    def set_price(self, price):
        if isinstance(price,int):
           self.price = price
    def set_name_item(self, name_item):
        if isinstance(name_item, str):
           self.name_item = name_item
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
        return self.name_item
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



class Discount:
    def __init__(self,sku,price,name_item,discount_percent):
        self.discount_percent= discount_percent



class Users:
    def __init__(self,):
        self.email = ''
        self.name_user = ''
        self.phone = ''
        self.__user_id = 0
        self.password = ''
        self.city = ''
        self.address = ''

    def set_user_id(self, user_id):
        if user_id>1000 and isinstance(user_id, int):
           self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id
    def set_password(self, password):
        self.password = password
    def get_password(self):
        return self.password
        #if email is not exsit in database than  fun create_new_user_id create new id to user
    def set_user(self, email, name_user, user_id,phone ,city, address):
        self.email = email
        self.name_user = name_user
        self.user_id = user_id
        self.city= city
        self.address= address
        self.phone = phone



class Ordering:
    def __init__(self,  order_id):
         self.order_id= order_id
         self.swimwear_list = []
         self.dresses_list = []
         self.rent_list = []
         self.total_price = 0
         self.active = ['', '', '', '' ]  # num index of tags
         self.show_active = ['', '', '', '']  # num index of tags

    def get_order_id(self):
     return  self.order_id

    def add_to_cart(self,price, *obj_order):#sku, name_item, size, color, price, link
       self.swimwear_list.append(obj_order)
       self.total_price += price


    "'set many argument and cheak if it exists in list'"
    def remove_from_card(self,  price, *remove):
        for itm in self.swimwear_list:
            if itm == remove:
              self.swimwear_list.remove(remove)
              self.total_price =- price

    def get_total_price(self):
         return self.total_price

    def set_show_active(self,name):
        self.show_active = ['', '', '', '']
        if "home" == name:
            self.show_active[0] = 'show active'
        elif "Swimwear" == name:
            self.show_active[1] = 'show active'
        elif "Dresses" == name:
            self.show_active[2] = 'show active'

    def set_active(self,name):
        self.active = ['', '', '', '']
        if "home" == name:
            self.active[0] = 'active'
        elif "Swimwear" == name:
            self.show_active[1] = 'active'
        elif "Dresses" == name:
            self.active[2] = 'active'


    def get_active(self):
        return self.active

    def get_show_active(self):
        return self.show_active





class OrderHistory:
    def __init__(self, order_id, user_id, email, name_user,phone ,order_date, total_price, order_cancel):
        self.email = email
        self.name_user = name_user
        self.phone = phone
        self.order_id = order_id
        self.order_date = order_date
        self.total_price = total_price
        self.order_cancel = order_cancel
        self.items_order = []
        self.user_id = user_id

    def set_items_order(self,items):
        self.items_order = items
        for itm in self.items_order:
            print("\nOrderHistory: "+ str(itm))

    def send_to_database(self):
        if self.user_id is None or self.total_price is None:
            print('None')










#respon to tag
def add_to_cart(color,index):
    sw = Swimwear()
    res_as_path = request.path.split('/')
    # the keyword global open the variable to initialize in function
    global as_path
    as_path = res_as_path[1]















