""" Classes for the UI elements """
import pygame as pg
import image

class Ui:
    """ basic ui element """
    def __init__(self, image_name, image_dict, screen ,x, y):
        self.image = image_dict[image_name]
        self.rect = self.image.get_rect()
        self.rect.move(x,y)
        self.screen = screen
        self.viewport_rect = screen.get_rect()

    def set_viewport(self, viewport_rect):
        self.viewport_rect = viewport_rect

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def set_position(self,x,y):
        self.rect = self.rect.move(-self.rect.x,-self.rect.y)
        self.rect = self.rect.move(x,y)

    def render(self):
        """rendering with regards to a rect"""
        self.image.render_dynamic(self.screen, self.rect, self.viewport_rect)

class Text(Ui):
    """ static text """
    def __init__(self, font, text, x, y, screen,color=pg.Color("black")):
        text_image = font.render(text, True, color)
        self.image = image.Image(text, text_image)
        self.rect = self.image.get_rect()
        self.rect.move(x,y)
        self.screen = screen
        self.viewport_rect = screen.get_rect()

class TextBox(Ui):
    """ a box where you can write """
    def __init__(self, font, screen, input_box, text_color=pg.Color("black"), active_color=pg.Color("blue") ):
        self.rect = input_box
        #rect used for creating the perimeter around the textbox
        self.box_perimiter = pg.Rect(0,0, input_box.w-1, input_box.h-1)
        self.viewport_rect = screen.get_rect()
        self.font = font
        self.active = False
        self.screen = screen
        self.text_color = text_color
        self.active_color = active_color
        self.bg_color = pg.Color("white")
        self.text = ""
        self.text_changed = False
        self.textbox_surface = pg.Surface((self.rect.w , self.rect.h))
        self.update()

    def update(self):
        self.textbox_surface.fill(self.bg_color)

        width = 4
        if not self.active:
            pg.draw.rect(self.textbox_surface, self.text_color, self.box_perimiter, width)
            self.textbox_surface.set_at((self.rect.w-1, self.rect.h-1), self.text_color)
        else:
            pg.draw.rect(self.textbox_surface, self.active_color, self.box_perimiter, width)
            self.textbox_surface.set_at((self.rect.w-1, self.rect.h-1), self.active_color)
    
        self.textbox_surface.blit(self.font.render(self.text, True, self.text_color), (self.box_perimiter.x+5 , self.box_perimiter.y+5))
        
        self.image = image.Image("text_box_surface", self.textbox_surface)

    def if_clicked(self, pos):
        clicked = False
        if self.viewport_rect.collidepoint(pos):
            if self.rect.collidepoint(pos[0]-self.viewport_rect.x, pos[1]-self.viewport_rect.y):
                clicked = True
                # Toggle the active variable.
                self.change_state()
                self.update()
            else:
                self.deactivate()
                self.update()
        return clicked
    
    def update_text(self, text):
        if text != self.text:
            self.text = text
            self.text_changed = True

    def get_text(self):
        return self.text

    def change_state(self):
        self.active = not self.active

    def deactivate(self):
        self.active = False

    def render(self):
        if self.text_changed:
            self.update()
            self.text_changed = False
        self.image.render_dynamic(self.screen, self.rect,self.viewport_rect)

