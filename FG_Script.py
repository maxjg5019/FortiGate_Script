import tkinter as tk

def make_Command():
    text = inputArea.get('1.0', 'end-1c')
    textArray = text.split('\n')
    testButton['state'] = 'disabled'
    print(text)
    print(textArray)


window = tk.Tk()
window.title('FortiGate 批量指令生成腳本')
window.geometry('400x450')
window.resizable(False,False)

radioVar = tk.IntVar()
radio_Subnet = tk.Radiobutton(text='產出 Subnet',variable=radioVar,value=1,font=('Times New Roman',10))
radio_FQDN = tk.Radiobutton(text='產出 FQDN',variable=radioVar,value=2,font=('Times New Roman',10))
radio_Subnet.place(x=50,y=20,anchor='nw')
radio_FQDN.place(x=350,y=20,anchor='ne')
radio_Subnet.select()

testButton = tk.Button(text='產出指令',command=make_Command,font=('Times New Roman',14))
testButton.pack(side='bottom',fill='x',pady=15,padx=15)
testButton.config(bg='#99ff99')

inputArea = tk.Text(window,width=40,height=20)
inputArea.place(x=200,y=120,anchor='n')

window.mainloop()
