# This is a prgoram that will work as a card editor, it will be used to create cards for boardgames,
#  the cards will be created by making a XML entry in the card XML.
#  It will also save a picture that is the card itself.
import pygame as pg
import ui

# constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000



# this is  code that shows an implementation of a textbox,
# use this as a basis for the writing boxes for the game.
def main():
    """ This is the main function of the program """
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    type_time = pg.time.get_ticks()
    viewbox = ui.Viewbox(100, 200, 500, 500)
    

    text_box = ui.TextBox(font,screen, pg.Rect(100,200,500,32))
    viewbox.add_ui_element(text_box)

    button = ui.Button(font,screen,pg.Rect(100,300,200,50),"button","button")
    viewbox.add_ui_element(button)

    press_button = ui.PressButton(font,screen,pg.Rect(100,400,200,50),"pressButton","pressButton")
    viewbox.add_ui_element(press_button)

    selection_list = ui.SelectionList(100,200,200,600,font,screen,butt_h =60)
    selection_list.add_button("button1", "1")
    selection_list.add_button("button2", "2")
    selection_list.add_button("button3", "3")
    selection_list.add_button("button4", "4")
    selection_list.add_button("button5", "5")


    while not done:
        keys = pg.key.get_pressed()
        if active:
            if keys[pg.K_RETURN] and text != '':
                print(text)
                text = ''

            #not optimal soloution, it would be better if we first had a event that if activated started an if statment after some time that check if we are still holding the button
            elif keys[pg.K_BACKSPACE] and abs(type_time-pg.time.get_ticks()) > 200:
                type_time = pg.time.get_ticks()
                text = text[:-1]

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False

                # check if button is pressed
                button.if_clicked(event.pos)
                press_button.if_clicked(event.pos)
                # Change the current color of the input box.
                text_box.if_clicked(event.pos)
                #selection list, check if clicked
                selection_list.if_clicked(event.pos)


                color = color_active if active else color_inactive
            else:
                if active:
                    if event.type == pg.KEYDOWN and event.key != pg.K_RETURN and event.key != pg.K_BACKSPACE: 
                        text += event.unicode
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        selection_list.view_move(dy=-10)
                    elif event.key == pg.K_DOWN:
                        selection_list.view_move(dy=10)
                    elif event.key == pg.K_RIGHT:
                        selection_list.view_move(dx=10)
                    elif event.key == pg.K_LEFT:
                        selection_list.view_move(dx=-10)
                    elif event.key == pg.K_k:
                        selection_list.add_button("new button", "new")
                    elif event.key == pg.K_l:
                        selection_list.remove_button("3")
                    elif event.key == pg.K_c:
                        selection_list.set_color(pg.Color("purple"), pg.Color("yellow"),pg.Color("green"),pg.Color("brown"))


        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        text_box.update_text(text)
        #viewbox.render()
        selection_list.render()


        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()