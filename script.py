import qrcode
# TKinder for doing the GUI in Python its pre-installed
from tkinter import *
from tkinter import messagebox 
import os
#>>>>>>>>> QR Code Class >>>>>>>>>>>>>>#

qr = qrcode.QRCode(
	# takes in an integer from 1 to 40 to controls the size of the qrcode
	# the smaller the number the smaller the qrcode
    version=1, 
    # 7 % less error?
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    # how big the box should be
    box_size=15,
    # hwo thick the border should be
    border=5
    )

#>>>>>>>>> Creating the GUI >>>>>>>>>>>>>>>#

root = Tk()
root.title(" QRCode Generator")
root.config(bg = "#a1d0bc")
root.geometry("500x500")
root.resizable(0,0)

#>>> bear image

bear = PhotoImage(file = "baer.png")
baer_label = Label(root,image = bear, bg = "#a1d0bc").pack()

#>>> creating the Labels (Text)

user_text_input_message = Label(
	root,
	text = " Enter webside or text above. ",
	font = ("Cambria",11),
	bg = "#a1d0bc",
	fg = "black"
	).place(relx=.5, rely=0.2, anchor="center")

#>>> creating a input box

user_text_input = Entry(root, width = 30)
# pack Entry seperate
#!!!! Otherwise .get() is called on pack() and will return None
user_text_input.place(relx=.5, rely=0.16, anchor="center")

#>>> Button Class

def generate():
	global user_text_input
	user_input = user_text_input.get()
	if user_input == None:
		messagebox.showinfo(title = None,message = "Please enter webside or text.")
		user_text_input = Entry(root, font = ("Cambria",12)).place(x = 160,y = 75)
	else:
		#>>> creating the QR Code
		print(user_input)
		qr.add_data(user_input)
		print(user_input)
		qr_img = qr.make_image(fill_color="black", back_color="white")
		home_location = os.path.expanduser('~')
		desktop_location = (home_location + "\Desktop")
		save_location = (desktop_location + "\My_QRCode" + ".jpg")
		qr_img.save(save_location)
		#>>> showing it on the screen
		qr_pop_image = PhotoImage(file = save_location)
		qr_image_pop = Label(root,image = qr_pop_image,bg = "#a1d0bc",width = 300,height = 300).place(relx=.5, rely=0.54, anchor="center")
		messagebox.showinfo(title = None,message = "Your QRCode has been saved succesfully.")

def reset():
	# detining the entert text
	user_text_input.delete(0,END)
	# resting the qr image to None
	qr_image_pop = Label(root,image = None,bg = "#a1d0bc").place(relx=.5, rely=0.54, anchor="center")


#>>> creating the Generate and Reset Buttons

generate_button = Button(root,text = "Generate",font = ("Cambria",11),command = generate).place(x = 370,y = 66)
reset_button = Button(root,text = "Reset",font = ("Cambria",11),command = reset).place(relx=.5, rely=0.9, anchor="center")

#>>> creating emty preview

#qr_image_pop = Label(root,image = None,bg = "#a1d0bc").place(relx=.5, rely=0.54, anchor="center")

#>>> hornoble mentions

jule = Label(root,text = " for my lovely sis ",font = ("Cambria",8),bg = "#a1d0bc",fg = "white").place(x = 408,y = 475)

#>>> loop until exit
root.mainloop()
