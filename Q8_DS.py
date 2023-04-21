def paraCheck( seq ):  
   while True:  
       if '()' in seq :  
           seq = seq.replace ( '()' , '' )  
       elif '{}' in seq :  
           seq = seq.replace ( '{}' , '' )  
       elif '[]' in seq :  
           seq = seq.replace ( '[]' , '' )  
       else :  
           return not seq  
  
value = '{[()]}'  
print(f'{value}  : {paraCheck(value)}')  
value1 = '{[()]}{]{}}'  
print(f'{value1}  : {paraCheck (value1)}')