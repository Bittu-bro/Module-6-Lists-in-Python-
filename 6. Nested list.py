#Nested lists
list = [2,[4,0 ],[0,3,6],[4,2,5,[9,0]]]
print(f"Here is our list is: {list}\nAnd our list length is \'{len(list)}\'")

#use this function for find element of list
# fun1 = int(input(f"Enter the element position, whose persent in the list: "))
# print(f"your selected element is : {list[fun1]}.")



#use this function for find sub-element of list
# fun1 = int(input(f"Enter the element position, whose persent in the list! : "))
# fun2 = int(input(f"Enter the sub-element position, whose persent in the list! : "))
# print(f"your selected sub-element is : {list[fun1][fun2]}.")




#use this function for find sub-element of sub-element of list
fun1 = int(input(f"Enter the element position, whose persent in the list! : "))
fun2 = int(input(f"Enter the sub-element position, whose persent in the list! : "))
fun3 = int(input(f"Enter the sub-element of sub-element position, whose persent in the list! : "))
print(f"your selected sub-element of sub-element is : {list[fun1][fun2][fun3]}.")
