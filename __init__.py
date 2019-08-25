import os
from cudatext import *
from .db import *

SPACES = ['\f','\n','\r','\t','\v',' ']

class Command:
    
    def on_complete(self,ed_self):
        carets=ed_self.get_carets()
        if len(carets)==1:
            x1,y1,x2,y2=carets[0]
            if x2==-1 and y2==-1:
                curr_line=ed_self.get_text_line(y1)[:x1]
                tokens=curr_line.split()
                if len(curr_line)>0 and curr_line[-1] in SPACES:
                    begin=''
                else:
                    begin=tokens[-1]
                    tokens=tokens[:-1]
                if len(begin)>0 and begin[0]=='%':
                    to_complete=[]
                    for i in ed_self.get_text_all().splitlines():
                        t=i.split()
                        if len(t)>0:
                            curr=i.split()[0]
                            if curr.startswith(begin):
                                to_complete.append('var|'+curr+'|')
                    if to_complete:
                        ed_self.complete('\n'.join(to_complete),len(begin),0)
                        return True
                if len(tokens)>1 and tokens[1]=='=':
                    tokens=tokens[2:]
                if len(tokens)==0 and (begin.startswith('Op') or begin=='O'):
                    to_complete=[]
                    for i in db.keys():
                        if i.startswith(begin):
                            to_complete.append('Op|'+i+'|')
                    if to_complete:
                        ed_self.complete('\n'.join(to_complete),len(begin),0)
                        return True
                if tokens:
                    to_complete=[]
                    try:
                        enum_name=db[tokens[0]][len(tokens)-1]
                        for i in db_enums[enum_name]:
                            if i.startswith(begin):
                                to_complete.append(enum_name+'|'+i+'|')
                    except:
                        pass
                    if to_complete:
                        ed_self.complete('\n'.join(to_complete),len(begin),0)
                        return True
