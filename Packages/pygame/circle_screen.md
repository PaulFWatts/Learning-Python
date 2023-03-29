[Python 001 - Python and Pygame (ronjeffries.com)](https://ronjeffries.com/articles/-y023/python/-z000/001/)

> I’ve decided to work with Python a bit. I think I’ll enjoy it as much as Kotlin, and I’ll certainly enjoy being further away from Gradle.

I have thought for years that I would like the Python language. I like Ruby and Smalltalk, which are both duck-typing languages, and I am really good about proper indenting, so aside from an aversion to typing `self` as the first parameter to all my functions, I should be good to go.

I’ve had a brief pairing session with Bryan Beecham, setting up PyCharm. I’ve paid my PyCharm fee, perhaps for the second time, so I’m good to go.

I have a sample program, not the first one that Bryan and I I started with because I cleverly pasted over it, but this is like the second example for pygame and it’s just fine as a start.

I’ll be explaining simple things here, with two purposes. First, explaining them will help me to learn them. Second, some few readers might be interested in starting with pygame, and the explanations may help them. Here’s the program I’ve got right now:

```
# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
```

As with the Kotlin game thing, OPENRNDR, and the Codea game thing before it, we’ve got two basic phases here, the setup and the game loop. Everthing before the `while running:` is the setup, and the infinite `while` loop is the game loop.

The first thing I want to mention is that if we just did `while running:`, our game loop would run flat out, full speed, pedal to the metal, CPU temperature notwithstanding. So down at the very bottom we see `clock.tick(60)`, which, I gather, pauses the loop unti at least a 60th of a second has elapsed. I don’t know whether it still spins on the CPU or not. Anyway, that code gives us at most 60 updates per second. And, while we’re looking at it, it apparently returns the actual time of the slice, and we compute that into `dt`, whose units are presumably seconds.

The setup makes sense to me on the face of it:

```
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
```

I think we might argue about the `dt`, call it `deltaTime` or something, but it’s the kind of thing that the team will all see every day and know what it means. For now, I’m willing to let it go.

The rules are that you have to say `pygame.init()`. `pygame.display` is the main window of the program, and the `set_mode` is setting its size. My recollection from scanning the pygame documents is that `set_mode` can set other aspects of the screen, but I don’t remember the details. We’ll look them up when we need to.

I guess that `pygame.time.Clock()` is creating a clock. More than that I do not know … yet.

And the `running` flag, and `dt`. So, yeah, about what you’d expect. And in the main loop, this too has a generally familiar feeling:

```
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
```

My reading tells me that pygame creates an event queue, and you can read it with that `pygame.event.get()` that we see there. There will be keyboard events, mouse events, and so on in there. This sample just looks for `QUIT`, which is the event that fires when you close the window by clicking the X or red dot, or whatever you click on your computer to close a window. It also seems to work, on my MacBook Air, with Command+Q and Command+W. No big surprise there.

Having not quit, we draw a purple background by telling the screen to fill, and we ask pygame to draw a circle of radius 40. Or maybe it’s width 40. It is in fact radius: I just [looked it up](https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle). We’ve already seen that `player_pos` is set to the center of the screen by dividing the width and height in half.

And that brings me to a sort of digression.

Raster-Based

It seems that pygame graphics are what I’d call raster-based. The screen is an array of dots and you mostly write to it by “blitting” small arrays onto it. There does not seem to be any of the usual ability to rotate, translate, and scale your “viewport”, though you can rotate and scale a rectangle of pixels.

There are drawing primitives, which can draw onto any “Surface”, including the screen / display. If you have a picture of a spaceship or a cat, you can load that picture into a Surface and to put it on the screen, you `blit` it to the desired location, which pastes the pixels of the picture onto the screen at that point. Pygame does double-buffering, so that the blitting happens behind the scenes, and when you’ve done all your updating, you to `screen.flip()` and the new drawing appears.

I’m not sure how this is going to effect my coding. We’ll find out.

OK, back to this program. What we haven’t talked about yet is this:

```
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()
```

We use the famous WASD keys to mean “up left down right” and we adjust the `x` and `y` of `player_pos` accordingly. The 300 was surely selected so that things would feel right, but what it means, since it is scaled by `dt`, is 300 pixels per second.

After we change the player position, we do `pygame.display.flip()` to show the new background with the ball in its new position. (Well, actually, in its old position, since we first drew it and then moved the position for next time.)

When we run the program, it looks like this:

![ball moves around](https://ronjeffries.com/articles/-y023/python/-z000/001/ball.mov)

(I promise I’ll figure out a way to make these movies other than `.mov` files … but it’s so easy this way!)

## Testing

I don’t have a test for this program, but Bryan did kindly help me set up a test file so that I’d know how to do it:

```
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
```

Apparently PyCharm wants two blank lines between major items like imports and classes and classes and top level code. If I move those closer together it kindly offers to reformat. Hey, I just want to get along here, so I go with the social pressure.

When I run this clever test, it runs green with this message:

I can commit this little program and I think I will, since I’ve already lost a bit of the code that Bryan and I did yesterday, pasting this example over the top of our program, which was almost exactly like this one except without the ball.

Commit: _Initial commit pygame demo 2_.

Let’s sum up with a few observations, and notes on what I might do next.

## Summary

I like PyCharm: it’s a lot like IDEA, seemingly without the nasty Gradle stuff. It has a nice “virtual environment” that maintains a list of your libraries and versions and such. It seems easier to set things up, and since I do tend to write a lot of little programs, that will be useful.

So far, I’ve mostly only pasted code into PyCharm, so I don’t have a sense of how readily I’ll fall into the Python style, but the IDE seems pretty good about doing the indents for you, so I think it’ll mostly be easy. I’m more concerned with how often I’ll forget to put `self` into methods as the first parameter. We’ll see.

Next steps may include:

1.  Draw some different things, experiment with blitting, rotating, and scaling. I’ll probably do the Asteroids ship.
2.  Figure out a connection from here to GitHub, so that I can publish repos in case anyone wants to look at them.
3.  Perhaps set up a standard starting template for new programs. I think PyCharm knows how to do that, or I could have one up on GitHub to clone. I’d like to have a smooth process for starting new things.
4.  Probably … do asteroids one more time, in Python.
5.  Maybe … more than once.

So … a small beginning, but satisfactory for now. I hope you’ll follow along, and if you do, I hope you’ll let me know, ask questions, offer ideas, and so on.

See you next time!