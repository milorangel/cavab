import pygame


class Button:
    def __init__(self, rect_center, image='', caption='', width=0, height=0, btn_color=(255, 255, 255, 50), scale=1,
                 txt_color=(0, 0, 0), txt_color_back='0'):
        self.image = image

        self.btn_color = btn_color
        self.rect_center = rect_center
        self.x = rect_center[0]
        self.y = rect_center[1]
        self.clicked = False
        self.txt_color_back = txt_color_back

        # Set up the caption
        self.caption = caption
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render(self.caption, True, txt_color)
        if self.txt_color_back != '0':
            self.text_back = self.font.render(self.caption, True, txt_color_back)

        # Determine width and height
        self.width = width if width != 0 else self.text.get_width() + 10
        self.height = height if height != 0 else self.text.get_height() + 10

        # Create the rect for the button
        self.rect = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Draw button rectangle
        pygame.draw.rect(surface, self.btn_color, self.rect)

        # Position the text in the center of the button
        textx = self.rect.x + (self.width - self.text.get_width()) // 2
        texty = self.rect.y + (self.height - self.text.get_height()) // 2

        if self.txt_color_back != '0':
            surface.blit(self.text_back, (textx - 2, texty + 2))

        surface.blit(self.text, (textx, texty))

        # Check if the button is clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return action