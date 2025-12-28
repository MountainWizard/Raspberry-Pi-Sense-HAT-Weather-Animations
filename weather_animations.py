# Weather animations for the Raspberry Pi Sense HAT
# Libaries ------
from sense_hat import SenseHat
from time import sleep
from random import randrange
# Colour Variables ------
sense = SenseHat()
R = [255, 0, 0] # Red
B = [0, 0, 155]  # Blue Dark
LB = [102, 102, 255] # Blue Light
G1 = [110, 110, 110]  # Gray1 Dark
G2 = [160, 160, 160]  # Gray2 Light
W = [255, 255, 255] # White
Y = [255, 255, 0] # Yellow
DY = [150, 150, 0] # Dark Yellow
LY = [255, 255, 150] # Light Yellow
O = [0, 0, 0]  # Off
# Image Variables ------
cloud = [
O, O, G1, G1, G1, G1, O, O,
O, G1, G2, W, W, W, G1, O,
G1, W, W, G2, W, W, W, G1,
G1, G2, W, W, W, W, G1, O,
O, G1, G1, G1, G1, G1, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
]
lightning = [
O, O, G1, G1, G1, G1, O, O,
O, G1, G2, W, W, W, G1, O,
G1, W, W, G2, W, W, W, G1,
G1, G2, W, W, W, W, G1, O,
O, G1, G1, G1, G1, Y, O, O,
O, O, O, O, Y, O, O, O,
O, O, O, Y, O, O, O, O,
O, O, O, O, Y, O, O, O,
]
sun = [
O, O, O, O, O, O, O, O,
O, O, O, LB, LB, O, O, O,
O, O, LB, LY, DY, LB, O, O,
O, LB, LY, Y, Y, DY, LB, O,
O, LB, LY, Y, Y, DY, LB, O,
O, O, LB, LY, DY, LB, O, O,
O, O, O, LB, LB, O, O, O,
O, O, O, O, O, O, O, O,
]
sun_behind_cloud = [
O, LY, DY, O, O, O, O, O,
LY, Y, Y, DY, O, O, O, O,
LY, Y, LY, LY, G2, G1, O, O,
O, LY, G2, W, W, W, G1, O,
G1, W, W, G2, W, W, W, G1,
G1, G2, W, W, W, W, G1, O,
O, G1, G1, G1, G1, G1, O, O,
O, O, O, O, O, O, O, O,
]
thermometer = [
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, W, O, O, O, O, W, O,
O, W, O, O, O, O, W, O,
O, W, O, O, O, O, W, O,
O, O, W, W, W, W, O, O,
]
# Functions ------
def image_scroll(image):
    sense.clear()
    imgmove = image[56:] + image[: 56] # shift the array by -1 so it will be centered at the end.
    for z in range(8):
        sleep(0.3)
        movement = z * 8
        for y in range(8):
            for x in range(8):
                array_pos = x + 8 * y
                sense.set_pixel(x, y, imgmove[array_pos - movement])
        for b in range(z, 8): # make the lower pixels empty. Otherwise, the other half of the picture would be visible on the bottom.
            for a in range(8):
                sense.set_pixel(a, b, O)