class Button(Ui):
    """ Toggable button"""
    def __init__(self, font, screen, button_box, text,value,text_color=pg.Color("black"),button_color=pg.Color("white") 
    ,active_color=pg.Color("blue"), active_text_color=pg.Color("white")):
        self.value = value
        self.font = font
        self.text = text
        self.screen = screen
        self.rect = button_box
        self.box_perimiter = pg.Rect(0,0, button_box.w-1, button_box.h-1)
        self.text_color = text_color
        self.active_color = active_color
        self.button_color = button_color
        self.active_text_color = active_text_color
        #show if the button has been pressed
        self.active = False
        #says if the button is functional, button can be turned off by making this false
        self.button_active = True
        self.button_surface = pg.Surface((self.rect.w , self.rect.h))
        self.update()
        self.viewport_rect = screen.get_rect()


    def set_color(self, text= None , button=None, active=None, active_txt = None):
        """ sets the color scheme"""
        if text is not None:
            self.text_color = text
        if button is not None:
            self.button_color = button
        if active is not None:
            self.active_color = active
        if active_txt is not None:
            self.active_text_color = active_txt

    def update(self):
        """ method that uppdates the image for the button"""
        if not self.active:
            self.button_surface.fill(self.button_color)
            text_img = self.font.render(self.text, True, self.text_color)
        else:
            self.button_surface.fill(self.active_color)
            text_img = self.font.render(self.text, True, self.active_text_color)

        pg.draw.rect(self.button_surface, self.text_color, self.box_perimiter, 4)
        self.button_surface.set_at((self.rect.w-1, self.rect.h-1), self.text_color)

        text_rect = text_img.get_rect(center=(self.rect.w/2, self.rect.h/2))
        
        self.button_surface.blit(text_img,text_rect)
        self.image = image.Image("button_surface", self.button_surface)


    def if_clicked(self, pos):
        """checks if the button has been clicked and toggles it if it has"""
        clicked = False
        if self.viewport_rect.collidepoint(pos):
            if self.rect.collidepoint(pos[0]-self.viewport_rect.x, pos[1]-self.viewport_rect.y):
                self.toggle()
                clicked = True
        return clicked

    def get_value(self):
        return self.value

    def toggle(self):
        """ Toggles the button if it is active"""
        if self.button_active:
            self.active = not self.active
            self.update()

    def detoggle(self):
        self.active = False
        self.update()

    def change_text(self, text):
        """ Changes the text in the button"""
        self.text = text
        self.update()

    def toggle_button_func(self):
        """ turnes the button on/off"""
        self.button_active = not self.button_active

class PressButton(Button):
    """ Pressable button that automaticly unpresses(not toggle )"""
    def __init__(self, font, screen, button_box, value,text,text_color=pg.Color("black"),button_color=pg.Color("white") 
    ,active_color=pg.Color("blue"), active_text_color=pg.Color("white")):

        #init from Button
        Button.__init__(self, font, screen, button_box, value, text,text_color=pg.Color("black"),button_color=pg.Color("white") 
        ,active_color=pg.Color("blue"), active_text_color=pg.Color("white"))
        self.time_of_press = 0

    #overwritten method
    def if_clicked(self, pos):
        """checks if the button has been clicked and toggles it if it has"""
        clicked = False
        if self.viewport_rect.collidepoint(pos):
            if self.rect.collidepoint(pos[0]-self.viewport_rect.x, pos[1]-self.viewport_rect.y):
                self.toggle()
                self.time_of_press = pg.time.get_ticks()
                clicked = True
        return clicked

    #overwritten method
    def render(self):
        """Rendering function that also chekcs if the picture should be updated"""
        time_spent_active = 70
        if (pg.time.get_ticks() - self.time_of_press ) > time_spent_active and self.active:
            self.detoggle()
            self.update()
        self.image.render_dynamic(self.screen, self.rect, self.viewport_rect)

class EditorObject(Ui):
    """ Image in the preview window """
    def __init__(self, image_name, image_dict, screen ,x, y):
        Ui.__init__(self, image_name, image_dict, screen ,x, y)
        self.color_key_dict = {}
        self.image_dict = image_dict
        self.text_fields_dict = {}
        self.number_dict = {}
        self.tag_list = []
        self.image_element_dict = {}
        self.final_image = self.image

    def render(self):
        self.final_image.render_dynamic(self.screen, self.rect, self.viewport_rect)

    def add_color_pair(self, color_key, color):
        self.color_key_dict[color_key] = color

    def remove_color_pair(self, color_key):
        self.color_key_dict.pop(color_key)

    def add_text(self, text, text_tag):
        self.text_fields_dict[text_tag] = text

    def remove_text(self, text_tag):
        self.text_fields_dict.pop(text_tag)
   
    def add_number(self, number_tag, number):
        self.number_dict[number_tag] = number
   
    def remove_number(self, number_tag):
        self.number_dict.pop(number_tag)

    def add_tag(self, tag):
        self.tag_list.append(tag)

    def remove_tag(self, tag_index):
        self.tag_list.pop(tag_index)

    def add_image(self, image_name):
        self.image_element_dict[image_name] = self.image_dict[image_name]

    def remove_image(self, image_name):
        self.image_element_dict.pop(image_name)
    
    # TODO: Implement the following three functions
    def update(self):
        pass

    def load_from_xml(self):
        pass

    def save_to_xml(self):
        pass

    def get_images(self):
        return self.image_element_dict.copy()

    def get_numbers(self):
        return self.number_dict.copy()

    def get_color_pairs(self):
        return self.color_key_dict.copy()

    def get_tags(self):
        return self.tag_list.copy()

class Decals(Ui):
    """ decorative/non-functional images """
    def __init__(self, image_name, image_dict, screen ,x, y):
        Ui.__init__(self, image_name, image_dict, screen ,x, y)


