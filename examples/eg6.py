import podnet
import time

other_device = "KrwnMaomk3BxELZwe8XOD5NYev9bzV6W"

net = podnet.Podnet("OVPGpY19qM3QNoZYXg0zjWeEwbBxn2DR", debug=True)

while True:
    net.send_to("red", other_device)
    time.sleep(5)
    net.send_to("green", other_device)
    time.sleep(5)
    net.send_to("blue", other_device)
    time.sleep(5)

