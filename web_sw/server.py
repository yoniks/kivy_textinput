import flask

from main import Swimwear, Dresses,Users,Ordering
import pymongo
from pymongo import MongoClient
from bson.son import SON
from pprint import pprint
from flask import Flask, request, url_for, render_template, session, redirect,jsonify
import os
from dotenv import load_dotenv
from twilio.rest import Client
import secrets

#session.pop('user_id', None)
load_dotenv()
app = Flask(__name__)
#  Set the secret key to some random bytes. Keep this really secret!
app.secret_key = secrets.token_hex()  # b'_5#y2L"F4Q8z\n\xec]/'
print(app.secret_key)


TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN= os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_VERIFY_SERVICE = os.environ.get('TWILIO_VERIFY_SERVICE')
SENDGRID_API_KEY= os.environ.get('SENDGRID_API_KEY')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)




user = Users()
@app.route('/',methods=['GET','POST'])#add to list
@app.route('/home', methods=['GET','POST'])
def open_home():
    if 'user_id' in session:
        if session["user_id"] >= 11000 and len(user.email) > 0:
            print("user id is exist")
    else:
        pass
    return render_template('Home.html')


"""this class holding the order of items user and delete items """
ord = Ordering()
"""
1)list_dresses_to and list_first_group_dresses_to 
initialize one time from database mongoDB to fill the html.
2)temp_first_group holding some of value- title,sku,one url img, and price
when user click on the img we display all the photos with description
"""
list_dresses_to = []
list_first_group_dresses_to = []
temp_first_group = []
@app.route('/home/dresses/to',methods=['GET','POST'])
def set_dresses():
    print("my email: ",user.email)
    if request.method == 'POST':# user add to cart
        list_dress = request.get_json()
        for it in list_dress:
            
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
            ord.add_dresses_to_bag(temp_price,add_to_cart)
        if len(list_dress)>0:
            return jsonify({'dresses': 'ok'})
        else:
            return jsonify({'dresses': 'error'})
     
    elif len(list_dresses_to) == 0:
         user.email = "yon.ch"
         print("open server to initialize dresses")
         client = get_database()
         db = client['DesignerClothes']
         a_dresses = db['dresses']
         cursor = a_dresses.find({})#bring all Documents
         for it in cursor:
             list_dresses_to.append(it)#add object to list

         b_dresses = db['first_group_dresses']
         cursor = b_dresses.find({})  # bring all Documents

         for it in cursor:
             print("link",it['url_img'][0]['img'][0])
             print(it['sku'],"-",it['title'])
             doc = {"title":it['title'] ,"sku": it['sku'],"url_img":it['url_img'][0]['img'][0],"price":it['price']}
             #print(it['url_img']['color_text'],"-",it['url_img']['color'])
             temp_first_group.append(doc)
             list_first_group_dresses_to.append(it)
    return render_template('Dresses.html', list_dress=list_dresses_to,first_list_dress=temp_first_group)


""" list_swimwear_to 
initialize one time from database mongoDB to fill the html"""
list_swimwear_to = []
temp_list_swimwear_to =[]
@app.route('/home/swimwear/to',methods=['GET','POST'])
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
           # the key of self  kepping on list, we call the function
           ord.add_swimwear_list_to_bag(temp_price, add_to_cart)
           print("price: ",ord.get_total_price())
    elif len(list_swimwear_to)==0:
         client = get_database()
         db = client['DesignerClothes']
         swimwear = db['swimwear']
         cursor = swimwear.find({})  # bring all Documents
         for it in cursor:
             doc = {"title":it['title'] ,"sku": it['sku'],"url_img":it['url_img'][0]['img'][0],"price":it['price']}
             temp_list_swimwear_to.append(doc)
             list_swimwear_to.append(it)
    return render_template('Swimwear.html',list_swimwear=temp_list_swimwear_to)





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
at_list_gallery = []
@app.route('/home/gallery/photos/swimwear/to',methods=['GET','POST'])
def set_gallery_swim():
    if request.method == 'POST':  # user add to cart
       if len(at_list_gallery) > 0:
           at_list_gallery.pop(0)
       sku = request.get_json()
       print('sku swimwear ',sku)
       for it in list_swimwear_to_html:
           if sku == it['sku']:
               at_list_gallery.append(it)
               break
       if len(at_list_gallery)>0:
          return jsonify({'swimwear':'ok'})
       return jsonify({'swimwear':'error'})
    return render_template('GalleryPhotos.html',list_gallery=at_list_gallery)




