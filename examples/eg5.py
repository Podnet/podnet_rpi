import podnet

a = podnet.Podnet("KrwnMaomk3BxELZwe8XOD5NYev9bzV6W", debug=True)

print("Sending msg to device!")

if a.send_to("Hello", "OVPGpY19qM3QNoZYXg0zjWeEwbBxn2DR", debug=True):
    print("Msg sent to device")
else:
    print("Msg was NOT sent")
