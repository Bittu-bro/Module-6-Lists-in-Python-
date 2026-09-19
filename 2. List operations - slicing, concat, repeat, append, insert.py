#slicing
l1 = [1,2,3,4,5,6,7,8,9,10]
fun1 = l1[::2]
fun2 = l1[1::2]
#print(f"{fun1}\n{fun2}")

#adding
l2 = [11,12,13,14,15]
fun3 = [l1 + l2]
fun4 = [l2 + l1]
#print(f"{fun3}\n{fun4}")

#repeating
fun5 = l2*2
#print(fun5)

#append
  #l1
#l1.append(l2)
#l1.append(l1[::2])
#l1.append(l1[1::2])
#print(l1)


  #l2
#l2.append(l1)
#l2.append(l2[::2])
#l2.append(l2[1::2])
#print(l2)

#add some element whose doesn't exist in the l1 & l2 
#l1.append(20)
#l2.append(16)

#print(f"{l1}\n{l2}")


#insert(index always start with zero)
l1.insert(4, 50)
print(l1)