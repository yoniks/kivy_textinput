


class Parent:

    def __init__(self, sku, price, name_item):
        self.sku = sku
        self.price = price
        self.name_item = name_item
        self.size = []   #('S' ,'M' ,'L')
        self.colors = []
        self.url_img = []


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
   # def set_url_img(self, *args):
    #    if args != None:
     #      self.url_img= args





class Swimwear(Parent):

    def print_sw(self):
        return '\n sku: ' + self.get_sku() +"name:  "+ '\nprice: ' + str(self.get_price())


class Dresses(Parent):

      def print_obj(self):
          return self.url_img


class Discount(Parent):
    def __init__(self, sku, price,name_item, discount_percent):
        super().__init__(sku, price,name_item)
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
        if user_id>1000:
           self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id
    def set_password(self, password):
        self.password = password
        #if email is not exsit in database than  fun create_new_user_id create new id to user
    def set_user(self, email, name_user, user_id,phone ,city, address):
        self.email = email
        self.name_user = name_user
        self.user_id = user_id
        self.city= city
        self.address= address
        self.phone = phone

    def valid_login(self,user,password):
        self.email = user
        self.password = password
        return False

    def log_the_user_in(self,email):
        self.email = email


class Ordering:
    def __init__(self,  order_id):
         self.order_id= order_id
         self.items_of_order = []
         self.total_price = 0
         self.add_it = []

    def get_order_id(self):
     return  self.order_id

    def add_to_cart(self,price, *obj_order):#sku, name_item, size, color, price, link
       # self.items_of_order.append(" "+sku +","+ name_item+","+ size +","+ color +","+ str(price) +","+ str(link))
       self.items_of_order.append(obj_order)
       self.total_price += price

    "'set many argument and cheak if it exists in list'"
    def remove_from_card(self,  price, *remove):
        for itm in self.items_of_order:
            if itm == remove:
              self.items_of_order.remove(remove)
              self.total_price =- price

    def get_total_price(self):
         return self.total_price

    def get_items_of_order(self):
        return self.items_of_order



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








