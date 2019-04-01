import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput  
from kivy.uix.widget import Widget 

class MyGrid(GridLayout):
    def Compute(self,Equate):
        if Equate:
            try:
                self.display.text = str(eval(Equate))
            except:
                self.display.text = "Error X.X"
        


class Test(App):
    def build(self):
        return MyGrid()
    
if __name__ == "__main__":
    Test().run()