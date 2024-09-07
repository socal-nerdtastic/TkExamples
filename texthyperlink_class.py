
import webbrowser
from functools import partial
import tkinter as tk

class HyperlinkText(tk.Text):
    """Add a method to the Text widget to insert a hyperlink"""
    links = 0
    def inserthyperlink(self, index, text, link):
        # currently does not support newlines in the text
        tagname = f"hyperlink{self.__class__.links}"
        self.__class__.links += 1
        self.tag_configure(tagname, foreground="blue", underline=True)
        self.tag_bind(tagname, '<Enter>', self.on_enter)
        self.tag_bind(tagname, '<Leave>', self.on_leave)
        self.tag_bind(tagname, '<1>', partial(self.on_click, link))
        if index.lower() == tk.END:
            start = self.index("end-1c")
        else:
            start = self.index(index)
        self.insert(start, text)
        row, col = start.split(".")
        self.tag_add(tagname, start, f"{row}.{int(col)+len(text)}")
    def on_enter(self, event=None):
        self.config(cursor="hand2")
    def on_leave(self, event=None):
        self.config(cursor="arrow")
    def on_click(self, link, event=None):
        webbrowser.open(link)

##DEMO
def demo():
    r = tk.Tk()
    t = HyperlinkText()
    t.insert(tk.END, "Check out the best ")
    t.inserthyperlink(tk.END, "python help site", "https://learnpython.reddit.com")
    t.insert(tk.END, " on the internet!")
    t.pack(fill=tk.X, expand=True)
    t.focus()
    r.mainloop()

if __name__ == "__main__":
    demo()
