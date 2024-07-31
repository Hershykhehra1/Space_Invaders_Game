import pygame, random

# Create a class for our Alien that inherits from pygame.sprite.Sprite
class Alien(pygame.sprite.Sprite):
   # Constructor method for initializing the Alien
   def __init__(self, type, x, y):
       # Call the constructor of the parent class (pygame.sprite.Sprite)
       super().__init__()
       # Set the 'type' attribute to distinguish different aliens
       self.type = type
       # Create a file path for the alien image based on its type using f”” which is formatted string literal
       # Example: if the "type" is 1, it will create a path like Graphics/alien_1.png
       path = f"Graphics/alien_{type}.png"
       # Loads the alien image from the specified path
       self.image = pygame.image.load(path)
       # Get the rectangular area occupied by the alien image
       # Set the top-left corner of the rectangle to the specified (x, y) coordinates
       self.rect = self.image.get_rect(topleft=(x, y))

   def update(self, direction):
       # Update the position of the alien based off the direction it moves
       self.rect.x += direction


class MysteryShip(pygame.sprite.Sprite):

    def __init__(self, screen_width, offset):
        super().__init__()
        self.offset = offset
        self.image = pygame.image.load("Graphics/mystery.png")
        self.screen_width = screen_width

        # ".choice" returns random element from list
        # takes two elements, the top left corner of ship IF IT SPAWNS left or right of game screen
        x = random.choice([self.offset/2, self.screen_width + self.offset - self.image.get_width()])

        if x == self.offset/2:
            self.speed = 3
        else:
            self.speed = -3

        # this allows the ship to be 40 pixels down from game screen and spawn the ship left or right side of screen (x)
        self.rect = self.image.get_rect(topleft=(x, 90))

    def update(self):
        # set speed
        self.rect.x += self.speed
        # destroy ship if outside of the game screen
        if self.rect.right > self.screen_width + self.offset/2:
            self.kill()
        elif self.rect.left < self.offset/2:
            self.kill()