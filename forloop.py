
# Write a program to print first 10 even numbers.
##for i in range(2,22,2):
##    print(i)

##for i in range(1,22):
##    if i%2==0:
##        print(i)

# Write a program to print first 10 odd numbers.
##for i in range(1,21,2):
##    print(i)

# square of every even number from 1 to 10
##for i in range(1,11):
##    if i%2!=0:
##        continue
##    print(i*i)

# Write a program to print first 10 even numbers in reverse order.
##for i in range(20,0,-2):
##    print(i, end=" ")

# Write a program to print table of a number accepted from user.
##num = int(input("Enter the number"))
##mult=1
##for i in range(1,11):
##    mult = num*i
##    print(num,"*",i,"=",mult)

##num = int(input("Enter any number"))
##for i in range(1,11):
##    print(num*i)

# Write a program to display product of the digits of a number accepted from the user.
##num = int(input("Enter any number : "))
##mul = 1
##while num!=0:
##    rem = num%10
##    mul = mul*rem
##    num = num//10
##print(mul)

##num = int(input("Enter any number : "))
##p=1
##while(num):
##   r=num%10
##   p=p*r
##   num=num//10
##print("Product of digits is",p)

# Write a program to find the sum of the digits of a number accepted from user
##num = int(input("Enter any number : "))
##sum = 0
##while num!=0:
##    rem = num%10
##    sum = sum+rem
##    num//=10
##print("sum of the digits :", sum)

# Write a program to check whether a number is prime or not.
##num = int(input("Enter any number : "))
##for i in range(2,num+1):
##    if num%i==0:
##        flag = True
##        break
##if flag:
##    print("Not a prime")
##else:
##    print("Not a prime")


##str1 = input("Enter a name : ")
##even = 0
##odd = 0
##for i in range(len(str1)):
##    if i%2==0:
##        even+=1
##    else:
##        odd+=1
##print("number of even : ",even)
##print("number of odd : ",odd)

#  Print sum of all even numbers from 10 to 20
##sum = 0
##for i in range(10,22,2):
##    sum+=i
##print(sum)

# Calculate the square of each number of list given by user:
##num= int(input("Enter the number of elements: "))
##lst = []
##for i in range (num):
##    ele = int(input())
##    lst.append(ele)
##print(lst)
##
##for i in lst:
##    square = i**2
##    print("Square of", i,":", square)

# Calculate the average of list of numbers given by user:
##num = int(input("Enter the number of element in the list: "))
##lst = []
##for i in range(num):
##    ele = int(input())
##    lst.append(ele)
##print(lst)
##
##sum = 0
##for i in lst:
##    sum+=i
##avg = sum/num
##print("Average of elements in the list : ", avg)

# Print all even and odd numbers
##num = int(input("Enter the number of elements in the list : "))
##lst = []
##for i in range(num):
##    ele = int(input())
##    lst.append(ele)
##print(lst)
##
##even = []
##odd = []
##for i in lst:
##    if i%2==0:
##        even.append(i)
##    else:
##        odd.append(i)
##print("Even numbers in the lst",":", even)
##print("Odd numbers in the lst",":", odd)

# Use for loop to generate a list of numbers from 9 to 50 divisible by 2.
##lst = []
##for i in range(9,51):
##    if i%2 == 0:
##        lst.append(i)
##print(lst)
# OR
##for i in range(10,52,2):
##    print(i)

# break the loop if number a number is greater than 15: numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
##numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
##for i in numbers:
##    if i>15:
##        break
##    else:
##        print(i, end = ",")

# Count the total number of ‘m’ in a given string.
##name = input("Enter the name: ")
##count = 0
##for i in name:
##    if i == "m" or i =="M":
##        count+=1
##    else:
##        continue
##print("Number of 'm' inside", name,":", count)

# print only the first two numbers out of 5
##for i in range(1,6):
##    if i >=3:
##        break
##    else:
##        print(i,end=" ")
##else:
##    print("Done")
##

# Reversed numbers of a list given by user, using reversed() function
##num = int(input("Enter the number of elements in the list : "))
##lst = []
##for i in range(num):
##    ele = int(input())
##    lst.append(ele)
##print(lst)
##lst1 = reversed(lst)
##print(lst1)

# Reverse numbers or string , using range() function
##name = "Suraj"
##for i in range(len(name)-1,-1,-1):
##    print(name[i],end='')
##

# Print Multiplication table of a first 5 numbers using for loop and while loop
##for i in range(1,6):
##    print("Multiplication table of", i)
##    count = 1
##    while count<11:
##        print(i,"*",count,"=",i*count)
##        count+=1
##    print('\n')

# Enumurate funtion to find the index of each element in list
##lst = [11,22,33,44,55,66,77,88,99,111]
##print(lst)
##for i, v in enumerate(lst):
##    print("[",i,"]","=",v)

##dict1 = dict(name="suraj",address="odisha")
##print(dict1)

# Creat a dict by user input and find a key given by user input
##length = int(input("Enter the number of keys : "))
##dict1 = {}
##for i in range (length):
##    key =  int(input("Enter the key : "))
##    value = input("Enter the value : ")
##    dict1[key] = value
##print(dict1)
##
##key1 = int(input("Enter a key to search : "))
##for i in dict1:
##    if key1 != key:
##        break
##else:
##    print(key1,"is present in dict1 as a key")













