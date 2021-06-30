from tkinter import *
main_tikinter=Tk()
main_tikinter.title("")
main_tikinter.geometry("160x200+1+850")
main_tikinter.minsize(135,290)
main_tikinter.maxsize(135,290)
take_percent=""
take_coin_price=""
take_balance=""
take_quantity=""
def Calculate():
    take_percent = float(fee_percent.get())
    take_balance = float(balance_entry.get())
    take_quantity= float(quantity_entry.get())
    take_coin_price=float(coin_price_entry.get())

    fee = round(take_quantity * ((take_coin_price * take_percent) / 100), 2)
    available= (take_balance - fee)  # anti insufficient balance
    print(fee,available)
    print_fee = Label(main_tikinter, text="Fee: "+str(fee), fg="red", font="Helvetica 13")
    print_available= Label(main_tikinter, text="Available: "+str(available), fg="green", font="Helvetica 13")
    print_fee.place(rely=0.78, relx=0.025)
    print_available.place(rely=0.84, relx=0.025)
    print(take_percent,take_balance,take_quantity,take_coin_price)





    pass
def clear_text(event):
    event.widget.delete(0, "end")
#---------------------------------------------------------------------------------------------
balance=Label(main_tikinter, text="Your Balance", fg="green", font="Helvetica 12")
balance_entry=Entry(main_tikinter,width=15, fg="gray22", font="Helvetica 12")
if (len(take_percent) == 0):
    balance_entry.insert(0, "3000")
    balance_entry.bind("<FocusIn>", clear_text)
else:
    balance_entry.insert(0, take_percent)


balance.place(rely=0.0155, relx=0.04)
balance_entry.place(rely=0.072, relx=0.050)
# ---------------------------------------------------------------------------------------------
coin_price = Label(main_tikinter, text="Coin Price", fg="green", font="Helvetica 12")
coin_price_entry = Entry(main_tikinter, width=15, fg="gray22", font="Helvetica 12")
if (len(take_coin_price) == 0):
    coin_price_entry.insert(0, "34543.00")
    coin_price_entry.bind("<FocusIn>", clear_text)
else:
    coin_price_entry.insert(0, take_percent)

coin_price.place(rely=0.18, relx=0.04)
coin_price_entry.place(rely=0.235, relx=0.05)

# ---------------------------------------------------------------------------------------------

percent=Label(main_tikinter, text="Fee Percentage", fg="green", font="Helvetica 12")
fee_percent=Entry(main_tikinter,width=15, fg="gray22", font="Helvetica 12")
if (len(take_percent) == 0):
    fee_percent.insert(0, "0.35")
    fee_percent.bind("<FocusIn>", clear_text)
else:
    fee_percent.insert(0, take_percent)

percent.place(rely=0.347, relx=0.04)
fee_percent.place(rely=0.406, relx=0.050)
#---------------------------------------------------------------------------------------------

quantity=Label(main_tikinter, text="Quantity", fg="green", font="Helvetica 12")
quantity_entry=Entry(main_tikinter,width=15, fg="gray22", font="Helvetica 12")
if (len(take_quantity) == 0):
    quantity_entry.insert(0, "0.0434")
    quantity_entry.bind("<FocusIn>", clear_text)
else:
    quantity_entry.insert(0, take_percent)


quantity.place(rely=0.508, relx=0.04)
quantity_entry.place(rely=0.565, relx=0.050)
# ---------------------------------------------------------------------------------------------

Calculate=Button(main_tikinter,text="Calculate",width=10,fg="gray22",font="Helvetica 11",highlightbackground="#89DA8F",command=Calculate)
Calculate.place(rely=0.675, relx=0.21)
main_tikinter.mainloop()