@app.route('/home/gallery/photos/dresses/to',methods=['GET','POST'])
def set_gallery_dress():
    if request.method == 'POST':  # user add to cart
       if len(at_list_gallery) > 0:
           at_list_gallery.pop(0)
       sku = request.get_json()
       session['id_item'] = sku
       print('sku dress', sku)
       is_group = identifier_item_of_cart(sku)
       if is_group == "group dresses":
          for it in list_first_group_dresses_to:
              if sku == it['sku']:
                 at_list_gallery.append(it)
                 break
       else:
           for it in list_dresses_to:
              if sku == it['sku']:
                 at_list_gallery.append(it)
                 break
       if len(at_list_gallery)>0:
               return jsonify({'dresses':'ok'})
       return jsonify({'dresses':'error'})

    if len(at_list_gallery)==0:#delete after this is if i refresh
        for it in list_first_group_dresses_to:
            if session['id_item'] == it['sku']:
                at_list_gallery.append(it)
                break
    print("set_gallery_dress():____",len(at_list_gallery),"-",session['id_item'])
    return render_template('GalleryPhotos.html',list_gallery=at_list_gallery)


#lest step


@app.route('/home/cart/add/to',methods=['GET','POST'])
def set_cart():
    #the list of swimwear and Dresses snding to cart when click on it
    # user can delete item at cart page and we upData with property
    # class of Ordering
    for at in ord.get_dresses_list():
        print(at)
    if request.method == 'POST':  # user add to cart
        pass
    if len(ord.get_dresses_list()) > 0:
        pass
    if len(ord.get_swimwear_list()) > 0:
        pass
    return render_template('Cart.html',dresses=ord.get_dresses_list(),swimwear=ord.get_swimwear_list())

############




@app.route('/7777/send/order/to/server')
def send_order_to_database():
    #1 we check if user made login
    #2 we create uniq id order
    #3 we send the order
   
    if 'user_id' in session:
        if session["user_id"] < 10000 or len(user.email) == 0:
           print('user must verify before the order sent to server')
           #print some msg to user
        else:
          client = get_database()
          db = client['orders']
          items = db['items']
         

          if len(ord.get_dresses_list())>0 or len(ord.get_swimwear_list())>0: #or len(ord.rent_list)>0:
             if ord.get_order_id() == 0:
                uniq_id = 0
                u_id = items.find().limit(1).sort([('_id', -1)])
                uniq_id = int(u_id[0]['_id'])
                uniq_id += 1
                ord.set_order_id(uniq_id)
                print('order:', ord.get_order_id(),' sent')
                if uniq_id > int(u_id[0]['_id']):#up to dataBase
                   set_to_dress = []
                   set_to_swimwear = []
                   set_to_rent = []
                   for o in ord.get_dresses_list():# just with class of Ordring we add or remove  object,
                       set_to_dress.append({"sku":o.sku,"title":o.title,"descript":o.descript,"size":o.size,"color":o.color,
                                             "url_img":o.url_img,"available_stock":o.available_stock,
                                             "counter":o.counter,"price":o.price,"is_cancel":ord.get_is_cancel()})

                   items.insert_one({'_id':ord.get_order_id(),'user_id':session["user_id"],'email':user.email,
                                 'list_dress':set_to_dress,
                                  'list_swimwear':set_to_swimwear,
                                  'list_rent':set_to_rent,
                                 'total_price':ord.get_total_price()})
    return render_template('Home.html')





