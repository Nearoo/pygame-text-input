# Pygame Text Input Module

This module provides two utility classes that simplify entering text using pygame. The classes are:
* `TextInputVisualizer` which can be used to both manage and draw text input. Simply pass all events returned by `pygame.event.get()` to it every frame, and blit its `surface` attribute on the screen.
*  `TextInputManager` that can be used to just manage inputted text, with no visual aspect. Used by `TextInputVisualizer` behind the scenes.



![Example of module in use](https://i.imgur.com/h7a64Y2.gif)

# Installation

Simplest way is using pypi:

```
python3 -m pip install pygame-textinput
```

# Usage

## `TextInputVisualizer`

### Example

All arguments to the constructor are optional. Once constructed, call `update` every frame with all pygame events as an argument, then blit it's `surface` field to the screen, like so:

```python
import pygame_textinput
import pygame
pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (10, 10))

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(30)
```

## Arguments:

All arguments are optional. 

Argument | Description
---|---
manager | The `TextInputManager` used to manage the input
font_object | The `pygame.font.Font` object used for rendering
antialias |  whether to render the font antialiased or not
font_color | color of font rendered
cursor_blink_interval | The interval of the cursor blinking, in ms
cursor_width | The width of the cursor, in pixels
cursor_color | The color of the cursor

## Fields

All arguments above are also fields that can be accessed and modified on the fly, e.g. like this:

```python
textinput.cursor_width = 12
textinput.value = "Hello, World!"
print(textinput.font_color)
```

Field | Description
--- | ---
value | (string) The text entered so far
surface | The `pygame.Surface` object with entered text & cursor on it and a transparent background. **Cannot be set.**
cursor_visible | (bool) wether the cursor is currently visible or not. Flips every `cursor_interval` ms as long as `update` is called continuously. 

## Methods

Method | Description
--- | ---
update(events) | Call this method every frame for as long as input should be processed and `cursor_visible` should be updated.

### Notes on the newer version:
* You have to watch for "return" presses by the user yourself, e.g. like this:

```python
for event in events:
    ...
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        print("Oooweee")
```

* Contrary to the old version, key-stroke repeats are not manually introduced anymore, since they can now be enabled within `pygame` directly:

```python
pygame.key.set_repeat(200, 25) # press every 50 ms after waiting 200 ms
```


This new version has also been optimized such that you can **modify any fields on the fly** and the actual surface will only re-render if you access it using `textinput.surface` - and only if you actually modified any values.


# `TextInputManager`

If you prefer to draw the text on the screen yourself, you can use `TextInputManager` to only manage the string that has been typed so far.

Like `TextInputVisualizer`, you feed its `update` method all events received by `pygame.event.get()` which you want it to process. `TextInputVisualizer` does this for you inside its `update` method if you pass it a `TextInputManager`.

## Arguments:
Argument | Description
---|---
initial | The initial value (text)
validator | A function taking a `string` and returning a `bool`. Every time an input modifies the value, this function is called with the modified value as an argument; if the function returns `True`, the input is accepted, otherwise the input is ignored.

So say you want to only allow input to up to 5 letters, you could do that with

```python
manager = TextInputManager(validator=lambda input: len(input) <= 5)
```

## Fields
Field | Description
---|---
value | The inserted value so far. When change, `cursor_pos` is kept as far as possible.
cursor_pos | The position of the cursor. `0` is before the first character, `len(manager.value)` the position after the last. Values outside this range are clamped.


# More Examples

## Most features

```python
import pygame
import pygame.locals as pl

pygame.init()

# No arguments needed to get started
textinput = TextInputVisualizer()

# But more customization possible: Pass your own font object
font = pygame.font.SysFont("Consolas", 55)
# Create own manager with custom input validator
manager = TextInputManager(validator = lambda input: len(input) <= 5)
# Pass these to constructor
textinput_custom = TextInputVisualizer(manager=manager, font_object=font)
# Customize much more
textinput_custom.cursor_width = 4
textinput_custom.cursor_blink_interval = 400 # blinking interval in ms
textinput_custom.antialias = False
textinput_custom.font_color = (0, 85, 170)

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

# Pygame now allows natively to enable key repeat:
pygame.key.set_repeat(200, 25)

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    textinput_custom.update(events)

    # Get its surface to blit onto the screen
    screen.blit(textinput.surface, (10, 10))
    screen.blit(textinput_custom.surface, (10, 50))

    # Modify attributes on the fly - the surface is only rerendered when .surface is accessed & if values changed
    textinput_custom.font_color = [(c+10)%255 for c in textinput_custom.font_color]

    # Check if user is exiting or pressed return
    for event in events:
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            print(f"User pressed enter! Input so far: {textinput.value}")

    pygame.display.update()
    clock.tick(30)
    
```

