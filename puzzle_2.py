import threading
import Rfid_NP532
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Puzzle_2(Gtk.Window):

    def __init__(self):
        self.lector = Rfid_NP532.Rfid_NP532()

        #Creem la finestra
        Gtk.Window.__init__(self, title = "Puzzle2")
        Gtk.Window.set_default_size(self,200,50)
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(5)
        self.set_resizable(True)

        #Caixa que conté els dos widgets
        
        self.c_general = Gtk.Box(orientation = "vertical")
        self.add(self.c_general)
        
        ##Caixa que conté el label del uid (ho faig per organitzar la finestra)
        self.c_text = Gtk.Box()
        self.text = Gtk.Label(label = "\nPlease, login with your university card\n")
        #self.uidBox.pack_start(self.uidLabel, True, True, 0)
        self.c_text.add(self.text)

        #Caixa que conté els dos botons (clear i el botó temporal de close)
        #TODO: Eliminar la caixa abans de presentar
        
        self.c_boto = Gtk.Box()
        
        self.boto = Gtk.Button(label = "Clear")
        self.boto.connect("clicked", self.clear_uid)

        self.c_boto.pack_start(self.boto, True, True, 0)
        

        ##Afegim les subcaixes dins de la caixa principal
        self.c_general.pack_start(self.c_text, True, True, 0)
        self.c_general.pack_start(self.c_boto, True, True, 0)
        
        ##Threading
        thread = threading.Thread(target = self.scan_uid)
        thread.daemon = True
        thread.start()
    
    #funció que reinicia el thread per llegir el uid
    def clear_uid(self, widget):
        self.text.set_label('\nPlease, login with your university card\n')
        thread = threading.Thread(target = self.scan_uid)
        thread.start()

    #funció que crida el thread
    def scan_uid(self):
        uid = self.lector.read_uid()
        self.text.set_label("\n                     " + uid + "\n")


finestra = Puzzle_2()
finestra.show_all()
Gtk.main()
