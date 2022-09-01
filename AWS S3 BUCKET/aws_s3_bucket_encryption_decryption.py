import boto3
import os
import time
import base64
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
load_dotenv()
# Let's use Amazon S3
"""
s3 = boto3.resource('s3')
s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')
"""



path = 'master_key.txt'
def create_master_key_to_encry():
    file_bytes = os.urandom(32)
    print(type(file_bytes), file_bytes)
    result = base64.b64encode(file_bytes)#
    #result = result.decode('ascii')
    print(type(result),result)
    with open(path, "w+b") as f:  # w+b
        f.write(result)


"""read master key encryption data and create id_order to name file than save text in file"""
def encryption_data(credit_card):

    if os.path.exists(path)==False:
       print("create key")
       create_master_key_to_encry()
       return ""

    with open(path, "r+b") as r:  # w+b
         master_key = r.read()
         if len(master_key)>0:
            #print(type(master_key), master_key)
            to_encry = Fernet(master_key)
            my_data_private =credit_card['name']+"-"+credit_card['number']+"-"+credit_card['month']+"-"+credit_card['year']
            print("credit card to encryption: \n",my_data_private)
            token = to_encry.encrypt(my_data_private.encode('ascii'))
            id_order = int(time.time())
            id_order = str(id_order)
            create_id_order_as_name_file = f"{id_order}"+".txt"
            with open(create_id_order_as_name_file, "w+b") as f:  # w+b
                 f.write(token)
            print("in the file: ", create_id_order_as_name_file,", \n " ,"text encrypted \n", token)
            return create_id_order_as_name_file

def decryption_data(token, master_key,name_file):
    to_encry = Fernet(master_key)
    decryption_data = to_encry.decrypt(token)
    print("decrypt: ", decryption_data.decode('ascii'))
    with open(name_file, "w+") as f:#w+b
        data_str = decryption_data.decode('ascii')
        f.write(f'"{data_str}"')
    with open(name_file, "r") as r:  # w+b
        data_str = r.read()
    split_data = data_str.split("-")
    if len(split_data) > 0:
       credit_card = {"name": split_data[0], "number": split_data[1], "month": split_data[2], "year": split_data[3]}
       print(credit_card)



def upload_data(path):#region='eu-central-1'
    S3 = boto3.client('s3',aws_access_key_id = os.environ.get('Access_key_ID_write'),
    aws_secret_access_key = os.environ.get('Secret_access_key_write'))
    S3.upload_file(path, 'savingmycrditcard', path)
    print("upload name file ", path)

    #S3.download_file('savingmycrditcard', path, "user0_download.py")


def download_data(id_order_as_name_file):
    s3 = boto3.client('s3', aws_access_key_id=os.environ.get('Access_key_ID_raed'),
                      aws_secret_access_key=os.environ.get('Secret_access_key_read'))
    s3.download_file('savingmycrditcard', id_order_as_name_file, id_order_as_name_file)



def try_upload_data_without_permission(id_order_as_name_file):
    s3 = boto3.client('s3',aws_access_key_id = os.environ.get('Access_key_ID_write'),
    aws_secret_access_key = os.environ.get('Secret_access_key_write'))
    s3.download_file('savingmycrditcard', id_order_as_name_file, id_order_as_name_file)

def get_data_to_upload():
    """my data to encryption"""
    credit_card = {"name": "yoni chitrit", "number": "0000103310920000", "month": "08", "year": "2026"}
    id_order_as_name_file = encryption_data(credit_card)
    if len(id_order_as_name_file) > 0:
       upload_data(id_order_as_name_file)
       if os.path.exists(id_order_as_name_file):
          os.remove(id_order_as_name_file)
    else:
        print("created master key please try again!")
        create_master_key_to_encry()


def set_id_order_to_download(id_order_as_name_file):

    if os.path.exists(id_order_as_name_file):
        with open(path, "r+b") as r:  # w+b
            master_key = r.read()
        with open(id_order_as_name_file, "r+b") as id_:
            token = id_.read()
            if len(token) > 90:
                print("file decrypted")
                decryption_data(token, master_key, id_order_as_name_file)
            else:
                print("file already decrypted")
        # print("read token to dec",type(token), token)

    else:
         download_data(id_order_as_name_file)
         #try_upload_data_without_permission(id_order_as_name_file)



#get_data_to_upload()
set_id_order_to_download("1661932063.txt")







