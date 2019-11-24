import kivy

kivy.require('1.10.1')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label
from kivy.uix.button import Button


class Toolbar(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text='Toolbar')
        self.label.color = [0.58, 1, 0.97, 1]

        self.add_widget(self.label)


class ChatContainer(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text='Chat Container')
        self.label.background_color = [0.58, 1, 0.97, 1]
        self.add_widget(self.label)


class Chat(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MessageContainer(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text='Message Container')
        self.label.background_color = [0.58, 1, 0.97, 1]

        self.add_widget(self.label)


class Message(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainArea(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.chat_container = ChatContainer()
        self.chat_container.size_hint = (.3, 1)
        self.message_container = MessageContainer()
        self.message_container.size_hint = (.7, 1)

        self.add_widget(self.chat_container)
        self.add_widget(self.message_container)


class Root(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'

        self.toolbar = Toolbar()
        self.toolbar.size_hint = (1, .1)

        self.main_area = MainArea()

        self.add_widget(self.toolbar)
        self.add_widget(self.main_area)



class MyApp(App):

    #override class method
    def build(self):

        return Root()



app = MyApp()
app.run()