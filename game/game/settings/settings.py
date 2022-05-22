class Click:

    value = 0

    def increment_value(self):
        self.value += 1


class Mouse:
    def __init__(self, mouse_position_tuple: tuple):
        self.x = mouse_position_tuple[0]
        self.y = mouse_position_tuple[1]


FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RECT = (330, 250, 0, 0)
