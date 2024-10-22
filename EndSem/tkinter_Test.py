import tkinter as tk

from jupyterlab.extensions import entry

root= tk.Tk()
root.title("Test Gui")
root.geometry("1920x1080")

lable=tk.Label(root,text="Hello  ",font=('Arial',16))
lable.pack(pady=10)


button=tk.Button(root,text="Click Me", bg="red" ,fg="pink")
button.pack(pady=20)

entry=tk.Entry(root)
entry.pack(pady=20)

text=tk.Text(root, height=10, width=100)
text.pack(pady=20)

var = tk.IntVar()
check=tk.Checkbutton(root, text="I Agree To T&C",variable=var)
check.pack(pady=10)
root.mainloop()