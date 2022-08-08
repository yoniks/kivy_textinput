



class Parent:
# this class extends to dresses and swimwear and we user it to add items of users,
#we not use it to aet from server becouse size and color must be list.
    def __init__(self):
        self.sku = ''
        self.title = ''
        self.descript = ''
        self.size = 'size'   #('S' ,'M' ,'L')
        self.color = 'color'
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
    def __init__(self):
         self.order_id= 0
         self.swimwear_list = []
         self.dresses_list = []
         self.rent_list = []
         self.total_price = 0
         self.is_cancel = False


    def get_is_cancel(self):
        return self.is_cancel
    def set_is_cancel(self,cancel):
        self.is_cancel=cancel
        
    def set_order_id(self,ID):
        self.order_id = ID

    def get_order_id(self):
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

    "'set many argument and cheak if it exists in list'"
    #i must send object doc = {'key':valu}
    def remove_at_swimwear(self,  price, item):
        for itm in self.swimwear_list:
            if itm.sku == item.sku and itm.color == item.color:
              self.swimwear_list.remove(item)
              self.total_price =- price

    def remove_at_dresses(self, price, item):
        for itm in self.dresses_list:
            if itm.sku == item.sku and itm.color == item.color:
                self.dresses_list.remove(item)
                self.total_price = - price
    def get_total_price(self):
         return self.total_price






class OrderHistory:
    def __init__(self, order_id, user_id, email, name_user,phone ,order_date, total_price, is_all_order_cancel):
        self.email = email
        self.name_user = name_user
        self.phone = phone
        self.order_id = order_id
        self.order_date = order_date
        self.total_price = total_price
        self.order_cancel = is_all_order_cancel
        self.user_id = user_id




















