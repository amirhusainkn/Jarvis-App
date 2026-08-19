from kivy.app import App
from kivy.uix.label import Label

class JarvisApp(App):
    def build(self):
        return Label(text='Jarvis AI Assistant Ready!')

if __name__ == '__main__':
    JarvisApp().run()
  
