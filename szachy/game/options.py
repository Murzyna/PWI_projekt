import pygame as pg
import sys

class Menu:
    def __init__(self):
        pg.init()

        self.screen_width = 800
        self.screen_height = 800
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Chess Game Menu")

        self.clock = pg.time.Clock()

        self.font_heading = pg.font.Font(None, 150)
        self.font_options = pg.font.Font(None, 80)
        self.heading = self.font_heading.render("Chess Game", True, (173, 216, 230))

        self.options = ["Player vs Player", "Player vs Bot"]
        self.selected_option = None

    def draw_menu(self):
        #Główne menu, zawierające nagłówek "Chess Game" oraz opcje gry: "Player vs Player", "Player vs Bot"
        self.screen.fill((0, 0, 0))

        heading_rect = self.heading.get_rect(center=(self.screen_width // 2, 80))
        self.screen.blit(self.heading, heading_rect)

        for i, option in enumerate(self.options):
            text = self.font_options.render(option, True, (173, 216, 230))  # Light blue text
            rect = text.get_rect(center=(self.screen_width // 2, 200 + i * 80))
            self.screen.blit(text, rect)

        pg.display.flip()

    def draw_color_selection(self):
        #Rysuje ekran wyboru koloru dla gracza (biały lub czarny) w przypadku wybrania opcji "Player vs Bot"
        self.screen.fill((0, 0, 0))

        heading_rect = self.heading.get_rect(center=(self.screen_width // 2, 80))
        self.screen.blit(self.heading, heading_rect)

        text_white = self.font_options.render("White", True, (173, 216, 230))
        rect_white = text_white.get_rect(center=(self.screen_width // 2, 300))
        self.screen.blit(text_white, rect_white)

        text_black = self.font_options.render("Black", True, (173, 216, 230))
        rect_black = text_black.get_rect(center=(self.screen_width // 2, 400))
        self.screen.blit(text_black, rect_black)

        pg.display.flip()

    def draw_bot_selection(self):
        #Rysuje ekran wyboru poziomu trudności - Dumb Bot lub Smart Bot w przypadku wybrania opcji "Player vs Bot" i wyboru koloru
        self.screen.fill((0, 0, 0))

        heading_rect = self.heading.get_rect(center=(self.screen_width // 2, 80))
        self.screen.blit(self.heading, heading_rect)

        text_dumb = self.font_options.render("Dumb Bot", True, (173, 216, 230))
        rect_dumb = text_dumb.get_rect(center=(self.screen_width // 2, 300))
        self.screen.blit(text_dumb, rect_dumb)

        text_smart = self.font_options.render("Smart Bot", True, (173, 216, 230))
        rect_smart = text_smart.get_rect(center=(self.screen_width // 2, 400))
        self.screen.blit(text_smart, rect_smart)

        pg.display.flip()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    for i, option in enumerate(self.options):
                        text_rect = self.font_options.render(option, True, (173, 216, 230)).get_rect(center=(self.screen_width // 2, 200 + i * 80))
                        if text_rect.collidepoint(mouse_pos):
                            self.selected_option = option
                            if self.selected_option == "Player vs Bot":
                                self.draw_color_selection()
                                return self.get_color_selection()
                            elif self.selected_option == "Bot vs Bot" or self.selected_option == "Player vs Player":
                                return self.selected_option

            self.draw_menu()
            self.clock.tick(30)

    def get_color_selection(self):
        #Funkcja obsługująca wybór koloru przez gracza. Oczekuje na kliknięcie myszą i zwraca informacje o wybranym kolorze
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    text_white_rect = self.font_options.render("White", True, (173, 216, 230)).get_rect(center=(self.screen_width // 2, 300))
                    text_black_rect = self.font_options.render("Black", True, (173, 216, 230)).get_rect(center=(self.screen_width // 2, 400))
                    if text_white_rect.collidepoint(mouse_pos):
                        self.selected_option += " - White"
                        self.draw_bot_selection()
                        return self.get_bot_selection()
                    elif text_black_rect.collidepoint(mouse_pos):
                        self.selected_option += " - Black"
                        self.draw_bot_selection()
                        return self.get_bot_selection()

            self.clock.tick(30)

    def get_bot_selection(self):
        #Funkcja obsługująca wybór poziomu trudności bota przez gracza. Oczekuje na kliknięcie myszą i zwraca informacje o wybranym bocie
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    text_dumb_rect = self.font_options.render("Dumb Bot", True, (173, 216, 230)).get_rect(center=(self.screen_width // 2, 300))
                    text_smart_rect = self.font_options.render("Smart Bot", True, (173, 216, 230)).get_rect(center=(self.screen_width // 2, 400))
                    if text_dumb_rect.collidepoint(mouse_pos):
                        self.selected_option += " - Dumb Bot"
                        return self.selected_option
                    elif text_smart_rect.collidepoint(mouse_pos):
                        self.selected_option += " - Smart Bot"
                        return self.selected_option

            self.clock.tick(30)

if __name__ == "__main__":
    menu = Menu()
    selected_option = menu.run()
    print(f"Selected option: {selected_option}")
