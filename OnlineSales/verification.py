from main import Swimwear, Dresses,Users,Ordering
import pymongo
from pymongo import MongoClient
from pprint import pprint
from flask import Flask, request, url_for, render_template, session, redirect
import os
from dotenv import load_dotenv
from twilio.rest import Client
import secrets

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
as_path = 'home'
items = ['', '', '', '', '', '']
ord = Ordering('123456')
show_active = ord.show_activity(as_path)
active = ord.m_active(as_path)

@app.route('/home/nav')
def open_home():
    return render_template('home.html', len=len(items),
                           list_item=items, color_select=sw.get_color(),
                           show_active=show_active, active=active,replace_btn=False)




user = Users()
@app.route('/')
def navigation():

    if 'user_id' in session:
        if session["user_id"] >= 1000 and len(user.email)>0:
            print("user id is exist")
            return redirect(url_for('open_home'))

        elif session["user_id"] >= 1000:# colud be user closed the website and open,than constractor of user is empty
            user_id = session["user_id"]
            if set_user_with_id(user_id):  # open database to initialize the use
               return redirect(url_for('open_home'))
            else:
                return redirect(url_for('open_home'))
    else:
        print("user id don't exist")
        return redirect(url_for('open_home'))
       # return f'Logged in as {session["user_id"]}'
    #return render_template('home.html',email='',name_user='')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        _email = request.form['email']
        print(_email)
        session["_email"] = _email
        send_verification(_email)
        return render_template('home.html', len=len(items),
                               list_item=items, color_select=sw.get_color(),
                               show_active=show_active, active=active, replace_btn=True)




@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user_id', None)
    return redirect(url_for('navigation'))


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
                                   show_active=show_active, active=active,
                                   replace_btn=True, error=error)
    return  redirect(url_for('navigation'))


def check_verification_token(email, token):
    check = client.verify \
        .services(TWILIO_VERIFY_SERVICE) \
        .verification_checks \
        .create(to=email, code=token)
    return check.status == 'approved'






def get_database():
    client = MongoClient("mongodb+srv://yoniat:your pass server without quotes@websw.dfksw.mongodb.net/?retryWrites=true&w=majority")
    try:
       print(client.server_info())
       return client
    except:
       print('Unable to open server')


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
        user.name_user = get_user['name_user']
    else: #the user not exsit in database
       # go from new doc to old
       id_doc = collection.find().limit(1).sort([('_id', -1)])  # or $natural
       user_id = int(id_doc[0]['_id'])
       user_id+= 1
       print(user_id)
       doc = {"_id":user_id, "name_user":"", "email": email, "mobile": "", "city": "", "address": ""}
       collection.insert_one(doc)
       get_user = collection.find_one({"email": email})
       if get_user!=None:
           # just if user has been verification we initialize to next login
           session['user_id'] = get_user['_id']
           user.email = get_user['email']
           user.name_user = get_user['name_user']


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
          user.name_user = _user['name_user']
          return True
    return False

def set_swimwear():
    client = get_database()
    db = client['DesignerClothes']
    collection = db['swimwear']
    doc = {}
    collection.insert_one(doc)



@app.route('/send/order' ,methods=['GET', 'POST'])
def send_order_to_server():# if there is no name, city, and address tham call fun to ask it
    if request.method == 'POST':
       if 'user_id' in session and len(user.email)>0:
           if session['user_id']!=None:
               pass


       else:
          return redirect(url_for('login'))
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)#host='0.0.0.0', port=5000



