from tkinter import *
import tkinter.messagebox as box

col_bg = "#EEEEDB" # Background Col
col_fg = "#003b6f" # Foreground Col
col_im = "#da635d" # Important col
col_bt = "#088DA5" # Button Col
col_et = "#000b16" # Entry text
col_eb = "#DEDEB8" # Entry Background

def Hoff(ion, presh, preshu, temp, units, **input): 
    if units == "Celsius":
        kelvin = temp + 273.15
    elif units == "Kelvin":
        kelvin = temp
    elif units == "Fahrenheit":
        kelvin = (temp + 459.67) / 1.8
    else:
        return "Temp ERROR"

    if preshu == "L·atm/mol·K":
        persh_atm = presh
    elif preshu == "J/mol·K":
        persh_atm = presh * 0.0821
    else:
        return "Temp ERROR"

    if 'mol' in input:
        What_in = "Molarity"
        What_in_v = input['mol']
        What_in_u = "M"
        w_pot = (ion * What_in_v) * (kelvin * persh_atm)
        w_pot = (0 - w_pot) / 10
        What_out = "Water potenchal"
        What_v = w_pot
        Waht_u = "MPa"
    elif 'pot' in input:
        What_in = "Water potenchal"
        What_in_v = input['pot']
        What_in_u = "MPa"
        w_pot = (0 - What_in_v) * 10
        molarty = w_pot /(kelvin * persh_atm * ion)
        What_out = "Molarity"
        What_v = molarty
        Waht_u = "M"
    else:
        return "Args Error"

    out = f"Given a {What_in} of {What_in_v :,.{2}f} {What_in_u} \nWith Inputs:\n Number of Ions = {ion :,.{0}f} \n Temperature = {temp :,.{2}f} ({units}) \n Pressure = {presh :,.{2}f} {preshu}\n"
    out = out + f"\nGivs a {What_out} of {What_v :,.{2}f} {Waht_u}"
    return out

def not_float(value):
  try:
    float(value)
    return False
  except ValueError:
    return True


def valueGET(ion, presh, preshu, temp, units, molpot, mp):
    if ion == "" or presh == "" or temp == "" or molpot == "":
        box.showerror("Basic Error", "You Need to Write in the Boxes")
    elif not_float(ion) or not_float(presh) or not_float(temp) or not_float(molpot):
        box.showerror("Very Basic Error", "YOU NEED TO ENTER NUMBERS!!")
    elif 0 > float(ion) < 20:
        box.showerror("Time Error", "Inappropriate Number of ion")
    elif type(int(ion)) != int:
        box.showerror("Other Rep Error", "Ion Must be a Hole Number")
    elif float(temp) > 500:
        box.showerror("Rep Error", "Inappropriate Number for Temp")
    else:
        if float(presh) != 0.0831:
            box.showwarning("Warning", "You are not using the\ndefault pressure constant (0.0831 atm L/mol K or 8.314 J/mol*K)")
        if mp == "molarity":
            final = Hoff(float(ion), float(presh), str(preshu), float(temp), str(units), mol=float(molpot))
            box.showinfo("Answer", final)
        elif mp == "W potential":
            final = Hoff(float(ion), float(presh), str(preshu), float(temp), str(units), pot=float(molpot))
            box.showinfo("Answer", final)
        else:
            box.showerror("Unknown Error", "Weird?!?")


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background=col_bg)

        self.parent = parent
        self.parent.title("Hoff equation")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):

        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        quitButton = Button(self, text="Quit", fg=col_im, bg=col_fg,
            command=self.onQuest)
        quitButton.place(x=250, y=120)

        inform = Button(self, text="Calculate", fg=col_fg, bg=col_bt,
                        command=lambda: valueGET(inputs_ion.get(), inputs_pre.get(), pre.get(), inputs_temp.get(), opt.get(), inputs_m_p.get(), m_p.get()))
        inform.place(x=5, y=120)

        m_p = StringVar(self)
        m_p.set("molarity") # initial value
        lable_m_p = Label(self, text="Mol/Pot", fg=col_fg, bg=col_bg)
        lable_m_p.grid(row=1, column=1)
        inputs_m_p = Entry(self, bd =1, fg=col_et, bg=col_eb, width=8)
        inputs_m_p.grid(row=1, column=2)
        opt_m_p = OptionMenu(self, m_p, "molarity", "W potential")
        opt_m_p.grid(row=1, column=3)
        opt_m_p.config(bd=1,fg=col_fg, bg=col_bt)

        lable_ion = Label(self, text="No ions", fg=col_fg, bg=col_bg)
        lable_ion.grid(row=2, column=1)
        inputs_ion = Entry(self, bd =1, fg=col_et, bg=col_eb, width=8)
        inputs_ion.grid(row=2, column=2)
        inputs_ion.insert(0, 1)

        opt = StringVar(self)
        opt.set("Celsius") # initial value
        lable_opt = Label(self, text="Temperature", fg=col_fg, bg=col_bg)
        lable_opt.grid(row=3, column=1)
        inputs_temp = Entry(self, bd =1, fg=col_et, bg=col_eb, width=8)
        inputs_temp.grid(row=3, column=2)
        inputs_temp.insert(0, 25)
        option = OptionMenu(self, opt, "Celsius", "Kelvin", "Fahrenheit")
        option.grid(row=3, column=3)
        option.config(bd=1,fg=col_fg, bg=col_bt)

        pre = StringVar(self)
        pre.set("L·atm/mol·K") # initial value
        lable_pre = Label(self, text="Pressure", fg=col_fg, bg=col_bg)
        lable_pre.grid(row=4, column=1)
        inputs_pre = Entry(self, bd =1, fg=col_et, bg=col_eb, width=8)
        inputs_pre.grid(row=4, column=2)
        inputs_pre.insert(0, 0.0831)
        opt_pre = OptionMenu(self, pre, "L·atm/mol·K", "J/mol·K")
        opt_pre.grid(row=4, column=3)
        opt_pre.config(bd=1,fg=col_fg, bg=col_bt)

    def onQuest(self):
        result = box.askquestion("Quit", "Did you intend to Quit?\n")
        if result == 'yes':
            self.parent.quit()
            self.parent.destroy()
        else:
            return True

def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()

main()
