#days_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]



#for reverse function
# print(f"Days of week: {days_of_weak}")
# days_of_week.reverse()
# print(f"Reverse days of week: {days_of_week}")




#sort(to list element in ascending & decending order)
# nums = [4,5,1,0,7,1,4,5,7,9,0,5,3,3]
# print(f"Our normal list is: {nums}")
# nums.sort()
# print(f"Now, this is the ascending order of list: {nums}")
# nums.sort(reverse=True)
# print(f"After that, this is the decending order of list: {nums}")




#count (to find number of occurrences)
nums = [2,4,7,8,9,0,0,9,4,6,4,2,5,9,0,3,5,]
#print(f"Our lists is \'{nums}\'")
#occurrences = nums.count(int(input(f"Elect the number from the uper list: ")))
#print(f"Total number of occurrences is \'{occurrences}\' in the list.")




#menbership("in" or "not in")
days_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
print(f"Total days of week is: {days_of_week}")

## in
holidays_days_of_week = ["mon", "wed", "thu"]
fun1 = len(holidays_days_of_week)
print(f"We have total \'{fun1}\' holidays in this week.")
fun2 = (input(f" Please select day on which you like to take leave. ") in holidays_days_of_week)
print(f"It is \'{fun2}\', that the day you selected is avilable.")


### not in
# working_days_of_week = ["mon", "thu", "sat", "sun"]
# fun1 = len(working_days_of_week)
# print(f"We have total \'{fun1}\' workdays in this week.")
# fun2 = (input(f" Please select day on which you like to take leave. ") not in working_days_of_week)
# print(f"It is \'{fun2}\',That the day you selected is avilable.")