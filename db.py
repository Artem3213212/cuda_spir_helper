import os
import json

filename_db=os.path.join(os.path.dirname(__file__), 'spirv.core.grammar.json')

def load_db():
    db={}
    db_enums={}
    with open(filename_db,'r') as f:
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
