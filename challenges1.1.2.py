year = int(input("Enter the year "))

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
  print("{0} is the leap year".format(year))
else:
  print("{0} is not leap year".format(year))
