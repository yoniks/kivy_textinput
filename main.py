from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.lang import Builder
from unidecode import unidecode
from kivy.properties import ConfigParserProperty, ConfigParser, StringProperty, NumericProperty, ObjectProperty
from functools import partial

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

Builder.load_file('editor_text.kv')


class MyWidget(RelativeLayout):
    txt_input = ObjectProperty(None)
    new_lines = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__()
        self.focus = True
        self.new_lines = 0
        # Clock.schedule_once(partial(self.set_cursor, self.txt_input, col, row), 1)

    def check_status(self):  # kivy TextInput hebrew support
        Clock.schedule_once(partial(self.set_cursor, self.txt_input), 0.0)
        Clock.schedule_once(partial(self.new_line, self.txt_input), 0.1)

    def set_cursor(self, instance, dt):
        """RTL or LTR it is doesn't matter,it is for language HEBREW or other 
        ,it's set the cursor to index-1 if your language of chars  written right to left,
           it's mean cursor move to left of text and change the default of the right ."""
        vb = instance.cursor_index()
        col, row = instance.get_cursor_from_index(vb)
        instance.cursor = (col - 1, row)  # when you input is cursor go right text mean to bigger index so
        # col-1 back it to left of 1 index
        return

    def new_line(self, instance, dt):
        """after the result, if you
           input "." so open new line,
            it mean end text Hebrew of cursor is left side and not right so i can't enter to
           new line i should add \n to it,
         """
        vb = instance.cursor_index()
        col, row = instance.get_cursor_from_index(vb)
        num_letters = instance._lines[row]
        print(col, row)

        if len(num_letters) > 1:  # if more one char
            print(num_letters[0], num_letters[col])
            print("point code: ", ord(num_letters[0]))
            code_point = ord(num_letters[col])
        else:  # else it just one char
            print(num_letters)
            code_point = num_letters
        print(code_point)
        if code_point == 46 or code_point == '.':  # if input "." cursor go to end line and than enter to new line
            # instance.cursor = (len(num_letters), row)
            instance.text += "\n"
            print("bigger", type(instance.text))
        self.new_lines = row


class Application(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    Application().run()
