import podnet
from gpiozero import LED

l1 = LED(2)
l2 = LED(3)
l3 = LED(4)


def off_all():
    l1.off()
    l2.off()
    l3.off()


off_all()


def green():
    l1.on()


def red():
    l2.on()


def blue():
    l3.on()


a = podnet.Podnet("KrwnMaomk3BxELZwe8XOD5NYev9bzV6W", debug=True)

print("Control LED using Control Signals")

while True:
    msg = a.recv().lower()
    if msg == "red":
        print("Lighting red LED")
        off_all()
        red()
    elif msg == "blue":
        print("Lighting blue LED")
        off_all()
        blue()
    elif msg == "green":
        print("Lighting green LED")
        off_all()
        green()
    else:
        print(msg)
