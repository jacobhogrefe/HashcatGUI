import customtkinter as CTk

root = CTk.CTk()

menubar = CTk.Menu(root)

filemenu = CTk.Menu(menubar, tearoff=False)

filemenu.add_command(label="New", command=root.quit)

filemenu.add_command(label="Open", command=root.quit)

filemenu.add_command(label="Save", command=root.quit)

filemenu.add_separator()

filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

root.mainloop()