#verify Email
@app.route('/login/verify', methods=['GET','POST'])
def login():
    # _email = request.form['email']
    if request.method == 'POST':
        _email = request.get_json()
        print("email", _email)
        session["_email"] = _email
        is_valid = send_verification(_email)
        if is_valid:
           return jsonify({'status': 'ok'})
        else:
            return jsonify({'status': 'error'})

    return redirect(url_for('open_home'))


def send_verification(to_email):
    verification = client.verify.services(TWILIO_VERIFY_SERVICE).verifications.create(to=to_email, channel='email')
    print("send ", verification.sid, "-- ", verification)
    if verification.sid:
        return True
    else:
        return False





@app.route('/pass/verify', methods=['GET', 'POST'])
def generate_verification_code():
    if "user_id" in session and request.method == 'POST':#Email already verified
        return jsonify({'status': 'verified'})
       # return redirect(url_for('open_home'))
    elif request.method == 'POST':
        _email = session['_email']
       # verification_code = request.form['verificationcode']
        verification_code = request.get_json()
        print("pass", verification_code)
        if check_verification_token(_email, verification_code):# if verification return true
            set_user(_email)#check if is it new user or not and initialize the constractor of usr
            print("email proved")
            return jsonify({'status': 'ok'})
        else:
            error = "Invalid verification code. Please try again."
            return jsonify({'status': error})

    return redirect(url_for('open_home'))


def check_verification_token(email, token):
    check = client.verify \
        .services(TWILIO_VERIFY_SERVICE) \
        .verification_checks \
        .create(to=email, code=token)
    return check.status == 'approved'








def get_database():
    client = MongoClient("mongodb+srv://yoniat:###@websw.dfksw.mongodb.net/?retryWrites=true&w=majority")
    try:
       print(client.server_info())
       return client
    except:
       print('Unable to open server')


def set_user(email):

 if len(email) > 0 and len(user.email) == 0:
     client = get_database()
     session['user_id'] = None
     db = client["Users"]
     collection = db["user"]
     get_user = collection.find_one({"email":email})
     if get_user!=None:
        print("user is registered")
        session['user_id'] = get_user['_id']#from database
        user.email = get_user['email']
        user.name_user = get_user['name']
     else: #the user not exsit in database
       # go from new doc to old
       id_doc = collection.find().limit(1).sort([('_id', -1)])  # or $natural
       user_id = int(id_doc[0]['_id'])
       user_id+= 1
       print(user_id)
       doc = {"_id":user_id, "name":"", "email": email, "mobile": "", "city": "", "address": ""}
       collection.insert_one(doc)
       get_user = collection.find_one({"email": email})
       if get_user != None:
           # if user has been verification to email we initialize theire data from server
          session['user_id'] = get_user['_id']
          user.email = get_user['email']
          user.name_user = get_user['name']
 else:
    return False


def set_user_with_id():
    if 'user_id' in session:
       user_id = session['user_id']
       print('set_user_with_id')
       client = get_database()
       db = client["Users"]
       users = db["user"]
       _user = users.find_one({"_id":user_id})
       if _user!=None:
          if len(_user['email']) > 0 and _user['_id']>0:#must return str and int and >1000
             session['user_id'] = _user['_id']#from database
             user.email = _user['email']
             user.name_user = _user['name']
             return True
    return False




"""
if user remove item from cart i must updata the list but this function return the 
name of list to search, (group dresses,dresses,swimwear) by sku we defined.  
"""
def identifier_item_of_cart(sku):
    if sku.isdigit():
       return "Error"
    else:
        digit = ''
        text = ''
        for at in sku:
            if at.isdigit():
               digit += at
            else:
               text += at
        print(text, "-", int(digit))
        if int(digit) >= 22000 and  int(digit) <= 22200:
            return "group dresses"
        elif int(digit) >= 22201 and int(digit) <= 22251:
            return "dresses"
        elif int(digit) >= 33000 and int(digit) <= 33200:
            return "swimwear"







if __name__ == "__main__":
    app.debug = True
    app.run(port=5500)#host='0r().0.0.0', port=5000






