# This Password Security Level Checker Created By Dr.Nick_Z

# Library

# Gui Library
from tkinter import*
# Variable #####################################################################################################

# Strings For Containing Symbols...

Small_Alpha=tuple("abcdefghijklmnopqrstuvwxyz")
Letter_Aplha=tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Integer_Number=tuple("1234567890")
Symbol_Define=tuple("`~!@#$%^&*()[]_-+=}|{:;'<,>./?")



# Function #######################################################################################################

# Function For Who Check Password Security Level
# We Created 4 security Level There ( 1. Low , 2. Medium , 3. Strong , 4. Highly Recommended )
def Password_Security_Level_Checker():

    ps=EntryBox.get()

    # Four Security Level
    
    # Condition For Low Level 
    # 1. (Password Lenght More Than 10)
    # 2. (Second Contion Is The Password Contain Only One Kind Of Symbol , Example ('abcdefghijkl','ABCDEFGHIJKLMNOP'))

    # Condition For Medium Level
    # 1. (Lenght More Than 10)
    # 2. (Contain Two Type Of Symbol , Example ('ABCdefGHijklmnop'))
    # 3. (Symbol Must Be Two Different In Lenght Two..)
    
    # Condition For Strong Level
    # 1. (Lenght More Than 10)
    # 2. (Contain Three Type Of Symbol , Example ('ABCabc12301'))
    # 3. (Symbol Must Be Two Different In Lenght Two..)

    # Condition For Highly Recommended
    # 1. (Lenght More Than 10)
    # 2. (Contain Four Type Of Symbol , Example ('ABCabc12301!@#'))
    # 3. (Symbol Must Be Two Different In Lenght Two..)

    # Local Variable For Some Logic Building
    # Logic Given Following Below With Description

    Ps_Security_Level_Checker=[]
    Small_Alpha_level=0
    Letter_Aplha_level=0
    Integer_Number_level=0
    Symbol_Define_level=0
    Security_Final_Level=0

    # Checking Security Level Of Password
    # Frist It Check Lenght Of Password If Password Lenght More Than Or Equal To 10 
    if (len(ps)>=8):


        # Than In For Loop Getting All Character Of Password
        for i in ps:

            # Frist Nested For Loop
            # This Find Small Alphabet In Password
            for j in Small_Alpha:
                if (i==j):
                    # If Small Alphabet Found In Password It Set +1 In Given Variable 
                    Small_Alpha_level+=1


            # Second Nested For Loop
            # This Find Capital Alphabet In Password
            for k in Letter_Aplha:
                if (i==k):
                    # If Capital Alphabet Found In Password It Set +1 In Given Variable 
                    Letter_Aplha_level+=1


            # Third Nested For Loop
            # This Find Number (0 to 9 ) In Password
            for h in Integer_Number:
                if (i==h):
                    # If Number Found In Password It Set +1 In Given Variable 
                    Integer_Number_level+=1


            # Fourth Nested For Loop
            # This Find Symbol Like (!@#$) In Password
            for u in Symbol_Define:
                if (i==u):
                    # If Symbol Found In Password It Set +1 In Given Variable 
                    Symbol_Define_level+=1


            # If Every Given Variable Get +2 I Will Add Sum Of All

            
            


    # If Sum Will Be 2 I Will Give OutPut As Low Level
    if (Small_Alpha_level>=2):
        Security_Final_Level+=2
    

    # If Sum Will Be 4 I Will Give OutPut As Medium Level
    if (Letter_Aplha_level>=2):
        Security_Final_Level+=2


    # If Sum Will Be 6 I Will Give OutPut As Strong Level
    if (Integer_Number_level>=2):
        Security_Final_Level+=2
    

    # If Sum Will Be 8 I Will Give OutPut As Highly Recommended Level
    if (Symbol_Define_level>=2):
        Security_Final_Level+=2

    
    # Seting Security Level Of Password

    # Low Level
    if (Security_Final_Level==2):
        progress.configure(image=pic_weak)
        level_label.configure(text="Weak", fg="red")


    # Medium Lvel
    if (Security_Final_Level==4):
        progress.configure(image=pic_medium)
        level_label.configure(text="Medium",fg="yellow")

    # Strong Level
    if (Security_Final_Level==6):
        progress.configure(image=pic_strong)
        level_label.configure(text="Strong", fg="aqua")

    # Highly Recommended Level
    if (Security_Final_Level==8):
        progress.configure(image=pic_highly_r)
        level_label.configure(text="Highly Recommended", fg="green")



    EntryBox.after(50,Password_Security_Level_Checker)

# Tkinter #############################################################################################################
root=Tk()
root.geometry("350x400+100+100")
root.maxsize(350,400)
root.minsize(350,400)
root.title("Password Security Checker V 2.0")
root.configure(bg="black")

# Images ############################################################################################################

C = Canvas(root, bg="black", height=60, width=60)
filename = PhotoImage(file = "anon.png")
imgFile = filename.subsample(4,4)
background_label = Label(root,image=imgFile,bg='black')
background_label.place(x=125, y=0)

C.pack()

progress_bar = Canvas(root, bg="black", height=20, width=40)
weak = PhotoImage(file = "weak.png")
pic_weak = weak.subsample(4,4)

medium = PhotoImage(file="medium x.png")
pic_medium = medium.subsample(4,4)

strong = PhotoImage(file="strong.png")
pic_strong = strong.subsample(4,4)

highly_r = PhotoImage(file="highly rem.png")
pic_highly_r = highly_r.subsample(4,4)

progress = Label(root,image=pic_weak,bg='black')
progress.place(x=55, y=190)

progress_bar.pack(padx=20,pady=80)


# Entry Box ##########################################################################################################

EntryBox= Entry(root,font=("arial",16,"italic bold"),relief="ridge",fg="blue")
EntryBox.focus_set()
EntryBox.place(x=55,y=140)

Password_Security_Level_Checker()


# Label ##############################################################################################################

level_label = Label(root,text="Weak" ,fg='red',bg="black",font=("arial",11,"italic bold"))
level_label.place(x=55,y=210)

root.mainloop()