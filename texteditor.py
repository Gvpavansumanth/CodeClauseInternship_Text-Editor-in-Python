import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create the main window
window = tk.Tk()
window.title("Text Editor")
window.geometry("800x600")  # Set the initial window size

# Create a Text widget with scrollbars
txt = tk.Text(window, fg='purple', bg='light yellow', font=('Calibri', 14))
txt.pack(fill=tk.BOTH, expand=True)  # Use pack() with fill and expand options

# Create a function to open a file
def open_file():
    filepath = askopenfilename(filetypes=[("Text file", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt.delete("1.0", tk.END)
    with open(filepath, mode='r', encoding='utf-8') as input_file:
        text = input_file.read()
        txt.insert(tk.END, text)
        window.title(f'Text Editor - {filepath}')

# Create a function to save a file
def save_file():
    filepath = asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, mode='w', encoding='utf-8') as output_file:
        text = txt.get("1.0", tk.END)
        output_file.write(text)
        window.title(f'Text Editor - {filepath}')

# Create a menu
menu = tk.Menu(window)
window.config(menu=menu)

# Create a "File" menu with "Open" and "Save As" options
filemenu = tk.Menu(menu, tearoff=0)  # Disable tearoff
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save As...', command=save_file)

# Add a separator
filemenu.add_separator()

# Add an "Exit" option
filemenu.add_command(label='Exit', command=window.quit)

# Create a "Edit" menu with some basic editing options
editmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=lambda: txt.event_generate("<<Cut>>"))
editmenu.add_command(label='Copy', command=lambda: txt.event_generate("<<Copy>>"))
editmenu.add_command(label='Paste', command=lambda: txt.event_generate("<<Paste>>"))
editmenu.add_separator()
editmenu.add_command(label='Undo', command=lambda: txt.event_generate("<<Undo>>"))
editmenu.add_command(label='Redo', command=lambda: txt.event_generate("<<Redo>>"))

# Run the Tkinter main loop
window.mainloop()
