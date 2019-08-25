import os
import json

filename_db=os.path.join(os.path.dirname(__file__), 'spirv.core.grammar.json')

def load_db(fn):
    db={}
    db_enums={}
    with open(fn,'r') as f:
        json_db=json.loads(f.read())
    for i in json_db.get('instructions',[]):
        itm=[]
        for i0 in i.get('operands',[]):
            itm.append(i0['kind'])
        db[i['opname']]=itm
    for i in json_db.get('operand_kinds',[]):
        itm=[]
        for i0 in i.get('enumerants',[]):
            itm.append(i0['enumerant'])
        db_enums[i['kind']]=itm
    return db,db_enums

db,db_enums=load_db(filename_db)
