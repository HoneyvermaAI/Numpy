from scipy.cluster.hierarchy import average

temperatures = [32.8,36.2,33.4,33.9,28.6,29.4,10.2,8.3,45.0,8.2,22.6]
total = 0
for temp in temperatures:
    total += temp
average = total / len(temperatures)

print("The average of the temperatures is : " , average)