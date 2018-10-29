print('#### POWERS THEN AMPERAGES ####')

data = [float(x) for x in input().split()]
amperages = [float(x) for x in input().split()]
powers = []

r_mini = 0.073
r_big = 0.177
n = 600.0

print()
for i in range(1, len(data), +2):
    powers += [float(data[i-1] + data[i])]

for i in range(len(powers)):
    print(i,'| P =', round((amperages[i]*3.14*((r_big)**2)*n), 3), 'AND M =', round((powers[i]*r_mini), 3))
