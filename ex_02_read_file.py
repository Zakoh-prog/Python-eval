text = open("nameslist.txt", "r") 
d = dict() 
for line in text: 
    
    line = line.strip() 

    if line in d: 
            
            d[line] = d[line] + 1
    else: 
            
        d[line] = 1
  
    
for key in list(d.keys()): 
    print(key, ":", d[key])