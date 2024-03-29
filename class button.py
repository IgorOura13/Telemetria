def cursor_is_over(x, y, width, height, cursor_position):  # Determines if the mouse cursor position in tuple (x,y) is over
    if cursor_position[0] > x and cursor_position[0] < x + width:
        if cursor_position[1] > y and cursor_position[1] < y + height:
            return True
    return False

font = pygame.font.Font('freesansbold.ttf', 16)

class button():
    def __init__(self, screen, color, x, y, width, height, text=''):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, outline=True): # Draw the Button
        if outline:
            pygame.draw.rect(self.screen, (0,0,0), (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            text = font.render(self.text, True, (0, 0, 0))
            (self.screen).blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def cursor_is_over(self, cursor_position): #Determines if the mouse cursor position in tuple (x,y) is over the button
        return cursor_is_over(self.x,self.y,self.width,self.height,cursor_position)
