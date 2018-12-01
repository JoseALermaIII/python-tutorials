# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000.  # km per second


def speed_fraction(time, distance):
    # Traceroute time is often round trip. So, distance must double.
    # Then, multiply by 1000 ms/s to get the right units
    return distance * 2.0 / time * 1000 / speed_of_light


print(speed_fraction(50, 5000))
# >>> 0.666666666667

print(speed_fraction(50, 10000))
# >>> 1.33333333333  # Any thoughts about this answer, or these inputs?
# 1.3 = faster than the speed of light (I wish)
# even .7 the speed of light is pretty fast. No routers?

print(speed_fraction(16, 20))
# >>> 0.00833333333333
