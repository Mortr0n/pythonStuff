print("Hello World!")
name = "Noelle"
print("Hello",name)
print ("Hello " + name)

name=42
print("Hello", 42)
# print("Hello " +42)

fav_food1 = "sushi"
fav_food2 = "Pizza"
print("I love to eat {} and {}".format(fav_food1, fav_food2))
print(f"I love to eat {fav_food1} and {fav_food2} ")

x = 70
if x>50:
    print("bigger than 50")
else:
    print("less than 50")

print(type(x))

my_dict = { "name": "Noelle", "language": "Python"}
for k in my_dict:
    print(my_dict[k])

capitals = {"a": "A", "b": "B", "c": "C", "d": "D"}

for key in capitals.keys():
    print(key)

for val in capitals.values():
    print(val)

for key, val in capitals.items():
    print(key, " = ", val)

for count in range(0, 5):
    print("looping - ", count)

count = 0
while count < 5:
    print("looping - ", count)
    count += 1

y = 3
while y > 0:
    print(y)
    y = y -1
else: 
    print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)

for val in "string":
    if val == "i":
        continue
    print(val)

y=3
while y > -1:
    print(y)
    y -= 1
    if y==0:
        break
else:
    print("Final else statement")