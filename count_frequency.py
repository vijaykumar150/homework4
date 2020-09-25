def freq(mylist): 
  
    mylist = mylist.split()          
    str = [] 
  
    for i in mylist:              
  
        
        if i not in str: 
  
            str.append(i)  
              
    for i in range(0, len(str)): 
  
             print( str[i], ':', mylist.count(str[i]), end=' ')     
  
def main(): 
    mylist = 'one two eleven one three two eleven three seven eleven'
    freq(mylist)                     
  
if __name__=="__main__": 
    main()   