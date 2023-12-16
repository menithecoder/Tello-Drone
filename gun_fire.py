import pygame
import time
# Initialize pygame

def fire(num):
    start_time=time.time()
    while time.time()-start_time<2 :
        pygame.init()

        # Load gunfire sound file
        if(num==1):
            gunfire_sound = pygame.mixer.Sound("gunfire.mp3")
        if(num==2):
            gunfire_sound = pygame.mixer.Sound("rocket.mp3")


        # Play the gunfire sound
        gunfire_sound.play()

        # Wait for the sound to finish (optional)
        pygame.time.wait(int(gunfire_sound.get_length() * 1000))

        # Quit pygame
        pygame.quit()


