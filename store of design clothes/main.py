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



class Discount:
    def __init__(self,sku,price,name_item,discount_percent):
        self.discount_percent= discount_percent



class Users:
    def __init__(self,name,city,address,zip, mobile):
        """uniq id we cant call it"""
        self.__user_id = 0
        self.email = ''
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
    def set_user(self, email, name_user, user_id,phone ,city, address):
        self.email = email
        self.name_user = name_user
        self.user_id = user_id
        self.city= city
        self.address= address
        self.phone = phone


d = datetime.datetime.now()
class Ordering:

    def __init__(self):
         self.order_id= 0
         self.swimwear_list = []
         self.dresses_list = []
         self.total_price = 0
         self.date = str(d.day) + " " + str(d.strftime("%B")) + " " + str(d.year)

    def get_date(self):
        return self.date
    def set_order_id(self,ID):
        self.order_id = ID

    def get_order_id(self):
        dt = int(d.day)+int(d.month)+int(d.year)
        self.order_id = int(time.time())+dt
        return self.order_id

    def add_dresses_to_bag(self,price, obj):#sku, name_item, size, color, price, link
        self.dresses_list.append(obj)
        self.total_price += price


    def get_dresses_list(self):
        return self.dresses_list


    def add_swimwear_list_to_bag(self,price,obj):
        self.swimwear_list.append(obj)
        self.total_price += price
    def get_swimwear_list(self):
        return self.swimwear_list


    #it must GET object a doc = {'key':valu}...
    def remove_at_swimwear(self,  price, item):
        print("remove_at_swimwear")
        for itm in self.swimwear_list:
            if itm.sku == item['sku'] and itm.color == item['color'] and itm.size == item['size']:
                self.swimwear_list.remove(itm)
                self.total_price -= price
                return True
        return False

    def remove_at_dresses(self, price, item):
        for itm in self.dresses_list:
            if itm.sku == item['sku'] and itm.color == item['color'] and itm.size == item['size']:
                print("removed dresses...")
                self.dresses_list.remove(itm)
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





















