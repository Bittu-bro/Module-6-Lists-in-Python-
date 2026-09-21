#lists
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [11,12,13,14,15]



#for slicing
fun1 = l1[::2]
fun2 = l1[1::2]
fun3 = l2[::2]
fun4 = l2[1::2]
#print(f"{fun1}\n{fun2}")
#print(f"{fun3}\n{fun4}")


#for adding
fun5 = [l1 + l2]
fun6 = [l2 + l1]
#print(f"{fun5}\n{fun6}")



#for repeating
fun7 = l1*2
fun8 = l2*2
#print(fun7)
#print(fun8)

#for append

  #l1
# l1.append(l2)
# l1.append(l1[::2])
# l1.append(l1[1::2])
#print(l1)


  #l2
# l2.append(l1)
# l2.append(l2[::2])
# l2.append(l2[1::2])
#print(l2)

#add some element whose doesn't exist in the l1 & l2 
# l1.append(20)
# l2.append(16)

# print(f"{l1}\n{l2}")


#insert(element position, element)
l1.insert(0, 50)
#here is the 0 is element position & 50 is the element
print(l1)