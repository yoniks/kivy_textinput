from PIL import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import pytesseract
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock
from functools import partial
import os
import re
import logging

Builder.load_file('/{your path}/my.kv')
sm = ScreenManager()


## txt_in = self.ids['txt_input']

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Contracts(Screen):
    pass


class ScanFile(Screen):
    #   text_colour = ObjectProperty([1, 0, 0, 1])
    text_input = ObjectProperty(None)
    txt_input = ObjectProperty(None)
    pytesseract.pytesseract.tesseract_cmd = r'/{your path}/tesseract/tesseract'

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self._popup = None
        self.temp_text = None
        self.lan = None
        self.arr_temp = []
        self.result = []
        self.screen1 = kwargs['name']  # if i not use kwargm.get('name')
        self.text_input.text = ''
        self.txt_input.text = ''

        print(Screen)

    def test(self):
        sm.current = 'menu'

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        """load the file and send the text to method text_extraction"""

        print("LOAD: ", os.path.join(path, filename[0]))
        if '.png' in filename[0] or '.jpg' in filename[0]:
            img = Image.open(os.path.join(path, filename[0]))
            self.temp_text = pytesseract.image_to_string(img, lang='heb')  # eng
            print(self.temp_text)
            self.arr_temp = self.temp_text.split(' ')
            self.lan = self.check_language(self.temp_text)  # the highest char of percent language

            self.dismiss_popup()
        elif '.txt' in filename[0]:
            with open(os.path.join(path, filename[0])) as stream:
                self.temp_text = stream.read()
                self.lan = self.check_language(self.temp_text)
            self.dismiss_popup()
        else:
            print('not found')
            self.dismiss_popup()
        self.result = self.cut_chars_from_text(self.arr_temp,
                                               self.lan)  # clean this value from text @#$%^&*()_-+=!?<>,./\|"':;
        if 'heb' == self.lan:
            self.text_extraction_heb(self.result)  # check the contract,
            self.revers_index_char_heb(
                self.revers_index_list_heb(self.result))  # if hebrew, self.revers_index_list_heb(self.result)
        elif 'eng' == self.lan:
            self.text_extraction_eng(self.result)

    def cut_chars_from_text(self, arr_text, lan):  # heb or eng
        new_list = []
        for t0 in arr_text:  # text end to start text if hebrew
            temp_text = ""
            isLetter = False
            isNum = False
            for t in t0:
                # print(f"{t0[0]}:, {t0}")
                if lan == 'heb' and (1487 < ord(t) < 1515):  # heb
                    if isNum:
                        temp_text += ' '
                        isNum = False
                        new_list.append(temp_text)
                        temp_text = ""
                    temp_text += t
                    isLetter = True


                # elif lan == 'eng' and (
                #        (64 < ord(t) < 91) or (96 < ord(t) < 123) or (47 < ord(t) < 58) or (ord(t) == 64)):  # eng
                #    temp_text += t
                else:
                    if isLetter:
                        temp_text += ' '
                        isLetter = False
                        new_list.append(temp_text)
                        temp_text = ""
                    if 39 < ord(t) < 42 or ord(t) == 39 or ord(t) == 45 or ord(t) == 34 or ord(t) == 96:  # if -()'" `
                        temp_text += ' '
                    elif (47 < ord(t) < 58) or ord(t) == 44 or ord(t) == 46 or ord(t) == 37 or ord(
                            t) == 47:  # if it number or /,.%
                        temp_text += t
                        isNum = True

            if len(temp_text) == 1 and temp_text == ' ':
                print('pass')
            elif len(temp_text) > 0:
                new_list.append(temp_text)

        print("result: ", new_list)
        return new_list

    def revers_index_list_heb(self, list_temp):  # 2
        new_text = []
        # new_text.append(':טקסט שנבדק לא תמיד זהה למקור')
        # new_text.append('\n')
        print(f"before:{type(list_temp)},size: {len(list_temp)}, {list_temp} \n")
        for r in range(1, len(list_temp) + 1):  # start 1 to
            temp = ' '.join(list_temp[-r:len(list_temp):r])
            new_text.append(temp)  # if append so result to be list of list
        print(f"after: {new_text}")
        return new_text

    def revers_index_char_heb(self, text_in):  # 3

        result_arr = []
        for t in text_in:
            temp_text = ""
            for j in range(1, len(t) + 1):
                ch = t[-j:len(t):j]
                if (1487 < ord(ch) < 1515) or ch == ' ':
                    temp_text += t[-j:len(t):j]  # every char, end to:all word:just at index
                elif ch != ' ':  # it have to be some of .,/0-9
                    temp_text = t
                    break
            if len(temp_text) > 0:
                result_arr.append(temp_text)

        print("rev words: ", result_arr)
        temp1 = ""
        counter = 5
        for r in range(1, len(result_arr) + 1):  # revers the row
            temp1 += ' '.join(result_arr[-r:len(result_arr):r])
            temp1 += ' '
            if r == counter or r == len(result_arr):
                self.txt_input.text += temp1
                self.txt_input.text += "\n"
                temp1 = ""
                counter += 5
        # self.text_extraction_heb(self.txt_input.text)

        # Clock.schedule_once(partial(self.set_cursor, self.txt_input), 0.0)
        # Clock.schedule_once(partial(self.new_line, self.txt_input), 0.1)

    # @staticmethod
    def text_extraction_heb(self, text_file):  # 1
        """this method search in contact bad text and return it."""
        text_check = ['20%', 'שכר']
        for t in text_file:
            for ck in text_check:
                if ck in t:
                    for i in range(1, len(ck) + 1):
                        if 1487 < ord(t[i - 1]) < 1515:
                            self.text_input.text += ck[-i:len(ck):i]  # hebrew reves the word
                        else:
                            self.text_input.text += ck
                            break
                    self.text_input.text += '\n'

    def text_extraction_eng(self, check_text):
        check_list = ['yoni', '33']
        for t in check_text:
            for ck in check_list:
                if ck in t:
                    self.text_input.text += ck
                    self.text_input.text += '\n'

    def check_language(self, text):
        eng = 0
        heb = 0
        for t in text:
            if (ord(t) > 64 and ord(t) < 91) or (ord(t) > 96 and ord(t) < 123):
                eng += 1
            elif (ord(t) > 1487 and ord(t) < 1515):
                heb += 1
        if (eng / len(text)) * 100 > (heb / len(text)) * 100:
            print(f"language is English: {(eng / len(text)) * 100}")
            return 'eng'
        else:
            print(f"language is Hebrew: {(heb / len(text)) * 100}")
            return 'heb'

    def set_cursor(self, instance, dt):
        """RTL or LTR it is doesn't matter,it is for language HEBREW or other
        ,it's set the cursor to index-1 if your language of chars  written right to left,
           it's mean cursor move to left of text and change the default of the right ."""
        vb = instance.cursor_index()
        col, row = instance.get_cursor_from_index(vb)
        instance.cursor = (col - 1, row)

        return


class ScanApp(App):
    def build(self):
        sm.add_widget(Contracts(name='menu'))
        sm.add_widget(ScanFile(name='scan'))

        return sm


if __name__ == '__main__':
    ScanApp().run()
