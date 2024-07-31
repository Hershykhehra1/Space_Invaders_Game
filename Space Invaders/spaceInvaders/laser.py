# Step 1
import pygame


# Step 2
class Laser(pygame.sprite.Sprite):
    # Step 3: constructor
    def __init__(self, position, speed, screen_height):
        # Call in the parent class
        super().__init__()
        # Step 4: yellow small rectangle
        # laser
        self.image = pygame.Surface((4, 15))
        self.image.fill((243, 216, 63))
        # Step 5:
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height +15 or self.rect.y < 0:
            # remove the sprite complete
            print("Killed")
            self.kill()