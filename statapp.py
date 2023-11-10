# Given a data set input like 77,82,100,95,88
# this program will print out data set's average, variance, standard derivation
#
import fileinput
import sys
import math

# Using input() function to read a line of scores like "77,82,100,95,88"
input_line = input("Enter text: ")
print(input_line)

scores=input_line.split(",")

for i in range(len(scores)):
 scores[i]=int(scores[i])

mean = sum(scores) / len(scores)
res = sum((x - mean) ** 2 for x in scores) / len(scores)
sd = math.sqrt(res)

# printing result
print("The mean of list is : " + str(mean))
print("The variance of list is : " + str(res))
print("The sd of list is : " + str(sd))
