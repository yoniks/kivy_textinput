class Parent(object):
    def __init__(self, sku, price, size, colors, *url_img):
        self.sku = sku
        self.price = price
        self.size = size   #('S' ,'M' ,'L')
        self.colors = colors
        self.url_img = url_img


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
   # def set_url_img(self, *args):
    #    if args != None:
     #      self.url_img= args





class Swimwear(Parent):
    def __init__(self, sku, price, size, colors, name_sw, *url_img):
        super().__init__(sku, price, size, colors, *url_img)
        self.name_sw = name_sw

    def get_name_sw(self):
        return self.name_sw

    def print_sw(self):
        return '\n sku: ' + self.get_sku() +"name:  "+ self.name_sw + '\nprice: ' + str(self.price)


class Dresses(Parent):
    def __init__(self, sku, price, size, colors, name_dress,*url_img):
        super().__init__(sku, price, size, colors, *url_img)
        self.name_dress = name_dress

    def get_dress(self):
        print(self.name_dress)
        return 'name dress: ' + self.name_dress


class Discount(Parent):
    def __init__(self, sku, price, size, colors, discount_percent,*url_img):
        super().__init__(sku, price, size, colors, *url_img)
        self.discount_percent= discount_percent



class UserLoging:
    def __init__(self, email, name_user,phone):
        self.email = email
        self.name_user = name_user
        self.phone = phone
        # id create when new user is logingUp, id create just one time
        self.user_id = ''

        #if email is not exsit in database than  fun create_new_user_id create new id to user
    def set_user(self, email, name_user, user_id,city, address):
        self.email = email
        self.name_user = name_user
        self.user_id = user_id
        self.city= city
        self.address= address

    def create_new_user_id(self):
        self.user_id = 'S162829141'

    def get_user_id(self):
        return self.user_id

    def pring_user(self):
        return "user register: "+str(self.email)+" "+str(self.name_user)+" "+str(self.user_id)




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



class OrderHistory(UserLoging):
    def __init__(self, order_id, user_id, email, name_user,phone ,order_date, total_price, order_cancel):
        super(OrderHistory, self).__init__(email, name_user, phone)
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







# def main():

alist = []
user = UserLoging('yoni.ch@icloud.com', 'yoni chitrit','052000000')#'052000000'
user.create_new_user_id()
print(user.pring_user())
#sku, price, *url_img, size, colors, name_sw
url = ('http//0','http//2')
sw = Swimwear('CW20001',100,'S','#00000','bikini' ,url)
print(sw.print_sw())

url1 = ('http//2','http//3')
dss = Dresses('CW40001',120,'S','#fffff','stan' ,url1)


add_to = Ordering('123000')
add_to.add_to_cart(sw.price, sw.sku, sw.name_sw,sw.size, sw.colors,sw.price, sw.url_img[0])
add_to.add_to_cart(dss.price, dss.sku,dss.name_dress,dss.size,dss.colors,dss.price,dss.url_img[0])
print("total price: "+ str(add_to.get_total_price()))

add_to.remove_from_card( sw.price, sw.sku, sw.name_sw,sw.size, sw.colors,sw.price, sw.url_img[0])


for items in add_to.get_items_of_order():
    print("order user: "+str(items))


#order_id, user_id, email, name_user, order_date, total_price, order_cancel
send_order = OrderHistory(add_to.order_id, user.user_id, user.email, user.name_user,user.phone,'10/10/2022',
                         add_to.get_total_price(),False)
send_order.set_items_order(add_to.get_items_of_order())

