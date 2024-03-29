import kivy

kivy.require('1.10.1')


from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.splitter import Splitter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput



class Toolbar(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text='Toolbar')
        self.label.color = [0,0,0,1]

        self.add_widget(self.label)

        # self.canvas.add(Color(0.58, 1, 0.97))
        # self.canvas.add(Rectangle(pos=self.pos, size=self.size))

        self.bind(pos=self.update_pos_size, size=self.update_pos_size)

    def update_pos_size(self, event, widget):
        self.canvas.before.add(Color(0.2313,0.349,0.596))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))
        


class ChatContainer(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.size_hint = (1, None)
        self.height = self.minimum_height
        self.spacing = 10
        # self.label = Label(text='Chat Container')
        # self.label.color = [0,0,0, 1]
        # self.add_widget(self.label)

        for i in range(20):
            chat = Chat(text=str(i), size_hint_y=None, height=70)
            self.add_widget(chat)


        self.bind(pos=self.update_pos_size, size=self.update_pos_size)
        self.bind(minimum_height=self.setter('height'))

    def update_pos_size(self, event, widget):
        self.canvas.before.add(Color(0.2313,0.349,0.596))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))


class ChatScrollView(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(ChatContainer())

#refactoring
class ChatSplitter(Splitter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sizable_from = 'right'
        self.min_size = 150
        self.max_size = 400
        self.add_widget(ChatScrollView())


class Chat(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(pos=self.update_pos_size, size=self.update_pos_size)
    
    def update_pos_size(self, event, widget):
        self.canvas.before.add(Color(0.4627,0.7137,0.9568))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))

class MessageContainer(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

        self.orientation = 'vertical'
        self.messages = Messages()
        self.messages.size_hint=(1,0.8)
        self.add_widget(self.messages)

        self.typing_area = TypingArea(send_message=self.send_message)
        self.typing_area.size_hint = (1, 0.2)
        self.add_widget(self.typing_area)

        self.bind(pos=self.update_pos_size, size=self.update_pos_size)

    def update_pos_size(self, event, widget):
        self.canvas.before.clear()
        self.canvas.before.add(Color(0.2313,0.349,0.596))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))


    def send_message(self, event):
        
        if self.count % 2 == 0:
            self.messages.add_widget(MessageSent(message=self.typing_area.text_box.text))
        else:
            self.messages.add_widget(MessageReceived(message=self.typing_area.text_box.text))

        self.typing_area.text_box.text = ''        
        self.count += 1


class TypingArea(BoxLayout):
    def __init__(self, send_message, **kwargs):
        super().__init__(**kwargs)

        self.text_box = TextInput(padding=[15,15,15,15], font_size=20)
        self.add_widget(self.text_box)
        self.text_box.size_hint=(0.7, 1)

        self.send_button = Button(text='Send', on_press=send_message)
        self.add_widget(self.send_button)
        self.send_button.size_hint=(0.3, 1)

class Messages(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.size_hint = (1, None)
        self.height = 150
        # self.add_widget(MessageReceived())
        # self.add_widget(MessageSent())


class Message(AnchorLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        self.size_hint = (1, None)
        self.height = 150
        
        # self.add_widget(self.text)


class Text(Label):

    def __init__(self, background, **kwargs):
        super().__init__(**kwargs)

        self.background = background

        self.bind(pos=self.update_pos_size, size=self.update_pos_size)

    def update_pos_size(self, event, widget):
        self.canvas.before.clear()
        self.canvas.before.add(Color(*self.background))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))


class MessageReceived(Message):

    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)

        self.anchor_x = 'left'

        self.text = Text(background=[0.96,0.96,0.96],text=message)
        self.text.color = [0,0,0, 1]
        self.text.size_hint = (None, 1)
        self.text.width = 250

        self.add_widget(self.text)


class MessageSent(Message):

    def __init__(self,message, **kwargs):
        super().__init__(**kwargs)

        self.anchor_x = 'right'

        self.text = Text(background=[0.5215,0.7764,0.8312], text=message)
        self.text.color = [0,0,0, 1]
        self.text.size_hint = (None, 1)
        self.text.width = 250

        self.add_widget(self.text)


class MainArea(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.spacing = 10

        self.chat_container = ChatSplitter()
        self.chat_container.size_hint = (.3, 1)
        self.message_container = MessageContainer()
        self.message_container.size_hint = (.7, 1)

        self.add_widget(self.chat_container)
        self.add_widget(self.message_container)


class Root(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.spacing = 10

        self.toolbar = Toolbar()
        self.toolbar.size_hint = (1, .1)

        self.main_area = MainArea()

        self.add_widget(self.toolbar)
        self.add_widget(self.main_area)


        self.bind(pos=self.update_pos_size, size=self.update_pos_size)

    def update_pos_size(self, event, widget):
        self.canvas.before.add(Color(0.7137,0.7921,0.9137,1))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))



class MyApp(App):

    #override class method
    def build(self):

        return Root()

app = MyApp()
app.run()