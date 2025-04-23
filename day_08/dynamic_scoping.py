x = 1

def funcA():
  print(x)

def funcB():
  x = 2
  print(f"Inside funcB: local x = {x}")
  funcA()

print("Calling funcB...")
funcB()
