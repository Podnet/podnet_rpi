import podnet

a = podnet.Podnet("OVPGpY19qM3QNoZYXg0zjWeEwbBxn2DR", debug=True)

print("Msg recevied is...")

while True:
    msg = a.recv()
    print(msg)

