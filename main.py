#!/usr/bin/python3
import textinput
import pygame
pygame.init()

textinput_obj = textinput.TextInput(font_family="Ubuntu")

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

color_switch = True

while True:
    screen.fill((225, 225, 225))

    color_switch = not color_switch

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Space to do things
    value = textinput_obj.update(events)
    if value: print(value)
    screen.blit(textinput_obj.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(30)
