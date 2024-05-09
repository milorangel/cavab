
import pygame

# Initialisation de Pygame
pygame.init()

# Création d'une surface de test (remplacez la surface par la vôtre)
surface = pygame.Surface((100, 100))
surface.fill((255, 255, 255))  # Remplir la surface avec une couleur blanche
surface.set_at((50, 50), (0, 0, 0))  # Définir un pixel noir à la coordonnée (50, 50)

# Coordonnées du pixel à tester
x = 50
y = 50

# Récupérer la couleur du pixel à la coordonnée spécifiée
pixel_color = surface.get_at((x, y))

# Comparer la couleur du pixel avec pygame.Color(0, 0, 0)
if pixel_color == pygame.Color(0, 0, 0):
    print("Le pixel à la coordonnée ({}, {}) est noir.".format(x, y))
else:
    print("Le pixel à la coordonnée ({}, {}) n'est pas noir.".format(x, y))
