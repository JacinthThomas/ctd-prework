# The purpose of the script it to catagorize a player as a child or and adult
#Input First Name
input("First Name: ")
#Input Last Name
input("Last Name: ")
# Input Age to determine if player is an adult or a child. 
print("Age: ")

age = int(input())
if age >= 18:
  print("Adult Divsion!")
else:
  print("Child Divsion")

# Input weight to determine which weight divsion they fall into
print("Weight in kg: ")
weight = float(input())
if weight >= 150:
  print("Heavy weigh Division")
else:
  print("Light weight divsion")
   
