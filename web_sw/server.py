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





def initialize_swimwear_to_server():
    client = get_database()
    db = client['DesignerClothes']
    collection = db['dresses']
    dress =  collection.find_one({"sku":"DR777"})
    print(dress)



user = Users()
ord = Ordering(0)#hold the active and lists of items we inialize num order when user
@app.route('/')#add to list
@app.route('/home')
def open_home():

    if 'user_id' in session:
        if session["user_id"] >= 1000 and len(user.email) > 0:
            print("user id is exist")
    else:
        print("user id don't exist")
       # initialize_dress_to_server()

    return render_template('home.html')

list_dresses_to_html = []
 #Ordering() is contain few list of items
@app.route('/home/dresses/to')
@app.route('/home/dresses/to',methods=['POST'])
def open_dress():
    if request.method == 'POST':# user add to cart
        list_dress = request.get_json()#sent from js if user add
        if ord.order_id==0:
            ord.order_id = get_id_order()#it bring from server new order id by sort
        for it in list_dress:
            add_to_cart = Dresses() #obj of dresses must be created every new initialize
            add_to_cart.title = it['title']#initialize obj
            add_to_cart.descript = it['descript']
            ord.dresses_list.append(add_to_cart)
            print(it['sku'])
    elif len(list_dresses_to_html)==0:
         print("open server to bring dresses")
         client = get_database()
         db = client['DesignerClothes']
         dresses = db['dresses']
         cursor = dresses.find({})#bring all Documents
         print('cursor', cursor)
         for it in cursor:
             print('it',it)
             list_dresses_to_html.append(it)#add object to list

    return render_template('Dresses.html', list_dress=list_dresses_to_html)#list of list and object


link_img = ['https://res.cloudinary.com/clouster/image/upload/v1658824154/website_clothes/Dresses/DR1002_BLACK_zwlgwe.png',
            'https://res.cloudinary.com/clouster/image/upload/v1658824154/website_clothes/Dresses/DR1002_GREEN_kcdnpm.png']


def initialize_dress_to_server():
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

def get_id_order():#create new id order to each user
    client = get_database()
    db = client['history_orders']
    new_id = db['orders']
    id_doc = new_id.find().limit(1).sort([('order_id', -1)])  # or $natural
    mid  = int(id_doc[0]['order_id'])
    return mid+1

@app.route('/home/swimwear/to')
def open_swimwear():
    return render_template('swimwear.html')




@app.route('/login/verify', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        _email = request.get_json() # _email = request.form['email']
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








@app.route('/send/order' ,methods=['POST'])
def send_order_to_server():# if there is no name, city, and address tham call fun to ask it
    if request.method == 'POST':
       if 'user_id' in session:
         if session["user_id"] >= 1000 and len(user.email)==0:  # send it
           user_id = session["user_id"]
           if set_user_with_id():  # open database to initialize the use
               print("send the order", user.email)
           return redirect(url_for('open_home'))
       elif session["user_id"] >= 1000 and len(user.email) >0:
            print("send to order")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)#host='0.0.0.0', port=5000






