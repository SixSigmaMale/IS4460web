print(f"a: {55 > 9}")
print(f"b: {4==5}")
print(f"c: {2==0}")
print(f"d: {5==5}")

print("two is equal to 3:",int(2==3))
print("two is equal to two:",int(2==2))

myname = "James"
myage = 41
print(f"a: {77}")
print(f"b: {'goodbye'}")
print(f"c: {True}")
print(f"d: {myname}")
print(f"e: {myage}")

print((1-2+3),(3-2+1))
print((1*2+3),(3*2+1))

print(f"is 'alex'=='alexander'? {'alex'=='alexander'}")

my_name = "alex"
print("assignment: ",my_name)
print("equality: ", my_name =="alex")

print("comparison:","bb"<"c")
print("comparison:", 6 < 7)

a=5
b=6
print(f"comparison: {a} is greater than {b}" if a>b else"")
print(f"comparison: {a} is less than {b}" if a<b else "")
print(f"comparison: {a} is greater than or equal to {b}" if a>=b else "")
print(f"comparison: {a} is less than or equal to {b}" if a<=b else "")

bank_balance = 100
if bank_balance <200:
  money=1000
  bank_balance += money

bank_balance = 100
if bank_balance >200:
  money=1000
  bank_balance += money
else:
  print("balance is less than or equal to 200")

bank_balance =700
savings = 200
if bank_balance <100:
  money=1000
  bank_balance += money
elif bank_balance >200:
  savings +=100
  bank_balance -=100
else:
  savings += 50
  bank_balance -=50
print(bank_balance)
print(savings)

fuel =2
print("Fill tank now" if fuel <= 1 else "there's enough fuel")

fuel =11
while fuel >5:
  print("There's enough fuel")
  fuel -= 1

movies = ["The Notebook","Good Will Hunting","Dead Poets Society"]
for movie in movies:
  print (f"Movie: {movie}")
for i in range(6):
  print(f'i: {i}')

for count in range(9):
  print(f"{count} time 12 is {count *12}")
  if count ==4:
    break
for count in range(9):
  if count ==4:
    continue
  print(f"{count} times 12 is {count*12}")
