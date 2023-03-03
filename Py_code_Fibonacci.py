
# calculate and store the first n Fibonacci numbers

n = 100
fib = [1, 1]
for i in range(2, n+1):
    fib.append(fib[i-1] + fib[i-2])
    print(fib)
    
# alternatively:

n = 100
# keep track of the two most recent Fibonacci numbers
a, b = 1, 1
print(a, b, end='')
for i in range(2, n+1):
  # The next number (b) is a+b, and a becomes the previous b
  a, b = b, a + b
  print(' ', b, end='')

