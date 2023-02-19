#  *************** Q1 *************
percentage =int(input("enter your percentage : "))
if percentage>90:
    print("Grade A")
elif percentage>80 and percentage<=90:
    print("Grade B")
elif percentage >=60 and percentage<80:
    print("Grade C")
else : 
    print("Grade D")

# ********** Q2 ********************
cp=int(input("enter the cost price of bike: ")) #cp stand for cost price
if cp>100000:
    print("road tax : 15%")
elif cp>50000 and cp<=100000:
    print("road tax : 10% ")
else : 
    print("road tax : 5%")

# ***************** Q3 **************
d={"delhi":"Red fort","agra":"Taj Mahal","jaipur":"Jal Mahal"}
city=input("enter the city name : ")
print(d.get(city)) # get() function return the value for a key if is available in dict.

# ***************** Q4 ***************
n=int(input("enter the number : "))
count=0
while n>=10 :
    
   
    if( n%3==0 ): 
        n=n/3
        count=count+1
    else:
        n=n/3
        count=count+1
    
print("number is divisible by : ",count,"times")

# **************** Q5 ****************
'''A while loop evaluates the condition
If the condition evaluates to True, the code inside the while loop is executed.
condition is evaluated again.
This process continues until the condition is False.
When condition evaluates to False, the loop stops.'''
# example : # n=10
# # while n>=1 :
# #     print(n)
# #     n=n-1

#****************** Q6 ******************
def pyra_pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*  ",end="")
        print("\r")
    
def sq_pattern(n):
    print("*********************************************************")
    for i in range(0,n):
        for j in range(0,n):
            print(" * ",end="")
        print("\r")
        
        
def rec_pattern(n):
    print("*********************************************************")
    for i in range(0,n):
        for i in range(0,2):
            print(" *",end="")
        print("\n")
        
pyra_pattern(5)
sq_pattern(5)
rec_pattern(5)
    




# **************** Q7 **************** 
n=10
while n>=1 :
    print(n)
    n=n-1
# question 7 and 8 are same


    


