def calc(x):
  x = x.split()
  stack = []
  
  num2 = int(x.pop())
  
  while x:
    num1 = int(x.pop())
    operator = x.pop()
    
    if operator == "+":
      num2 = num1 + num2
      
    if operator == "-":
      num2 = num1 - num2
      
    if operator == "*":
          num2 = num1 * num2
          
    if operator == "/":
          num2 = num1 / num2

  return num2


print calc("- 1 2")  # 1 - 2
# -1
print calc("- 9 * 2 3")  # 9 - (2 * 3)
# 3
print calc("/ 6 - 4 2")  # 6 / (4 - 2)
# 3