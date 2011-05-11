import feedparser

from Tkinter import *

class App:
  def __init__(self, master):
    frame = Frame(master, width=300, height=200)
    frame.pack()
    frame.pack_propagate(0)
    
    self.v = StringVar()
    self.getUpdate()
    
    self.msg = Message(frame, textvariable=self.v, width=260)
    self.msg.pack()
    
    bframe = Frame(frame, width=300, height=40)
    bframe.pack(side=BOTTOM)
    
    self.button = Button(bframe, text="QUIT", fg="red", command=frame.quit)
    self.button.pack(side=LEFT)
    
    self.update = Button(bframe, text="Update", command=self.getUpdate)
    self.update.pack(side=LEFT)
    
  def getUpdate(self):
    tweets = feedparser.parse('http://twitter.com/statuses/public_timeline.rss')
    self.v.set('\n' + tweets['entries'][0]['title'].encode("utf-8"))


def main():
  root = Tk()
  app = App(root)
  root.mainloop()

if __name__ == '__main__':
  main()
