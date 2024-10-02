from tkinter import*
from PIL import Image , ImageTk  # pip install pillow
from customer import Cust_Win
from room import Roombooking
from details import Details
import datetime 
from tkinter import messagebox


class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x900+0+0")
       

       #******first image**********
        img1 = Image.open(r"C:\Users\nandk\OneDrive\Desktop\Python\Hotel_Management_System\images\1633410403702hotel-images\hotel images\hotel1.png")
        img1 = img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = Label(self.root,image = self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=140)

        #******logo***********
        img2 = Image.open(r"C:\Users\nandk\OneDrive\Desktop\Python\Hotel_Management_System\images\1633410403702hotel-images\hotel images\logohotel.png")
        img2 = img2.resize((230,140),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root,image = self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=230,height=140)


        #*********title***********
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font = ("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief = RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height =50)


        #***********main frame*************
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        #********menu***************
        lbl_menu = Label(main_frame,text="MENU",font = ("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief = RIDGE)
        lbl_menu.place(x=0,y=0,width=230)


        #***********button frame*************
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=60,width=230,height=190)
        


        cust_btn = Button(btn_frame,text="CUSTOMER",command =self.cust_details, width=22,font = ("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0)
        

        room_btn = Button(btn_frame,text="ROOM",command = self.roombooking,width=22,font = ("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0)


        details_btn = Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font = ("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0)

        report_btn = Button(btn_frame,text="REPORT",command=self.developer_window, width=22,font = ("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0)

        logout_btn = Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font = ("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0)


        #************RIGHT SIDE IMAGE************

        img3 = Image.open(r"C:\Users\nandk\OneDrive\Desktop\Python\Hotel_Management_System\images\1633410403702hotel-images\hotel images\slide3.jpg")
        img3 = img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbling1 = Label(main_frame,image = self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=225,y=0,width=1310,height=590)





        #***********down images*********

        img4 = Image.open(r"C:\Users\nandk\OneDrive\Desktop\Python\Hotel_Management_System\images\1633410403702hotel-images\hotel images\myh.jpg")
        img4 = img4.resize((230,210),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbling1 = Label(main_frame,image = self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=230,width=230,height=210)


        img5 = Image.open(r"C:\Users\nandk\OneDrive\Desktop\Python\Hotel_Management_System\images\1633410403702hotel-images\hotel images\khana.jpg")
        img5 = img5.resize((230,190),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbling1 = Label(main_frame,image = self.photoimg5,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=420,width=230,height=190)
    

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)  

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = Details(self.new_window)  


     # Method to open the developer details window
    def developer_window(self):
        self.new_window = Toplevel(self.root)
        self.new_window.title("Developer Details")
        self.new_window.geometry("500x400")

        # Developer Info
        dev_info = Label(self.new_window, text="Developer: Devansh Soni", font=("times new roman", 20, "bold"), fg="blue")
        dev_info.pack(pady=10)

        # Developer Photo
        self.dev_photo = Image.open(r"C:\Users\nandk\OneDrive\Desktop\Python\Hotel_Management_System\images\1633410403702hotel-images\hotel images\developer_photo.png")
        self.dev_photo = self.dev_photo.resize((200, 200), Image.LANCZOS)
        self.dev_photo_image = ImageTk.PhotoImage(self.dev_photo)
        lbl_dev_photo = Label(self.new_window, image=self.dev_photo_image)
        lbl_dev_photo.pack(pady=10)

        # Generate Report button
        report_btn = Button(self.new_window, text="Generate Report", command=self.generate_report, font=("times new roman", 15, "bold"), bg="green", fg="white")
        report_btn.pack(pady=20)

    def generate_report(self):
        report_content = """Developer Report:
------------------------
Name: Devansh Soni
Contact: devanshsoni@example.com
Role: Lead Developer
Project: Hotel Management System
Date: {}
        """.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        with open("developer_report.txt", "w") as file:
            file.write(report_content)

        messagebox.showinfo("Success", "Report Generated Successfully!")
          
    

    def logout(self):
        self.root.destroy()













if __name__=="__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()

