from Tkinter import *
import feedparser

class App:
  def __init__(self, master):
    master.wm_title("doink: the awesome twitter client")
    
    frame = Frame(master, width=360, height=200, bg='white')
    frame.pack()
    frame.pack_propagate(0)
    
    self.v = StringVar()
    self.msg = Message(frame, textvariable=self.v, width=260, bg='white')
    self.msg.pack()
    
    bframe = Frame(frame, width=300, height=40)
    bframe.pack(side=BOTTOM)
    
    self.button = Button(bframe, text="Quit", fg="red", command=frame.quit)
    self.button.pack(side=LEFT)
    
    self.update = Button(bframe, text="Update", command=self.refreshMsg)
    self.update.pack(side=LEFT)
    
    self.tweets = []
    self.getTweets()
    self.refreshMsg()
    
  def getTweets(self):
    feed = feedparser.parse('http://twitter.com/statuses/public_timeline.rss')
    for tweet in feed['entries']:
      self.tweets.append(tweet['title'].encode("utf-8"))
    print 'getting tweets...'
  
  def refreshMsg(self):
    if not self.tweets:
      self.getTweets()
    self.v.set('\n' + self.tweets.pop())
      

def main():
  root = Tk()       # create the root widget
  app = App(root)   # pass root widget to App
  root.mainloop()   # app will run while mainloop does

if __name__ == '__main__':
  main()
