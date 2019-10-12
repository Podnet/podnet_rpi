import podnet

a = podnet.Podnet("KrwnMaomk3BxELZwe8XOD5NYev9bzV6W", debug=True)

print("Sending msg to cloud!")

if a.send_to_cloud("it's working!", debug=True):
    print("Msg sent to cloud")
else:
    print("Msg was NOT sent")
