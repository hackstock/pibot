def clip_speed(speed, minimum=-100, maximum=100):
    if speed < minimum:
        return minimum
    elif speed > maximum:
        return maximum
    else:
        return speed