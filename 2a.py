dict={'1':['a','b'],'2':['c','d']}
for i in dict['1']:
    for j in dict['1']:
        print(i,j)
for i in dict['2']:
    for j in dict['2']:
        print(i,j)
for i in dict['1']:
    for j in dict['2']:
        print(i,j)        
for i in dict['2']:
    for j in dict['1']:
        print(i,j)        
