#Create a program that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
WIN = int(input("Enter win match: "))
DRAWS = int(input("Enter draws match: "))
LOSSES = int(input("Enter losses match: "))

points = WIN * 3 + DRAWS * 1 + LOSSES * 0
print("Final pints is = {0}".format(points))