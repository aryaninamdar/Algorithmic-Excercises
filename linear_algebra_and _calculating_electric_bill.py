import numpy as np
import matplotlib.pyplot as plt

# Problem 1
a = np.array([ [2,-9], [1,6] ])
b = np.array([14,7])
solution = np.linalg.solve(a,b)
print("Problem 1")
print("[x. y.]")
print(solution)

# Problem 2
a = np.array([ [-11,10], [3,-2] ])
b = np.array([-4,4])
solution = np.linalg.solve(a,b)
print("\nProblem 2")
print("[x. y.]")
print(solution)

# Problem 3
print("\nProblem 3")
x = np.arange(0, 10, 0.1)
y = ((2/9) * x) - (14/9)
y2 = (-x/6) + (7/6)
plt.plot(x, y)
plt.plot(x, y2)
plt.yticks(np.arange(-5, 5, 1.0))
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
print("The lines ntersect at (7, 0), which is the same answer as Problem 1, therefore it is correct.")

# Problem 4
a = np.array([ [2,3,-1], [4,1,-3], [3,-2,5] ])
b = np.array([1,11,21])
solution = np.linalg.solve(a,b)
print("\nProblem 4")
print("[x. y. z.]")
print(solution)

# Problem 5
def electricity_rates(quantity):
  # found these by doing some math with the 4 suitable points
  d = 0.72
  r1 = 0.12
  r2 = 0.19
  r3 = 0.26

  # adds certain rates to cost depedning on quantity
  cost = 0.72
  if quantity <= 394:
    cost = (quantity * r1)
  elif quantity > 394 and quantity <= 1576:
    for x in range(quantity):
      if x < 394:
        cost += r1
      else:
        cost += r2
  elif quantity > 1576:
    for x in range(quantity):
      if x < 394:
        cost += r1
      elif x > 394 and x <= 1576:
        cost += r2
      else:
        cost += r3

  return cost


print("\nProblem 5")
units = np.random.randint(1,2000,200)
units.sort()
cost = [electricity_rates(quantity) for quantity in units]
plt.plot(units, cost)
plt.xlabel("Electricity Used (kWh)")
plt.ylabel("Cost")
