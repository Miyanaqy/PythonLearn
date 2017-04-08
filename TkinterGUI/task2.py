from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.namesInput = Entry(self)
        self.namesInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.namesInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

def main():
    root = Tk()
    root.geometry("400x350+500+200")
        
    app = Application()
    app.master.title('Hello World')
    app.mainloop()

if __name__ == '__main__':
        main()
