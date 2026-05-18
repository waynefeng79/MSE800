# 1. Last Expression in Python Interpreter
a = 2 * 3
try:
    print(f" _ = {_}")
except Exception as e:
    print(f"1. Last Expression _ usage doesn't work in script: {e}")

# 2. Ignoring Values 
# 5. Placeholder for temporary or unimportant variables 
_, a, _ = (1,2,3)
print(f"2,5. a = {a}, _ = {_}")

# 3. As a loop Variable 
print("3. ")
for _ in range(1, 5):
    print("-" * _)

# 4. Formatting Large Numbers
a = 5_000_000
print(f"4. a = {a}")
