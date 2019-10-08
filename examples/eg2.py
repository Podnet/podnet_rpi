import podnet

a = podnet.Podnet("KrwnMaomk3BxELZwe8XOD5NYev9bzV6W", debug=True)

print("Sending msg to cloud!")
if a.sendToCloud("Sacmo!", debug=True):
    print("It worked!")
else:
    print("It didn't")
while True:
    msg = a.recv()
    print(msg)
