from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import datetime
# from kivymd.uix.picker import MDDatePicker




class ToDoListApp(MDApp):
    def build(self):
        # setting theme
        self.theme_cls.primary_palette = "DeepPurple"

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()

