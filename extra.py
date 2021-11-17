from settings import HEIGHT

def to_pygame(point):
    return (point[0], HEIGHT - point[1])        