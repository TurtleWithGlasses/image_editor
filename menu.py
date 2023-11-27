import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self,parent):
        super().__init__(parent)
        self.grid(row=0,column=0,sticky="nsew",pady=10,padx=10)

        # tabs
        self.add("Position")
        self.add("Color")
        self.add("Effects")
        self.add("Export")

        PositionFrame(self.tab("Position"))
        ColorFrame(self.tab("Color"))
        EffectsFrame(self.tab("Effects"))
        ExportFrame(self.tab("Export"))

class PositionFrame(ctk.CTkFrame):
    def __init__(self,parent):        
        super().__init__(parent,fg_color="light grey")
        self.pack(expand=True,fill="both")
        SliderPanel(self,"Rotation")
        SliderPanel(self,"Zoom")

class ColorFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color="green")
        self.pack(expand=True,fill="both")
        SliderPanel(self,"Color")

class EffectsFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color="orange")
        self.pack(expand=True,fill="both")
        SliderPanel(self,"Effects")

class ExportFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color="purple")
        self.pack(expand=True,fill="both")
        SliderPanel(self,"Export")