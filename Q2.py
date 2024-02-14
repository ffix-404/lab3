x=[1,23,4,5,6,7,8,9,99,0,-101,99.1,1]
max=x[0]
for y in x[1:]:
   if y > max:
     max=y
    
print(f"the largest number in the list is={max}")  