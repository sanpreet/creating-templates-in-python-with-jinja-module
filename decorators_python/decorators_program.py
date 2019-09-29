# defining a decorator 
def calculations(func):
	def inner1(*args, **kwargs):	
 		result = func(*args, **kwargs)
 		return result
	return inner1	

# using the function via a decorator 
@calculations
def function_to_be_used(a, b): 
    if a>b:
    	return a+b
    elif a==b:
    	return a*b
    elif a<b:
    	return a-b
    else:
    	return "inapproriate values of a and b"		
  
# input the value of a and b 
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
# calling the function 
print(
	 "Valid condition as seen from function_to_be_used is :", 
	 function_to_be_used(a, b)
	 )

