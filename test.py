from facematch.face import match

f = open('/Users/abhinavtripathi/Downloads/facematch-master/examples/my.jpg', 'rb')
data1 = f.read()
f.close()

f = open('/Users/abhinavtripathi/Downloads/facematch-master/examples/ID.jpg', 'rb')
data2 = f.read()
f.close()

result, distance, data = match(data1, data2)

f = open('out.png', 'wb')
f.write(data)
f.close()

print(distance)
print(result)