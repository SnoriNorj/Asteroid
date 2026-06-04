import pygame, sys

from asteroidfield import AsteroidField 

from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)

from logger import log_state, log_event

from player import Player

from asteroid import Asteroid

from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)
    player = Player (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidfield = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        updatable.update(dt)
        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for ammo in shots:
                if ammo.collides_with(obj):
                    log_event("asteroid_shot")
                    ammo.kill()
                    obj.split()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # using the screen 
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


print("Starting Asteroids with pygame version: 2.6.1") 
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
