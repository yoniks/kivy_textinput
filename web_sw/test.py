
def create_array():

    mlist = []
    for it in range(0, 5):
        doc = {"_id" : 9 +it ,"name" :"yoni" ,"sku" :"DE777" ,"SIZE": ["S", "M", "L"]}
        mlist.append(doc)
    for it in mlist:
        print(it['_id'], it['SIZE'][0], it.get('sku'))
        for size in it['SIZE']:#next one PRINTS THE TIME HAS IN LIST
            print(size)
        print("next")


create_array()