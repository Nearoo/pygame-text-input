# Pygame Text Input Module

This small module can be used to write text in pygame. It includes a blinking cursor that can be moved using the left and right as well as the home and the end button. Any key can be pressed for an extended period of time to make that key re-enter itself many times a second.

Here's an example of the module in use using the [Ubuntu font](http://font.ubuntu.com/):
![Example of module in use](http://i.imgur.com/enuCPEY.gif)

# Usage

The module is very easy to use. Simply create an instance of `InputText` in your code and then feed its `update`-method with pygame-events every frame. The surface with the text and the cursor can then be gotten using `get_surface()`.

Here's a small example that displays a white window with the `InputText`-surface on it:


```
#!/usr/bin/python3
import pygame_textinput
import pygame
pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInput()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(30)
```
If you want to catch the user input after the user hits `Return`, simply evaluate the return value of the `update()`-method - it is always `False` except for when the user hits `Return`, then it's `True`. To get the inputted text, use `get_text()`. Example:
```
if textinput.update(events):
    print(textinput.get_text())
```

## Arguments:
Arguments for the initalisation of the `TextInput`-object (all of them are optional)

argument | description
---|---
font_family | Name or path of the font that should be used. If none or one that doesn't exist is specified, the pygame default font is used.
font_size | Size of the font in pixels. Default is 35.
antialias | (bool) Declare if antialias should be used on text or not. True uses more CPU cycles.
text_color | The color of the text.
repeat_keys_initial_ms | Time in ms until the key presses get repeated when a key is not released
repeat_keys_interval_ms | Time in ms between key presses if key is not released

## License:

The project stands under the MIT-license:

> Copyright (c) 2016 Silas Gyger

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
