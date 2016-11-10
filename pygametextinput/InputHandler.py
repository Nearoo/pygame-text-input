import pygame

# Font module of pygame must be initialized before it can be used:
pygame.font.init()

class InputHandler:
    def __init__(self, surface_size, fontname=None, fontsize=12):
        """
        (WIP DOCS)
        * Removes all KEYDOWN events from the event queue
        """
        self.text_array = []
        self.font_object = pygame.font.Font(pygamge.font.match_font(fontname), fontsize)
        self.rerender = False # If True the surface gets rerendered
        self.text_color = 1, 1, 1

        self.cursor_pos = 0 # pos in text_array
        self.cursor_blinking_speed = 500 #ms
        self.cursor_visible = False
        self.cursor_time_counter = 0
        self.cursor_surface = pygame.Surface(self.font_object.size("|"))


        self.surface = pygame.Surface(surface_size)

    def update(self, dt):

        # Update visual representation of cursor:
        self.cursor_time_counter += dt
        if self.cursor_time_counter >= self.cursor_blinking_speed:
            self.cursor_visible = not self.cursor_visible
            self.rerender = True

        for key in pygame.event.get(pygame.KEYDOWN):
            key