def animation_rain():
    rain = [
    O, O, G1, G1, G1, G1, O, O,
    O, G1, G2, W, W, W, G1, O,
    G1, W, W, G2, W, W, W, G1,
    G1, G2, W, W, W, W, G1, O,
    O, G1, G1, G1, G1, G1, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    drop1 = randrange(16, 31)
    drop2 = randrange(16, 31)
    drop3 = randrange(16, 31)
    drop4 = randrange(16, 31)
    sense.set_pixels(cloud)
    for x in range(50): #change this number to change the animation duration
        sense.set_pixels(rain)
        sleep(0.1)
        if drop1 > 55:
            rain[drop1] = cloud [drop1]
            drop1 = randrange(16, 31)
        else:
            rain[drop1] = cloud [drop1]
            drop1 = drop1 + 8
        if drop2 > 55:
            rain[drop2] = cloud [drop2]
            drop2 = randrange(16, 31)
        else:
            rain[drop2] = cloud [drop2]
            drop2 = drop2 + 8
        if drop3 > 55:
            rain[drop3] = cloud [drop3]
            drop3 = randrange(16, 31)
        else:
            rain[drop3] = cloud [drop3]
            drop3 = drop3 + 8
        if drop4 > 55:
            rain[drop4] = cloud [drop4]
            drop4 = randrange(16, 31)
        else:
            rain[drop4] = cloud [drop4]
            drop4 = drop4 +8
        rain[drop1] = B
        rain[drop2] = B
        rain[drop3] = B
        rain[drop4] = B
    sense.clear()
    rain[drop1] = O
    rain[drop2] = O
    rain[drop3] = O
    rain[drop4] = O

def animation_snow():
    rain = [
    O, O, G1, G1, G1, G1, O, O,
    O, G1, G2, W, W, W, G1, O,
    G1, W, W, G2, W, W, W, G1,
    G1, G2, W, W, W, W, G1, O,
    O, G1, G1, G1, G1, G1, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    drop1 = randrange(16, 31)
    drop2 = randrange(16, 31)
    drop3 = randrange(16, 31)
    drop4 = randrange(16, 31)
    sense.set_pixels(cloud)
    for x in range(12): #change this number to change the animation duration
        sense.set_pixels(rain)
        sleep(0.4)
        if drop1 > 55:
            rain[drop1] = cloud [drop1]
            drop1 = randrange(16, 31)
        else:
            rain[drop1] = cloud [drop1]
            drop1 = drop1 + 8
        if drop2 > 55:
            rain[drop2] = cloud [drop2]
            drop2 = randrange(16, 31)
        else:
            rain[drop2] = cloud [drop2]
            drop2 = drop2 + 8
        if drop3 > 55:
            rain[drop3] = cloud [drop3]
            drop3 = randrange(16, 31)
        else:
            rain[drop3] = cloud [drop3]
            drop3 = drop3 + 8
        if drop4 > 55:
            rain[drop4] = cloud [drop4]
            drop4 = randrange(16, 31)
        else:
            rain[drop4] = cloud [drop4]
            drop4 = drop4 +8
        rain[drop1] = W
        rain[drop2] = W
        rain[drop3] = W
        rain[drop4] = W
    sense.clear()
    rain[drop1] = O
    rain[drop2] = O
    rain[drop3] = O
    rain[drop4] = O

def animation_lightning():
    rain = [
    O, O, G1, G1, G1, G1, O, O,
    O, G1, G2, W, W, W, G1, O,
    G1, W, W, G2, W, W, W, G1,
    G1, G2, W, W, W, W, G1, O,
    O, G1, G1, G1, G1, Y, O, O,
    O, O, O, O, Y, O, O, O,
    O, O, O, Y, O, O, O, O,
    O, O, O, O, Y, O, O, O,
    ]
    drop1 = randrange(16, 31)
    drop2 = randrange(16, 31)
    drop3 = randrange(16, 31)
    drop4 = randrange(16, 31)
    sense.set_pixels(cloud)
    for x in range(50): #change this number to change the animation duration
        sense.set_pixels(rain)
        sleep(0.1)
        if drop1 > 55:
            rain[drop1] = lightning [drop1]
            drop1 = randrange(16, 31)
        else:
            rain[drop1] = lightning [drop1]
            drop1 = drop1 + 8
        if drop2 > 55:
            rain[drop2] = lightning [drop2]
            drop2 = randrange(16, 31)
        else:
            rain[drop2] = lightning [drop2]
            drop2 = drop2 + 8
        if drop3 > 55:
            rain[drop3] = lightning [drop3]
            drop3 = randrange(16, 31)
        else:
            rain[drop3] = lightning [drop3]
            drop3 = drop3 + 8
        if drop4 > 55:
            rain[drop4] = lightning [drop4]
            drop4 = randrange(16, 31)
        else:
            rain[drop4] = lightning [drop4]
            drop4 = drop4 +8
        rain[drop1] = B
        rain[drop2] = B
        rain[drop3] = B
        rain[drop4] = B
    sense.clear()
    rain[drop1] = O
    rain[drop2] = O
    rain[drop3] = O
    rain[drop4] = O

def animation_sunny():
    image_scroll(sun)
    sleep(3)
    sense.clear()
def animation_cloudy():
    image_scroll(cloud)
    sleep(3)
    sense.clear()
def animation_light_cloudy():
    image_scroll(sun_behind_cloud)
    sleep(3)
    sense.clear()
def animation_hot():
    sense.set_pixels(thermometer)
    for y in range(4, 7):
        for x in range(2, 6):
            sense.set_pixel(x, y, B)
    for count in range(3, -1, -1):
        sleep(0.4)
        sense.set_pixel(3, count, B)
        sense.set_pixel(4, count, B)
    for y in range(4, 7):
        for x in range(2, 6):
            sense.set_pixel(x, y, R)
    for count in range(3, -1, -1):
        sense.set_pixel(3, count, R)
        sense.set_pixel(4, count, R)
    sleep(3)
    sense.clear()
def animation_cold():
    sense.set_pixels(thermometer)
    for y in range(4, 7):
        for x in range(2, 6):
            sense.set_pixel(x, y, R)
    for count in range(4):
        sense.set_pixel(3, count, R)
        sense.set_pixel(4, count, R)
    for count in range(4):
        sleep(0.4)
        sense.set_pixel(3, count, O)
        sense.set_pixel(4, count, O)
    for y in range(4, 7):
        for x in range(2, 6):
            sense.set_pixel(x, y, B)
    sleep(3)
    sense.clear()
def animation_fog():
    sense.clear()
    sense.set_pixel(7, 0, G1)
    sleep(0.3)
    sense.set_pixel(6, 0, G1)
    sense.set_pixel(0, 2, G1)
    sleep(0.3)
    sense.set_pixel(5, 0, G1)
    sense.set_pixel(1, 2, G1)
    sense.set_pixel(7, 7, G1)
    sleep(0.3)
    sense.set_pixel(4, 0, G1)
    sense.set_pixel(2, 2, G1)
    sense.set_pixel(6, 7, G1)
    sense.set_pixel(7, 4, G1)
    sleep(0.3)
    sense.set_pixel(3, 0, G1)
    sense.set_pixel(3, 2, G1)
    sense.set_pixel(5, 7, G1)
    sense.set_pixel(6, 4, G1)
    sense.set_pixel(0, 6, G1)
    sleep(0.3)
    sense.set_pixel(2, 0, G1)
    sense.set_pixel(4, 2, G1)
    sense.set_pixel(4, 7, G1)
    sense.set_pixel(5, 4, G1)
    sense.set_pixel(1, 6, G1)
    sense.set_pixel(0, 4, G1)
    sleep(0.3)
    sense.set_pixel(1, 0, G1)
    sense.set_pixel(5, 2, G1)
    sense.set_pixel(4, 7, G1)
    sense.set_pixel(4, 4, G1)
    sense.set_pixel(2, 6, G1)
    sense.set_pixel(1, 4, G1)
    sleep(3)
    sense.clear()
# Display all animations ------
animation_fog()
animation_rain()
animation_snow()
animation_sunny()
animation_lightning()
animation_cloudy()
animation_light_cloudy()
animation_hot()
animation_cold()
