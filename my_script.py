print("Happy Tuesday Night.")

from my_mod import enlarge

df = pandas.DataFrame({"x":[1,2,3], "y":[3,4,5]})

print(df.head())

x = 5
print(x, "ENLARGE", x, "T", enlarge(x))

y = float(input("Please input number"))
print(enlarge(y))
