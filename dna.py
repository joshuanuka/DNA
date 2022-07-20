originalDNA = str(input("Enter a DNA sequence: "))
fPattern = str(input("Enter the pattern: "))
rPattern = fPattern[::-1]
theParts = originalDNA.split(fPattern, 1)
lastTwo = theParts[1].split(rPattern, 1)
theParts.remove(theParts[1])
for i in lastTwo:
    theParts = theParts + [i]
prefix = theParts[0]
middle = theParts[1]
suffix = theParts[2]
theParts[1] = theParts[1][::-1]
rMiddle = theParts[1]
result = str(theParts[0]) + fPattern + str(theParts[1]) + rPattern + str(theParts[2])
print("Prefix: " + prefix)
print("Marker: " + fPattern)
print("Middle: " + middle)
print("Reversed Middle: " + rMiddle)
print("Reversed Marker: " + rPattern)
print("Suffix: " + suffix)
print("Result: " + result)
