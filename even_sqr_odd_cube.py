# Return squares of even numbers or cubes when odd numbers
nums=[1,2,5,8,6,4,7,10,3]
even_square=[num*num for num in nums if num%2==0]
odd_cubes=[n*n*n for n in nums if n%2!=0]
print(f"The squares of even numbers is: {even_square} ")
print(f"The cubes of odd numbers is: {odd_cubes} ")