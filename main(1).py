# connect to the file
f = open("data1.txt", "r")

lastname = f.readline()

#loop as long as the last readline is not null
while lastname != "":
  age = f.readline()
  print(lastname, " age is ", age)
  lastname = f.readline()



