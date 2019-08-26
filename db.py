import os
import json

filename_db=os.path.join(os.path.dirname(__file__), 'spirv.core.grammar.json')

def load_db(fn):
    db={}
    db_enums={}

    with open(fn,'r') as f:
        json_db=json.loads(f.read())

    try:
        for i in json_db['instructions']:
            db[i['opname']] = [i0['kind'] for i0 in i.get('operands',[])]
    except:
        pass

    try:
        for i in json_db['operand_kinds']:
            db_enums[i['kind']] = [i0['enumerant'] for i0 in i.get('enumerants',[])]
    except:
        pass

    return db,db_enums

db,db_enums=load_db(filename_db)
