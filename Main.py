import time

def factorize(*numbers):
    result = []
    for n in numbers:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        result.append(list(set(factors)))
    return result

start_time = time.time()
a, b, c, d = factorize(128, 255, 99999, 10651060)
end_time = time.time()
print("Time:", end_time - start_time)
print(a)
print(b)
print(c)
print(d)
