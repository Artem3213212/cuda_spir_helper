import json

def load_db(filename):
    db={}
    db_enums={}
    with open(filename,'r') as f:
        json_db=json.loads(f.read())
    for i in json_db['instructions']:
        itm=[]
        try:
            for i0 in i['operands']:
                itm.append(i0['kind'])
        except:
            pass
        db[i['opname']]=itm
    for i in json_db['operand_kinds']:
        itm=[]
        try:
            for i0 in i['enumerants']:
                itm.append(i0['enumerant'])
        except:
            pass
        db_enums[i['kind']]=itm
    return db,db_enums
