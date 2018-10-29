data = [float(x) for x in input().split()]
medium = float(sum(data)/len(data))
out = 1
for i in data:
    out *= ((i-medium)**2/(len(data)-1))**.5
print(out)
