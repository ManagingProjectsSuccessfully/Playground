file = 'README.md'
 
with open(file,'r',encoding='utf-8') as fin:
    lines = list(fin)
new_lines = []
merge_area = False
for l in lines:
    if l.startswith("<<<<<<<") or l.startswith("=======") or l.startswith(">>>>>>>"):
        merge_area = True
    else:
        if merge_area:
            if l.strip():
                new_lines.append(l)
        else:
            new_lines.append(l)
        
with open(file,'w',encoding='utf-8') as fout:
    fout.writelines(new_lines)
    
    
print('ENTE')