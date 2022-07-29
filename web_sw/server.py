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




def initialize_dress_to_server():
    link_img = [
        'https://res.cloudinary.com/clouster/image/upload/v1658824154/website_clothes/Dresses/DR1002_BLACK_zwlgwe.png',
        'https://res.cloudinary.com/clouster/image/upload/v1658824154/website_clothes/Dresses/DR1002_GREEN_kcdnpm.png']
    client = get_database()
    db = client['DesignerClothes']
    dresses = db['dresses']
    #for it in range(0, 6):  # 0,1,2,3,4,5
    doc = {"_id": 7001 , "sku":'DR10030', "title": "Women Mini Dresses"
            , "descript": 'Women Mini Dresses Summer  Beach Dresses For '
                          'Womens Solid Neck Party Female Short Sleeve Loose Dress',
               "sizes": ["S", "M",'L'],
               "colors": ["Black", "Green"],
               "url_img": link_img,
               "available_stock": True, "price": 70}
    print('is_insert',dresses.insert_one(doc).inserted_id)

def initialize_swimwear_to_server():
    client = get_database()
    db = client['DesignerClothes']
    collection = db['dresses']
    dress =  collection.find_one({"sku":"DR777"})
    print(dress)



user = Users()
@app.route('/',methods=['GET','POST'])#add to list
@app.route('/home', methods=['GET','POST'])
def open_home():
    if 'user_id' in session:
        if session["user_id"] >= 11000 and len(user.email) > 0:
            print("user id is exist")
    else:
        session["user_id"] = 11000
        user.email = 'yoni.ch@icloud.com'
        print("user id don't exist")
       # initialize_dress_to_server()
    return render_template('Home.html')

ord = Ordering()#hold the active and lists of items we inialize num order when user
list_dresses_to_html = [] #one time is inialize the list item
 #Ordering() is contain few list of items
@app.route('/home/dresses/to')
@app.route('/home/dresses/to',methods=['POST'])
def open_dress():
    if request.method == 'POST':# user add to cart
        list_dress = request.get_json()#sent from js if user add
        for it in list_dress:
            add_to_cart = Dresses() #obj of dresses must be created every new initialize
            add_to_cart.title = it['title']#initialize obj
            add_to_cart.descript = it['descript']
            add_to_cart.sku = it['sku']
            add_to_cart.size = it['size']
            add_to_cart.color = it['color']
            add_to_cart.price = int(it['price'])
            add_to_cart.counter = int(it['counter'])
            add_to_cart.url_img = it['url_img']
            temp_price= add_to_cart.price * add_to_cart.counter
            ord.add_dresses_to_bag(temp_price,add_to_cart)#the key of self  kepping on list, we call the function

        for itm in ord.get_dresses_list():#it is instans of class, not object
            print('item',type(itm))

        if len(ord.get_dresses_list()) >= 2:
            return redirect(url_for('send_order_to_database'))

    elif len(list_dresses_to_html) == 0:
         print("open server to initialize dresses")
         client = get_database()
         db = client['DesignerClothes']
         dresses = db['dresses']
         cursor = dresses.find({})#bring all Documents
         for it in cursor:
             list_dresses_to_html.append(it)#add object to list
    return render_template('Dresses.html', list_dress=list_dresses_to_html)#list of list and object


@app.route('/7777/send/order/to/server')
def send_order_to_database():
    #1 we check if user made login
    #2 we create uniq id order
    #3 we send the order
    session['user_id'] = 11000
    user.email = 'yoni.ch@icloud.com'
    print('send order to')
    if 'user_id' in session:
        if session["user_id"] < 10000 or len(user.email) == 0:
           print('user must verify before the order sent to server')
           #print some msg to user
        else:
          client = get_database()
          db = client['orders']
          items = db['items']
          #Cursor = items.find({})
         # if list(Cursor)==0:

          if len(ord.get_dresses_list())>0 or len(ord.get_swimwear_list())>0: #or len(ord.rent_list)>0:
             if ord.get_order_id() == 0:
                uniq_id = 0
                u_id = items.find().limit(1).sort([('_id', -1)])
                uniq_id = int(u_id[0]['_id'])
                uniq_id += 1
                ord.set_order_id(uniq_id)
                print('order sent', ord.get_order_id())
                if uniq_id > int(u_id[0]['_id']):#up to dataBase
                   set_to_dress = []
                   set_to_swimwear = []
                   for o in ord.get_dresses_list():# just with class of Ordring we add or remove  object,
                       set_to_dress.append({"sku":o.sku,"title":o.title,"descript":o.descript,"size":o.size,"color":o.color,
                                             "url_img":o.url_img,"available_stock":True,
                                             "counter":o.counter,"price":o.price})

                   items.insert_one({'_id':ord.get_order_id(),'user_id':session["user_id"],'email':user.email,
                                 'list_dress':set_to_dress,
                                  'list_swimwear':set_to_swimwear,
                                 'total_price':ord.get_total_price()})
    return render_template('Home.html')









@app.route('/home/swimwear/to')
def open_swimwear():
    return render_template('Swimwear.html')




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
    _email = session['_email']
    if request.method == 'POST':
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
    client = MongoClient("mongodb+srv://yoniat:id@websw.dfksw.mongodb.net/?retryWrites=true&w=majority")
    try:
       print(client.server_info())
       return client
    except:
       print('Unable to open server')


def set_user(email):
 if len(email)>0 and len(user.email)==0:
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
       if get_user!=None:
           # if user has been verification to email we initialize theire data from server
           session['user_id'] = get_user['_id']
           user.email = get_user['email']
           user.name_user = get_user['name']


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











if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)#host='0.0.0.0', port=5000