class Viewbox:
    """ A collection of UI elements that can be changed together """
    def __init__(self, x, y, w, h):
        self.viewport = pg.Rect(x,y,w,h)
        self.orp= (0,0)
        self.elements = []
    
    def add_ui_element(self, new_elem):
        new_elem.set_viewport(self.viewport)
        self.elements.append(new_elem)

    def remove_ui_element(self, elem):
        self.elements.remove(elem)

    def view_move(self, dx= 0, dy= 0):
        self.orp = (self.orp[0]+dx, self.orp[1]+dy)
        for elem in self.elements:
            elem.move(dx,dy)

    def box_move(self, dx= 0, dy= 0):
        self.viewport.move_ip(dx,dy)

    def get_elements(self):
        """ Returns the elements list, OBS it is not a copy"""
        return self.elements
    
    def get_viewport(self):
        return self.viewport

    #TODO IMPLEMENT PARTIAL RENDERING
    def render(self):
        for elem in self.elements:
            elem.render()

#TODO implement this, and a class for viewport
class SelectionList(Viewbox):
    """ List where you can make a selection """
    def __init__(self, x, y, w, h, font, screen,butt_w=200, butt_h=100):
        Viewbox.__init__(self, x, y, w, h)
        self.font = font
        self.screen = screen

        self.activated_selection = None
        self.std_butt = pg.Rect(0,0,butt_w,butt_h)
        self.decals = []
        self.scroll_speed = 30
        self.scroll_pos = 0

        #colors
        self.text_color = pg.Color("black")
        self.button_color = pg.Color("white")
        self.active_color = pg.Color("blue")
        self.active_text_color = pg.Color("white")
    
    def set_color(self, text= None , button=None, active=None, active_txt = None):
        """Sets the color for the selectionlist and changes all existing buttons to comply"""
        if text is not None:
            self.text_color = text
        if button is not None:
            self.button_color = button
        if active is not None:
            self.active_color = active
        if active_txt is not None:
            self.active_text_color = active_txt

        for elem in self.elements:
            elem.set_color(self.text_color,self.button_color,self.active_color, self.active_text_color)

        for elem in self.elements:
            elem.update()
        
    def set_scroll_speed(self, speed):
        self.scroll_speed = speed
    
    def get_active(self):
        return self.activated_selection
    
    def get_active_value(self):
        return self.activated_selection.value


    #add a limit, should probably be so the top button can't go up and the bottom button can't go down
    def if_scrolled(self,pos,button_value):
        if self.viewport.collidepoint(pos):
            if button_value == 5 and self.scroll_pos > self.viewport.h - self.std_butt.h * len(self.elements):
                self.view_move(dy=-self.scroll_speed)
                self.scroll_pos += -self.scroll_speed
                return True
            elif button_value == 4 and self.scroll_pos < 0:
                self.view_move(dy=self.scroll_speed)
                self.scroll_pos += self.scroll_speed
                return True
        return False

    def if_clicked(self, pos):
        """ a function that checks if it is clicked"""
        if self.viewport.collidepoint(pos):
            for button in self.elements:
                if button is not self.activated_selection:
                    clicked = button.if_clicked(pos)
                    if clicked and self.activated_selection is not None:
                        self.activated_selection.detoggle()
                        self.activated_selection = button
                        return True
                    elif clicked and self.activated_selection is None:
                        self.activated_selection = button
                        return True
        return False

    def add_button(self, butt_txt, butt_val):
        """ add a button to the list"""
        list_pixel_height = len(self.elements) * self.std_butt.h
        button_rect = self.std_butt.move(0,list_pixel_height + self.orp[1])
        button_element = Button(self.font, self.screen, button_rect, butt_txt, butt_val)
        button_element.set_viewport(self.viewport)   
        button_element.set_color(self.text_color, self.button_color, self.active_color, self.active_text_color)
        self.elements.append(button_element)

    def remove_button(self, butt_val):
        """ remove a button from the list"""
        for elem in self.elements:
            if elem.value == butt_val:
                self.elements.remove(elem)
                self.update_butt_pos()

    def update_butt_pos(self):
        """ correct the position of all buttons in the list""" 
        y_height = 0
        for elem in self.elements:
            elem.set_position(0 , y_height)
            y_height = y_height + self.std_butt.h

    def render(self):
        """ renders the elements and decals in the selectionlist"""
        for elem in self.elements:
            elem.render()
        for elem in self.decals:
            elem.render()