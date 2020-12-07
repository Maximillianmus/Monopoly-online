""" module containing all the inout functions"""
import pygame as pg


def input(input_queue, c_clickables, c_rclickables,c_scrollables):
    for event in pg.event.get():
        input_value = None
        if event.type == pg.QUIT:
            input_queue.append("DONE")
        if event.type == pg.MOUSEBUTTONDOWN:
            input_value = mouse_input(event, c_clickables, c_rclickables,c_scrollables)

        if input_value is not None:
            input_queue.append(input_value)

def keyboard_input(event):
    pass

def mouse_input(event, c_clickables, c_rclickables,c_scrollables):
    """
    Handles all mosue input
    ALL clickables have to implement if_clicked(pos) and get_value,
    Right click has to implement if_rclicked(pos) and get_value,
    Scroll objects have ti implement if_scrolled(pos, button).
    """
    value = None
    if event.button == 1:
        for elem in c_clickables:
            if elem.if_clicked(event.pos):
                value = elem.get_value()
                break
    elif event.button == 2:
         for elem in c_rclickables:
            if elem.if_rclicked(event.pos):
                value = elem.get_value()
                break
    elif event.button == 4 or event.button == 5:
        for elem in c_scrollables:
            if elem.if_scrolled(event.pos, event.button):
                value = None
                break

    return value
