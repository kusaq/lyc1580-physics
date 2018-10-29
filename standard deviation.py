data = [float(x) for x in input().split()]
out = float(1)
medium = float(sum(data)/len(data))
for i in data:
    out *= ((i-medium)**2/(len(data)-1))**.5
print(out)
