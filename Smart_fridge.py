import pygame
import weather
import News
import AI_image

# Load PNG into Pygame surface
pygame.init()
screen = pygame.display.set_mode([1500, 1000])

# Load background image
background_surf = pygame.image.load("Insert your background image here")

# Load weather image
weather_surf = pygame.image.load(weather.filename)

# Load the AI image
ai_surf = pygame.image.load(AI_image.ad)

# Load news image
news_surf = pygame.image.load(News.news)

# Create font object for news headlines
font = pygame.font.SysFont('Arial', 36)

# Create font object for ad message
ad_font = pygame.font.SysFont('Arial', 33)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black color

    # Blit the background image onto the screen
    screen.blit(background_surf, (0, 0))

    # Display weather image at top left
    screen.blit(weather_surf, (0, 0))

    # Render news headlines onto surface
    text_surface = font.render('NEWS HEADLINES FOR ' + News.country, True, (255, 255, 255))

    # Position text surface below the weather image
    text_rect = text_surface.get_rect()
    text_rect.top = weather_surf.get_rect().bottom + 10

    # Blit text surface and news image onto the screen
    screen.blit(text_surface, text_rect)
    screen.blit(news_surf, (0, text_rect.bottom + 10))

    # Blit the AI image onto the screen
    ai_rect = ai_surf.get_rect()
    ai_rect.topright = (screen.get_width() - 10, 50)
    screen.blit(ai_surf, ai_rect)

    # Render ad message onto surface
    ad_surface = ad_font.render('AD FOR THE CITY OF ' + weather.city, True, (255, 255, 255))

    # Position ad surface above the AI image
    ad_rect = ad_surface.get_rect()
    ad_rect.centerx = ai_rect.centerx
    ad_rect.bottom = ai_rect.top - 10

    # Blit ad surface onto the screen
    screen.blit(ad_surface, ad_rect)

    pygame.display.flip()

pygame.quit()
