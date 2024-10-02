from tkinter import*
from PIL import Image , ImageTk  # pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")



        #**********variables*************
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof= StringVar()
        self.var_id_number = StringVar()
        




        #*********title***********
        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS",font = ("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief = RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height =50)

         #******logo***********
        img2 = Image.open(r"C:\Users\nandk\OneDrive\Desktop\Python\Hotel_Management_System\images\1633410403702hotel-images\hotel images\logohotel.png")
        img2 = img2.resize((100,40),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root,image = self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)


        #******label frame**********
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text = "Customer details",font = ("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width = 425,height = 490)



        #******************labels and entries***********
        #cust ref 
        lbl_cust_ref = Label(labelframeleft,text="Customer Ref",font = ("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row = 0 , column = 0)
        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref,width = 22,font = ("ti",12,"bold"),state = "readonly")
        entry_ref.grid(row = 0 , column = 1 )#1922

        #cust name
        cname = Label(labelframeleft,text="Customer Name",font = ("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row = 1 , column = 0)
        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width = 22,font = ("arial",12,"bold"))
        txtcname.grid(row = 1 , column = 1 )


        #mother name
        lblmname = Label(labelframeleft,text="Mother Name",font = ("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row = 2 , column = 0)
        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_mother,width = 22,font = ("arial",12,"bold"))
        txtmname.grid(row = 2 , column = 1 )


        #gender combobox
        label_gender = Label(labelframeleft,text="Gender",font = ("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row = 3 , column = 0 , sticky = W)

        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,font = ("arial",12,"bold"),width = 22,state = "readonly")
        combo_gender["value"] = ("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row = 3 , column = 1)




       


       #postcode
        lblPostCode = Label(labelframeleft,text="PostCode",font = ("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row = 4 , column = 0)
        txtPostCode = ttk.Entry(labelframeleft,textvariable=self.var_post,width = 22,font = ("arial",12,"bold"))
        txtPostCode.grid(row = 4 , column = 1 )

        #mobilenumber
        lblMobile = Label(labelframeleft,text="Mobile",font = ("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row = 5 , column = 0)
        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile,width = 22,font = ("arial",12,"bold"))
        txtMobile.grid(row = 5 , column = 1 )

        #email
        lblEmail = Label(labelframeleft,text="Email",font = ("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row = 6 , column = 0)
        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email,width = 22,font = ("arial",12,"bold"))
        txtEmail.grid(row = 6 , column = 1 )



        #nationality
        lblNationality = Label(labelframeleft,text="Nationality ",font = ("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row = 7 , column = 0)

        combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font = ("arial",12,"bold"),width = 22,state = "readonly")
        combo_Nationality["value"] = ("Indian","American","Britist")
        combo_Nationality.current(0)
        combo_Nationality.grid(row = 7 , column = 1)




        # idproof type combobox
        lblIdProof = Label(labelframeleft,text="Id Proof Type ",font = ("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row = 8 , column = 0)

        combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font = ("arial",12,"bold"),width = 22,state = "readonly")
        combo_id["value"] = ("Aadhar Card","Driving License","Passport")
        combo_id.current(0)
        combo_id.grid(row = 8 , column = 1)



        



        #id number
        lblIdNumber = Label(labelframeleft,text="Id Number ",font = ("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row = 9 , column = 0)
        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_id_number,width = 22,font = ("arial ",12,"bold"))
        txtIdNumber.grid(row = 9 , column = 1 )



        #address
        lblIdAddress = Label(labelframeleft,text="Address ",font = ("arial",12,"bold"),padx=2,pady=6)
        lblIdAddress.grid(row = 10 , column = 0)
        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_address,width = 22,font = ("arial",12,"bold"))
        txtIdNumber.grid(row = 10 , column = 1 )


        #***************buttons*************
        btn_frame = Frame(labelframeleft,bd = 2  , relief=RIDGE)
        btn_frame.place(x = 0 , y = 400 , width = 412 , height = 40)

        btnAdd = Button(btn_frame,text = "Add",command = self.add_data,font = ("arial",12,"bold"),bg = "black",fg = "gold",width = 9 )
        btnAdd.grid(row = 0 , column = 0 ,padx=1)

        btnUpdate = Button(btn_frame,text = "Update",command=self.update,font = ("arial",12,"bold"),bg = "black",fg = "gold",width = 9 )
        btnUpdate.grid(row = 0 , column = 1 ,padx=1)

        btnDelete = Button(btn_frame,text = "Delete",command = self.mDelete,font = ("arial",12,"bold"),bg = "black",fg = "gold",width = 9 )
        btnDelete.grid(row = 0 , column = 2 ,padx=1)

        btnReset = Button(btn_frame,text = "Reset",command = self.reset,font = ("arial",12,"bold"),bg = "black",fg = "gold",width = 9 )
        btnReset.grid(row = 0 , column = 3 ,padx=1)

        #************table frame search system*****************
        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,text = "View Details and Search System",font = ("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width = 860,height = 490)


        lblSearchBy = Label(Table_Frame,text="Search By ",font = ("arial",12,"bold"),bg = "red" , fg = "white")
        lblSearchBy.grid(row = 0 , column = 0, sticky = W,padx = 2)

        self.search_var = StringVar()
        

        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var,font = ("arial",12,"bold"),width = 24,state = "readonly")
        combo_Search["value"] = ("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row = 0 , column = 1,padx = 2)

        self.txt_search = StringVar()

        txtSearch= ttk.Entry(Table_Frame,textvariable=self.txt_search,width = 24,font = ("arial",12,"bold"))
        txtSearch.grid(row = 0 , column = 2,padx = 2 )

        btnSearch = Button(Table_Frame,text = "Search",command = self.search,font = ("arial",12,"bold"),bg = "black",fg = "gold",width = 9 )
        btnSearch.grid(row = 0 , column = 3 ,padx=1)


        btnShowAll = Button(Table_Frame,text = "Show All",command = self.fetch_data,font = ("arial",12,"bold"),bg = "black",fg = "gold",width = 9 )
        btnShowAll.grid(row = 0 , column = 4 ,padx=1)


        #******************Show data table***********
        details_table = LabelFrame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width = 860,height = 350)

        scroll_x = ttk.Scrollbar(details_table,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient = VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table,column = ("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill=Y)

        scroll_x.config(command =self.Cust_Details_Table.xview)
        scroll_y.config(command = self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text = "Refer No.")
        self.Cust_Details_Table.heading("name",text = "Name")
        self.Cust_Details_Table.heading("mother",text = "Mother Name")
        self.Cust_Details_Table.heading("gender",text = "Gender")
        self.Cust_Details_Table.heading("post",text = "PostCode")
        self.Cust_Details_Table.heading("mobile",text = "Mobile")
        self.Cust_Details_Table.heading("email",text = "Email")
        self.Cust_Details_Table.heading("nationality",text = "Nationality")
        self.Cust_Details_Table.heading("idproof",text = "ID Proof")
        self.Cust_Details_Table.heading("idnumber",text = "ID Number")
        self.Cust_Details_Table.heading("address",text = "Address")
        
        self.Cust_Details_Table["show"]="headings"


        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill = BOTH , expand = 1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password="MySqlw3(1234)",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get()))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Successs","Customer has been added",parent = self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong: {str(es)}",parent = self.root)    

    def fetch_data(self):
         conn = mysql.connector.connect(host = "localhost",username = "root",password="MySqlw3(1234)",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from customer")
         rows = my_cursor.fetchall()
         if len(rows)!=0:
             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
             for i in rows:
                 self.Cust_Details_Table.insert("",END,values=i)
             conn.commit()   
         conn.close()   



    def get_cursor(self,event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]
        if len(row) >= 11:
         self.var_ref.set(row[0]) , self.var_cust_name.set(row[1]),self.var_mother.set(row[2]),self.var_gender.set(row[3]),self.var_post.set(row[4]),self.var_mobile.set(row[5]),self.var_email.set(row[6]),self.var_nationality.set(row[7]),self.var_id_proof.set(row[8]),self.var_id_number.set(row[9]) ,self.var_address.set(row[10])        
                 
    def update(self):

        if self.var_mobile.get() == "":
            messagebox.showerror("Error","Please enter mobile number ",parent = self.root)
        else:

             conn = mysql.connector.connect(host = "localhost",username = "root",password="MySqlw3(1234)",database="management")
             my_cursor=conn.cursor()
             my_cursor.execute("update customer set  name = %s, mother=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref = %s",(self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get(),self.var_ref.get()))
             conn.commit()
             self.fetch_data()
             conn.close()

             messagebox.showinfo("Update ","Customer details has been updated successfully",parent = self.root)


    def  mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System","Do you want to delete this customer ",parent = self.root) 
        if mDelete>0:
            conn = mysql.connector.connect(host = "localhost",username = "root",password="MySqlw3(1234)",database="management")
            my_cursor=conn.cursor()
            query = "delete from customer where ref = %s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()   


    def reset(self):
        # self.var_ref.set("")  # Reset reference number
        self.var_cust_name.set("")  # Reset customer name
        self.var_mother.set("")  # Reset mother's name
        # self.var_gender.set("")  # Reset gender
        self.var_post.set("")  # Reset postal code
        self.var_mobile.set("")  # Reset mobile number
        self.var_email.set("")  # Reset email
        # self.var_nationality.set("")  # Reset nationality
        # self.var_id_proof.set("")  # Reset ID proof type
        self.var_id_number.set("")  # Reset ID number
        self.var_address.set("") 


        
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):
        conn = mysql.connector.connect(host = "localhost",username = "root",password="MySqlw3(1234)",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values = i)
            conn.commit()   
        conn.close()     




             










if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
