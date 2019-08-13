# Write a program that takes input array daily temperatures, as floats. and findout the maximum and minimum values
ip = input('Array of temp. space separated:')
ip_array = ip.strip().split(' ')
print(ip_array)
float_array = []
for k in ip_array:
    float_array.append(float(k))
print(float_array)
print(min(float_array), " ", max(float_array))
for i in range(len(float_array)):
    for j in range(i+1,len(float_array)):
        if(float_array[i]>float_array[j]):
            temp = float_array[i]
            float_array[i] = float_array[j]
            float_array[j] = temp

print(float_array)
print("minimum: ",float_array[0])
print("maximum: ",float_array[-1])