import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
black = (0, 0, 0)
blue = (50, 50, 255)
light_blue = (100, 100, 255)

# Screen dimensions
width, height = 800, 600

# Create the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Raindrop Animation")

# Clock to control frame rate
clock = pygame.time.Clock()

# Raindrop properties
raindrop_radius = 2
ripple_radius = 5
ripple_growth_rate = 1
raindrop_fall_speed = 5

# List to store raindrops and ripples
raindrops = []
ripples = []


def draw_raindrop(x, y):
    pygame.draw.circle(screen, blue, (x, y), raindrop_radius)


def draw_ripple(x, y, radius):
    pygame.draw.circle(screen, light_blue, (x, y), radius, 1)


def create_raindrop():
    x = random.randint(0, width)
    y = random.randint(-20, -1)
    raindrops.append((x, y))


def create_ripple(x, y):
    ripples.append((x, y, ripple_radius))


def update_raindrops():
    for i in range(len(raindrops)):
        raindrops[i] = (raindrops[i][0], raindrops[i][1] + raindrop_fall_speed)
    for x, y in raindrops:
        if y > height:
            create_ripple(x, height)
    return [rd for rd in raindrops if rd[1] <= height]


def update_ripples():
    for i in range(len(ripples)):
        ripples[i] = (ripples[i][0], ripples[i][1], ripples[i][2] + ripple_growth_rate)
    return [rp for rp in ripples if rp[2] < 50]


def main():
    running = True
    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        create_raindrop()
        raindrops = update_raindrops()
        ripples = update_ripples()

        for x, y in raindrops:
            draw_raindrop(x, y)

        for x, y, radius in ripples:
            draw_ripple(x, y, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()