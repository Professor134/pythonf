bit = int(input("enter the no of bits"))

bytes = float(bit/8)
kilobytes = float(bytes/1024)
megabytes = float(kilobytes/1024)
gigabytes = float(megabytes/1024)
terabytes = float(gigabytes/1024)

print("bits=",bit)
print("kilobytes=",kilobytes)
print("megabytes=",megabytes)
print("gigabytes=",gigabytes)
print("terabytes=",terabytes)