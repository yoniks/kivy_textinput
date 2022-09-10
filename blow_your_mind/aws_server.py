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
def encryption_data(_card,id_order ):
    """
     const doc_credit_card = {"id_order":0,"name":Name.value,"name_card":name_card,"number_card":number_card.value,
        "exp_month":exp_month.value,"exp_year":exp_year.value,"cvv":cvv.value }
    """
    if os.path.exists(path)==False:
       print("create key")
       create_master_key_to_encry()
       return ""

    with open(path, "r+b") as r:  # w+b
         master_key = r.read()
         if len(master_key)>0:
            to_encry = Fernet(master_key)
            data_private =_card['name']+"-"+ _card['name_card']+"-"+_card['number_card']\
                          +"-"+_card['exp_month']+"-"+_card['exp_year']+"-"+_card['cvv']
            print("credit card to encryption: \n",data_private)
            token = to_encry.encrypt(data_private.encode('ascii'))
            global create_id_order_as_name_file
            create_id_order_as_name_file = f"{id_order}"+".txt"
            with open(create_id_order_as_name_file, "w+b") as f:  # w+b
                 f.write(token)
            print("in the file: ", create_id_order_as_name_file,", \n " ,"text encrypted \n", token)
            return create_id_order_as_name_file
         else:
             print("there is no master key")



def upload_data(path):#region='eu-central-1'
    path = f"{path}"+".pdf"
    if os.path.exists(path):
       S3 = boto3.client('s3',aws_access_key_id = os.environ.get('Access_key_ID_write'),
       aws_secret_access_key = os.environ.get('Secret_access_key_write'))
       S3.upload_file(Filename=path, Bucket='savingmycrditcard', Key=path)
       print("upload name file ", path)
       return True
    else:
       print("field to send...")
       return False

    #S3.download_file('savingmycrditcard', path, "user0_download.py")




def get_data_to_upload(credit_card,id_order ):
    """my data to encryption"""
    id_order_as_name_file = encryption_data(credit_card,id_order)
    if len(id_order_as_name_file) > 0:
       upload_data(id_order_as_name_file)
       if os.path.exists(id_order_as_name_file):
          os.remove(id_order_as_name_file)
          return True
    else:
        return False
        #print("created master key please try again!")
        #create_master_key_to_encry()










   

"""
    with open(path, "r+b") as r:  # w+b
        master_key = r.read()
    with open(id_order_as_name_file, "r+b") as id_:
        token = id_.read()
        # print("read token to dec",type(token), token)
"""







def create_key():
   file_bytes = os.urandom(96)
   print(file_bytes[0])
   print(file_bytes, type(file_bytes))
   make_number = base64.b64encode(file_bytes)
   print(make_number)
   #for by in make_number:
   #   print(by, type(by))# make every char to decimal
   make_number = base64.b64decode(make_number)
   print(make_number)


   text = "yoni"
   result = text.encode('ascii')#binary same char
   enc_text = base64.b64encode(result)#binary convert 8 to 6
   print(enc_text)

   res = enc_text.decode('ascii')#convert str
   print(res)
   res2 = base64.b64decode(res)# 6 to 8 bits
   print(res2, res2.decode('ascii'))


#for bucket in s3.buckets.all():
#    print(bucket.name) b'qxMf b'\xab'

#s3 = boto3.resource('s3')
    #s3.meta.client.download_file('savingmycrditcard',name_file_to, name_file_to)
"""
file_bytes = os.urandom(96)
result = base64.b64encode(file_bytes)#
result =result.decode('ascii')
print(type(result))
"""
