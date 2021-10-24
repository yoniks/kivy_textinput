from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.lang import Builder
from unidecode import unidecode
from kivy.properties import ConfigParserProperty, ConfigParser, StringProperty, NumericProperty, ObjectProperty
from functools import partial
from kivy.uix.boxlayout import BoxLayout
import os
import sys

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

Builder.load_file('editor_text.kv')


class MyFirstWidget(RelativeLayout):
    txt_input = ObjectProperty(None)
    writing = StringProperty('')
    index_char = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__()
        self.focus = True

    def check_status(self):  # kivy TextInput hebrew support

         # col, row = self.txt_input.cursor
        vb = self.txt_input.cursor_index()
        col, row = self.txt_input.get_cursor_from_index(vb)
        lan_text = self.txt_input._lines[row]

        # print("point code: ", ord(lan_text[col]))
        print(vb, col, row)

        if len(lan_text) > col:
            point_code = ord(lan_text[col])
            if point_code == 32:  # if it's space
                return
            elif point_code == 58 | 10:  # if it's ':' or 'enter',for new line with '˅' or '˄'
                return
            elif point_code == 46:
                Clock.schedule_once(partial(self.set_cursor, self.txt_input,
                                            len(self.txt_input.text) + 1, row), 0)
            else:
                Clock.schedule_once(partial(self.set_cursor, self.txt_input, col, row), 0)
        else:
            Clock.schedule_once(partial(self.set_cursor, self.txt_input, col, row), 0)

    def set_cursor(self, instance, col, row, dt):
        l = self.txt_input.cursor_index()
        key = self.txt_input.cursor_offset()
        print("col: ", key, l)
        if key != 0:
            instance.cursor = (col, row)


class Application(App):
    def build(self):
        return MyFirstWidget()


if __name__ == '__main__':
    Application().run()
