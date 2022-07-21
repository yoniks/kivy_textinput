from main import Swimwear, Dresses,Users,Ordering
import pymongo
from pymongo import MongoClient
from pprint import pprint
from flask import Flask, request, url_for, render_template, session, redirect
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

sw = Swimwear()
user = Users()
items = ['', '', '', '', '', '']
ord = Ordering('123456')







@app.route('/')
@app.route('/home')
def open_home():
    ord.set_show_active('home')
    ord.set_active('home')
    if 'user_id' in session:
        if session["user_id"] >= 1000 and len(user.email) > 0:
            print("user id is exist")
    else:
        print("user id don't exist")
    return render_template('home.html', len=len(items),
                           list_item=items, color_select=sw.get_color(),
                           show_active=ord.get_show_active(), active=ord.get_active(),replace_btn=False)


dress_obj = Dresses()
@app.route('/home/nav/dress')
@app.route('/home/nav/dress',methods=['POST'])#
def open_dress():
    ord.set_show_active('Dresses')  # Dresses
    ord.set_active('Dresses')
    if request.method == 'POST':
        list_item = request.get_json()
        #print(list_item)
        for it in list_item:
            print(it['name'])
    else:
       print("open dress")

       if len(ord.dresses_list)==0:
           print("dress_list is empty so have to download from server")
           list_sku = ['DR0777','DR0778','DR0779','DR0780','DR0781','DR0782']
           for i in range(0, 6):
               dress_obj = Dresses()#create another objrct for next initialize don't affect on last one (similar pointer)
               print(list_sku[i])
               dress_obj.sku = list_sku[i]
               ord.dresses_list.append(dress_obj)
       else:
           print("you can send the data to html", ord.dresses_list[0].sku)
    return render_template('home.html', list_items=ord.dresses_list,
                           show_active=ord.get_show_active(), active=ord.get_active(), replace_btn=False)


@app.route('/home/nav/swimwear')
def open_swimwear():
    ord.set_show_active('Swimwear')
    ord.set_active('Swimwear')
    return render_template('home.html', len=len(items),
                           list_item=items, color_select=sw.get_color(),
                           show_active=ord.get_show_active(), active=ord.get_active(), replace_btn=False)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        _email = request.form['email']
        print(_email)
        session["_email"] = _email
        send_verification(_email)
        return render_template('home.html', len=len(items),
                               list_item=items, color_select=sw.get_color(),
                               show_active=ord.get_show_active(), active=ord.get_active(), replace_btn=True)
    return redirect(url_for('open_home'))


def send_verification(to_email):
    verification = client.verify.services(TWILIO_VERIFY_SERVICE).verifications.create(to=to_email, channel='email')
    print("send", verification.sid)



@app.route('/send_pass', methods=['GET', 'POST'])
def generate_verification_code():
    _email = session['_email']
    global error
    if request.method == 'POST':
        verification_code = request.form['verificationcode']
        if check_verification_token(_email, verification_code):# if verification return true
            set_user(_email)#check if is it new user or not and initialize the constractor of usr
            print("email proved")
            return redirect(url_for('open_home'))

        else:
            error = "Invalid verification code. Please try again."
            return render_template('home.html', len=len(items),
                                   list_item=items, color_select=sw.get_color(),
                                   show_active=ord.get_show_active(), active=ord.get_active(),
                                   replace_btn=True, error=error)
    return  redirect(url_for('navigation'))


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

def updata_my_email():
    list_u = []
    client = get_database()
    db = client["Users"]
    collection = db["user"]
    doc = {"_id": 10000, "name": "yoni chitrit", "email": "@icloud.com", "mobile": "", "city": "", "address": ""}
    collection.insert_one(doc)
    get_user = collection.find_one({"email": "yoni.ch@icloud.com"})
    user.email = get_user['email']
    list_u.append(user)
    for it in list_u:
        print("my email", it.email)


def set_user(email):
 if len(email)>0:
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
           # just if user has been verification we initialize to next login
           session['user_id'] = get_user['_id']
           user.email = get_user['email']
           user.name_user = get_user['name']


def set_user_with_id(user_id):
    print('set_user_with_id')
    client = get_database()
    db = client["Users"]
    collection = db["user"]
    _user = collection.find_one({"_id":user_id})
    if _user!=None:
       if len(_user['email']) > 0 and _user['_id']>0:#must return str and int and >1000
          session['user_id'] = _user['_id']#from database
          user.email = _user['email']
          user.name_user = _user['name']
          return True
    return False




def set_swimwear():
    client = get_database()
    db = client['DesignerClothes']
    collection = db['swimwear']
    doc = {}
    collection.insert_one(doc)



@app.route('/send/order' ,methods=['POST'])
def send_order_to_server():# if there is no name, city, and address tham call fun to ask it
    if request.method == 'POST':
       if 'user_id' in session:
         if session["user_id"] >= 1000 and len(user.email)==0:  # send it
           user_id = session["user_id"]
           if set_user_with_id(user_id):  # open database to initialize the use
               print("send the order", user.email)
           return redirect(url_for('open_home'))
       elif session["user_id"] >= 1000 and len(user.email) >0:
            print("send to order")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)#host='0.0.0.0', port=5000






