import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # self.title("GUI")

        # You will first create a division with the help of Frame class and
        # align them on TOP and BOTTOM with pack() method.
        top_frame = self.pack()
        bottom_frame = self.pack(side="bottom")

        # Once the frames are created then you are all set to add widgets in both the frames.
        # 'fg or foreground' is for coloring the contents (buttons)
        btn1 = tk.Button(top_frame, text="Button1", fg="red").pack()
        btn2 = tk.Button(top_frame, text="Button2", fg="green").pack()
        # 'side' is used to left or right align the widgets
        btn3 = tk.Button(bottom_frame, text="Button3", fg="purple").pack(side="left")
        btn4 = tk.Button(bottom_frame, text="Button4", fg="orange").pack(side="left")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("GUI")
    root.geometry("500x400")
    app = Application(root)
    app.mainloop()
