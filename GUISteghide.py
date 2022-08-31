import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import subprocess

def startgui():
	global window
	
	path_ef = ""
	path_cf = ""
	path_sf = ""
	passphrase = ""
	newfilename = ""
	
	def hide_1():
		open_button["state"] = "normal"
		menuretrieve["state"] = "disabled"
		textfiletohide["text"] = "Nascondi il file: "
	
	def retrieve_1():
		open_button2["state"] = "normal"
		menuhide["state"] = "disabled"
		openimagefor["text"] = "Apri l'immagine da cui estrarre il messaggio"
		
	def hide():
		global path_ef
		global path_cf
		global passphrase
		global newfilename
		passphrase = entrypass.get()
		newfilename = entryname.get()
		entrypass.delete("0", tk.END)
		entryname.delete("0", tk.END)
		subprocess.run(f"steghide embed -ef {path_ef} -cf {path_cf} -p {passphrase} -sf {newfilename}.jpg", shell=True)
		showinfo(
        title='Fatto!',
        message=f"Messaggio nascosto correttamente\nall'interno dell'immagine '{newfilename}'!"
    )
		refresh()
	
	def retrieve():
		global path_sf
		global passphrase
		passphrase = entrypass.get()
		entrypass.delete("0", tk.END)
		subprocess.run(f"steghide extract -sf {path_sf} -p {passphrase}", shell=True)
		showinfo(
        title='Fatto!',
        message="Messaggio estratto dall'immagine!"
    )
		refresh()
	
	def select_file_tohide():
	    global path_ef
	    filetypes = (
	        ('testo', '*.txt'),
	        ('audio', '*.wav')
	    )
	    filename = fd.askopenfilenames(
	    title='Testo o Audio da nascondere: ',
	    initialdir='/storage/emulated/0',
	    filetypes=filetypes)
	    danascondere["text"] = filename
	    imagetext["text"] = "\ndentro l'immagine: "
	    open_image["state"] = "normal"
	    path_ef = filename
	   
	def select_image():
	    global path_cf
	    global passphrase
	    global newfilename
	    filetypes = (
	        ('immagine', '*.jpg'),
	        ('all files', '.*')
	    )
	    filename = fd.askopenfilenames(
	    title='Immagine contenitore: ',
	    initialdir='/storage/emulated/0',
	    filetypes=filetypes)    
	    hide_button["state"] = "normal"
	    imagepath["text"] = filename
	    labelpass["text"] = "Inserisci la password: "
	    entrypass["state"] = "normal"
	    nfn["text"] = "Inserisci il nome del file finale: "
	    entryname["state"] = "normal"
	    path_cf = filename
	
	def select_image2():
	    global passphrase
	    global path_sf
	    filetypes = (
	        ('immagine', '*.jpg'),
	        ('all files', '.*')
	    )
	    filename = fd.askopenfilenames(
	    title='Immagine contenitore: ',
	    initialdir='/storage/emulated/0',
	    filetypes=filetypes)    
	    labelpass["text"] = "Inserisci la password: "
	    entrypass["state"] = "normal"
	    reveal_button["state"] = "normal"
	    imagepath["text"] = filename
	    path_sf = filename
	    passphrase = entrypass.get()
	
	window = tk.Tk()
	window.title("GUISteghide")
	window.configure(bg="black")
	
	title = tk.Label(text="STEGHIDE", bg="black", fg="green")
	title.pack(side=tk.TOP)
	
	frame1 = tk.Frame(window, bd=6, bg="green")
	frame1.pack()
	frame2 = tk.Frame(window, bg="black")
	frame2.pack()
	frame3 = tk.Frame(window, bg="black")
	frame3.pack()
	
	menuhide = ttk.Button(frame1, text="Nascondi", command=hide_1)
	menuhide.pack(side=tk.LEFT)
	
	menuretrieve = ttk.Button(frame1, text="Rivela", command=retrieve_1)
	menuretrieve.pack(side=tk.RIGHT)
	
	textfiletohide = tk.Label(frame2, bg="black", fg="white")
	textfiletohide.pack()
	
	open_button = ttk.Button(
	    frame2,
	    text='Apri File da nascondere',
	    command=select_file_tohide,
	    state="disabled"
	)
	open_button.pack(expand=True)
	
	openimagefor = tk.Label(frame2, bg="black", fg="white")
	openimagefor.pack()
	
	open_button2 = ttk.Button(
	    frame2,
	    text='Seleziona immagine',
	    command=select_image2,
	    state="disabled"
	)
	open_button2.pack(expand=True)
	
	danascondere = tk.Label(frame2, bg="black", fg="white")
	danascondere.pack()
	
	imagetext = tk.Label(frame2, bg="black", fg="white")
	imagetext.pack()
	
	open_image = ttk.Button(
	    frame2,
	    text='Scegli Immagine',
	    command=select_image,
	    state="disabled"
	)
	open_image.pack(expand=True)
	
	imagepath = tk.Label(frame2, bg="black", fg="white")
	imagepath.pack()
	
	labelpass = tk.Label(frame2, bg="black", fg="green")
	labelpass.pack()
	
	entrypass = tk.Entry(frame2, state="disabled")
	entrypass.pack()
	
	nfn = tk.Label(frame2, bg="black", fg="green")
	nfn.pack()
	
	entryname = tk.Entry(frame2, state="disabled")
	entryname.pack()
	
	empty = tk.Label(frame2)
	empty.pack()
	
	hide_button = ttk.Button(
	    frame2,
	    text='Nascondi',
	    command=hide,
	    state="disabled"
	)
	hide_button.pack(expand=True)
	
	reveal_button = ttk.Button(
	    frame2,
	    text='Rivela',
	    command=retrieve,
	    state="disabled"
	)
	reveal_button.pack(expand=True)
	
	emptyl = tk.Label(frame3, bg="black")
	emptyl.pack(side=tk.TOP)
	
	restart_button = ttk.Button(frame3, text="Ricomincia", command=refresh)
	restart_button.pack(side=tk.LEFT)
	
	exit_button = ttk.Button(frame3, text="Esci", command=exit)
	exit_button.pack(side=tk.RIGHT)
	
	window.mainloop()
	
def refresh():
	window.destroy()
	startgui()

startgui()