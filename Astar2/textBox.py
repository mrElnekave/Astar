import pygame
pygame.init()

class TextBox:
    def __init__(self, Xpos, Ypos, Box_width, Box_height, idle_colour=(124,124,124), active_colour=(255,255,255),
                 text_size=None, border=3, border_colour=(200,200,200)):
        # set positions
        self.x = Xpos
        self.y = Ypos
        self.pos = (self.x, self.y)
        # set dimensions
        self.Box_w = Box_width
        self.Box_h = Box_height
        # set colours
        self.idle_colour = idle_colour
        self.active_colour = active_colour
        # text
        self.text = ""
        self.border = border
        self.border_colour = border_colour
        self.capital = False
        if text_size == None:
            self.font = pygame.font.SysFont("Times New Roman", self.Box_h // 4)
        else:
            self.font = pygame.font.SysFont("Times New Roman", text_size)
        # state
        self.active = False
        # pygame terminology
        self.image = pygame.Surface((self.Box_w, self.Box_h))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if not self.active:
            if self.border == 0:
                self.image.fill(self.idle_colour)
            else:
                self.image.fill(self.border_colour)
                pygame.draw.rect(self.image, self.idle_colour,(self.border, self.border, self.Box_w - self.border*2,
                                                               self.Box_h - self.border*2))
        else:
            if self.border == 0:
                self.image.fill(self.active_colour)
            else:
                self.image.fill(self.border_colour)
                pygame.draw.rect(self.image, self.active_colour, (self.border, self.border, self.Box_w - self.border * 2,
                                                                self.Box_h - self.border * 2))
        text = self.font.render(self.text, False, (0, 0, 0))
        Ypos = (self.Box_h - text.get_height()) // 2
        text_width = text.get_width()
        if text_width < self.Box_w - self.border*2 or not self.active:
            self.image.blit(text, (1 + self.border * 2, Ypos))
        else:
            self.image.blit(text, (1 + self.border * 2 + self.Box_w - text_width - (self.border*4), Ypos))

        screen.blit(self.image, self.pos)

    def click(self, m_pos):
        if self.rect.collidepoint((m_pos)):
            self.active = True
        else:
            self.active = False

    def getText(self):
        return self.text

    def update_text(self, key, shift=False):
        if self.active:
            # letters and numbers
            text = list(self.text)
            # if chr(key).isalpha():
            #     if key == 304:
            #         self.capital = True
            #         print(key)
            #     else:
            #         if self.capital:
            #             text.append(chr(key).capitalize())
            #             self.capital = False
            #         else:
            #             text.append(chr(key))
            #         self.text = "".join(text)
            if chr(key).isalpha() or chr(key).isdigit():
                if key == 304:
                    pass
                else:
                    if shift:
                        text.append(chr(key).capitalize())
                    else:
                        text.append(chr(key))
                    self.text = "".join(text)
            # elif chr(key).isdigit():
            #     text.append(chr(key))
            #     self.text = "".join(text)
            elif key == 8:
                if len(text) > 0:
                    text.pop()
                    self.text = "".join(text)
            elif key == 32:
                text.append(" ")
                self.text = "".join(text)

    @staticmethod
    def draw_text(text, surface, font=pygame.font.SysFont("Times New Roman", 20), color=(0, 0, 0), x=0, y=0, middle = False):
        """
        :param text: what you want written
        :param surface: usually the program screen or any surface you want to draw on
        :param font: the font :)
        :param color: RGB color tuple
        :param x: Xpos
        :param y: Ypos
        :param middle: if the (x) is middle of object
        :return: returns the object it drew if you want it to interact with stuff
        """
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        if middle:
            textrect.midtop = (x, y)
        else:
            textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        return textrect
