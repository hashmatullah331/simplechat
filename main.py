import kivy

kivy.require('1.10.1')


from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label
from kivy.uix.button import Button



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
        self.canvas.before.add(Color(0.30,1,0.88))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))
        


class ChatContainer(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text='Chat Container')
        self.label.color = [0,0,0, 1]
        self.add_widget(self.label)

        self.bind(pos=self.update_pos_size, size=self.update_pos_size)

    def update_pos_size(self, event, widget):
        self.canvas.before.add(Color(0.30,1,0.88))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))


class Chat(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MessageContainer(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text='Message Container')
        self.label.color = [0,0,0, 1]

        self.add_widget(self.label)

        self.bind(pos=self.update_pos_size, size=self.update_pos_size)

    def update_pos_size(self, event, widget):
        self.canvas.before.add(Color(0.30,1,0.88))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))


class Message(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainArea(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.spacing = 10

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
        self.spacing = 10

        self.toolbar = Toolbar()
        self.toolbar.size_hint = (1, .1)

        self.main_area = MainArea()

        self.add_widget(self.toolbar)
        self.add_widget(self.main_area)


        self.bind(pos=self.update_pos_size, size=self.update_pos_size)

    def update_pos_size(self, event, widget):
        self.canvas.before.add(Color(0.34,0.03,1,1))
        self.canvas.before.add(Rectangle(pos=self.pos, size=self.size))



class MyApp(App):

    #override class method
    def build(self):

        return Root()



app = MyApp()
app.run()