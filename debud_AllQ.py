# # Q1
# def greet():
#     username = "Elia"
#     return f"Hello, {username}!"

# print (greet())

# ==================================

# # Q2
# counts = {"a":1, "b":2, "c":3}

# for k in list(counts):
#     if counts[k] %2 == 1:
#         del counts[k]

# print(counts)

# ==================================

# # Q3
# text = "debugging" + "!"

# print (text)

# ==================================

# # Q4
# nums = [1,2,3]
# for i in range(0, len(nums)):
#     print(nums[i])

# ==================================

# # Q5
# config = {"host" : "localhost", "port" : 5432}
# print(config["host"])
# print(config["port"])

# =================================

# # Q6
# age = 12
# print(age + 5)

# =================================

# # Q7
# user_input = "12.5"
# print(float(user_input))

# =================================

# # Q8
# def ratio(a, b):
#     return a / b
# print(ratio(0, 10))

# ================================

# # Q9
# import json
# print(json.dumps({"OK":True}))

# ================================

# # Q10 RecursionError
# def down(n):
#     if n == 0:
#         return 1
#     else:
#         return n * down(n - 1)
# print(down(5))

# =================================

# # Q11 Infinite loop
# x = 5
# while x > 0:
#     print(x)
#     break
# # x never changes

# =================================

# # Q12 Mutable default argument – state “leaks” across calls
# def add_item(item, bucket = None):
#     if bucket is None:
#         bucket = []
#         bucket.append(item)
#         return bucket
# print(add_item("a"))
# print(add_item("b"))

# ==================================

# Q13