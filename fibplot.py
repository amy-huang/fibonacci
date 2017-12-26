import matplotlib.pyplot as plt
from math import sqrt
# Which fibonacci numbers and approximations to plot?
start = 100 
end = 110
xvals = [i for i in range(start, end)]


# To truncate float approximations
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

# Plotting exact fibonacci numbers
fiblist = [1, 1]
for i in range(end):
    fiblist.append(fiblist[len(fiblist) - 1] + fiblist[len(fiblist) - 2])
print(fiblist[start:end])
plt.plot(xvals, fiblist[start:end], marker='o', color='r', label='exact fibonacci numbers')

# Plotting first approximations
approxlist = [1, 1]
mult = .5 * (1 + sqrt(5))
for i in range(end + 2):
    approxlist.append(mult * approxlist[len(approxlist) - 1])
#print([float(truncate(approxlist[i], 3)) for i in range(start, end)])
print([int(approxlist[i]) for i in range(start, end)])
plt.plot(xvals, approxlist[start:end], marker='o', color='b', label='first approximations')

# Plotting second approximations
approxlist = [1, 1]
mult2 = .5 * (1 + sqrt(4.995))
for i in range(end + 2):
    approxlist.append(mult2 * approxlist[len(approxlist) - 1])
#print([float(truncate(approxlist[i], 3)) for i in range(start, end)])
#plt.plot(xvals, approxlist[start:end], marker='o', color='g', label='sqrt(4.999)')

# Plotting third approximations
approxlist = [1, 1]
mult2 = .5 * (.999 + sqrt(5))
for i in range(end + 2):
    approxlist.append(mult2 * approxlist[len(approxlist) - 1])
#print([float(truncate(approxlist[i], 3)) for i in range(start, end)])
#plt.plot(xvals, approxlist[start:end], marker='o', color='y', label='.999 + sqrt(5)')

# Plotting fourth approximations
approxlist = [1, 1]
mult2 = .5 * (1 + sqrt(5.005))
for i in range(end + 2):
    approxlist.append(mult2 * approxlist[len(approxlist) - 1])
#print([float(truncate(approxlist[i], 3)) for i in range(start, end)])
plt.plot(xvals, approxlist[start:end], marker='o', color='m', label='sqrt(5.005)')

plt.legend()
plt.title(str(start) + ' to ' + str(end) + ' fibonacci numbers and approximations')
plt.axis([start, end, mult**(start), mult**(end - 1)])
plt.ylabel('kth fibonacci number or approximation')
plt.xlabel('k')

plt.savefig('all3mearly.jpg')
plt.show()
