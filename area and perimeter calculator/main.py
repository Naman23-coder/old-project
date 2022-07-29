from tkinter import *


root = Tk()

root.geometry('655x455')
root.minsize(655,455)
root.maxsize(655,455)
root.title('area and perimeter calculator')
sides = StringVar()
rectangle_height = StringVar()
rectangle_width = StringVar()
ourheight = StringVar()
breadth = StringVar()
a = StringVar()
b = StringVar()
c = StringVar()
radius = StringVar()
pi = 3.14159

def circle():

    circle_screen = Toplevel()
    def submitting():
        if radius.get().isdigit():
            asli_raduis = int(radius.get())
            a =  pi * (asli_raduis * asli_raduis)

            b200 = Label(circle_screen,text=f"the area is {a} cm ")
            b200.place(x=250,y=95)
    circle_screen.geometry('655x455')
    circle_screen.minsize(655, 455)
    circle_screen.maxsize(655, 455)
    circle_screen.title('Circle')
    Label(circle_screen, text='Circle').pack()
    Label(circle_screen, text='radius in cm').place(x=10, y=25)
    b100 = Entry(circle_screen, textvariable=radius)
    b100.place(x=80, y=25)
    #Button(circle_screen,text='Reset',command=reset).place(x=280,y=25)
    Button(circle_screen, text='Submit', command=submitting).place(x=210, y=25)


def square():

    def submit():

        if sides.get().isdigit():
            loli = int(sides.get())
            lol = loli + loli + loli + loli
            area = loli * loli
        print(sides)
        b1 = Label(top,text=f"the perimeter is {lol} cm")
        b1.grid()
        b2 = Label(top,text=f"the area is {area} sq.cm").grid()
    top = Toplevel()
    top.geometry('655x455')
    top.minsize(655,455)
    top.maxsize(655,455)
    top.title('Square')
    Label(top,text='Square').grid(row=0,column=5)
    bi= Label(top,text='Dimension of all sides in cm')
    bi.grid(row=3,column=0)
    btt=Entry(top,textvariable=sides)
    btt.grid(row=3,column=3)
    Button(top,text='submit',command=submit).grid(row=3,column=5,pady=5,padx=5)
    btt.set = 0

def Rectangle():

    def submit1():
        if rectangle_height.get().isdigit():
            height = int(btt1.get())
        if rectangle_width.get().isdigit():
             width = int(btt2.get())
        perimeter_rectangle = 2*(height+width)

        area_rectangle = height * width
        print(btt2)
        b3 =Label(top1,text= f"the perimeter is {perimeter_rectangle} cm")
        b3.grid(row=5,column=7)
        b4=Label(top1,text=f"the area is {area_rectangle} sq.cm").grid(row=6,column=7)
    top1= Toplevel()
    top1.geometry('655x455')
    top1.minsize(655,455)
    top1.maxsize(655,455)
    Label(top1,text='Rectangle').grid(row=0,column=66, pady=5,padx=5)
    bi= Label(top1 ,text='Height in cm')
    bi.grid(row=2,column=3)
    btt1=Entry(top1,textvariable= rectangle_height)
    btt1.grid(row=2,column=4)
    bi= Label(top1,text='Breadth in cm')
    bi.grid(row=3,column=3)
    btt2=Entry(top1,textvariable= rectangle_width)
    btt2.grid(row=3,column=4)
    Button(top1,text='submit',command=submit1).grid(row=4,column=4)
    btt2.set = 0




def triangle():

    def submit2():
        if ourheight.get().isdigit():
            height1 = int(ourheight.get())
            if breadth.get().isdigit():
                base = int(breadth.get())
                if a.get().isdigit():
                    aside = int(a.get())
                    if b.get().isdigit():
                        bside = int(b.get())

                        if c.get().isdigit():
                            cside = int(c.get())
                        area = (height1 / 2) * base
                        perimeter = aside + bside + cside
                        Label(triangleq,text=f"{area} cm").grid()
                        Label(triangleq,text = f"{perimeter} cm").grid()
    triangleq= Toplevel()
    triangleq.geometry('655x455')
    triangleq.minsize(655,455)
    triangleq.maxsize(655,455)
    Label(triangleq,text='Triangle').grid(column=9)
    Label(triangleq,text="Height in cm").grid(row=5)
    Entry(triangleq,textvariable=ourheight).grid(row=5,column=2)
    Label(triangleq,text="Base in cm").grid(row=6)
    Entry(triangleq,textvariable=breadth).grid(row=6,column=2)
    Label(triangleq,text="a side in cm").grid(row=7)
    Entry(triangleq,textvariable=a).grid(row=7,column=2)
    Label(triangleq,text="b side in cm").grid(row=8)
    Entry(triangleq,textvariable=b).grid(row=8,column=2)
    Label(triangleq,text="c side in cm").grid(row=9)
    Entry(triangleq,textvariable=c).grid(row=9,column=2)
    Button(triangleq,text="submit", command=submit2).grid(column=8)


Label(root, text='Area and Perimeter Calculator').place(x=300,y=10,anchor="center")
Button(root, text='Circle',command=circle).place(x=30,y=45)
Button(root, text='triangle',command=triangle).place(x=110,y=45)
Button(root, text='Square',command=square).place(x=185,y=45)
Button(root, text='Rectangle',command=Rectangle).place(x=250,y=45)

root.mainloop()
