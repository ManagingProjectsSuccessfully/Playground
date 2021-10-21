file = 'README.md'
 
with open(file,'r',encoding='utf-8') as fin:
    lines = list(fin)
new_lines = []
for l in lines:
    if l.startswith("<<<<<<<") or l.startswith("=======") or l.startswith(">>>>>>>"):
        pass
    else:
        new_lines.append(l)
        
with open(file,'w',encoding='utf-8') as fout:
    fout.writelines(new_lines)
    
    
print('ENTE')