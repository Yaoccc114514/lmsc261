#Code is here

#1
for i in range(4):
    print("Hello")

#2
count = 0
while count < 3:
    count = count + 1

print(count)

#3
score = 85
if score > 70:
    print("Pass")
elif score > 80:
    print("Great")
else:
    print("Fail")

#4
x = 5
while x > 0:
    print(x)
    x += 1

#5
for i in range(2):
    for j in range(2):
        print(i, j)


#My Answer
Q1. I think it will print "Hello" four times.

Actual Result:
Hello
Hello
Hello
Hello

range(4) makes the loop run 4 times (0, 1, 2, 3). Each time the loop runs, the program prints "Hello".



Q2. I think the loop will increase the count until it reaches 3, so it will print 3.

Actual Result:
3

The variable count starts at 0. The while loop runs while count < 3. Each loop increases count by 1. When count becomes 3, the loop stops and print(count) prints 3.



Q3. I think it might print "Great" because the score is high.

Actual Result:
Pass

Python checks conditions from top to bottom. The first condition is score > 70. Since 85 is greater than 70, the program prints "Pass". The elif condition is never checked because the first condition is already true.



Q4. I think it will print numbers starting from 5 and keep increasing.

Actual Result:
5
6
7
8
9
... (continues forever)

The loop condition is while x > 0. The variable x starts at 5 and increases by 1 each time (x += 1). Because x keeps getting bigger, it will always stay greater than 0. This creates an infinite loop.




Q5. I think it will print pairs of numbers from the two loops.

Actual Result:
0 0
0 1
1 0
1 1

There are two loops (nested loops). The outer loop runs with i = 0 and i = 1. For each value of i, the inner loop runs with j = 0 and j = 1. Each time it prints the pair (i, j).
