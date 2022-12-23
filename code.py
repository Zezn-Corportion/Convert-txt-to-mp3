from gtts import gTTS # pip install gTTS
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os 

userlang = os.popen('systeminfo | findstr /B /C:"System Locale"').read()

root = Tk()

if "Arabic" in userlang :
    root.geometry("310x180")
    root.title("تحويل النص الى صوت")
else :
    root.geometry("310x155")
    root.title("Convert TXT to Mp3")

root.resizable(False,False)
root.config(background = "#202020")

root_file_path = Label()
root_text = Label()

def root_btcommand1():
    global root_file_path
    global root_text

    root_file_path["text"] = filedialog.askopenfilename()
    root_var1 = open(root_file_path["text"] , mode="r" , encoding="utf-8")
    root_text["text"] = root_var1.read()
    root_var1.close()

if "Arabic" in userlang :
    root_l4 = Label(root,text = ": لغة المستند" , bg="#202020" , fg = "#ffffff").place(x = 234 , y = 50)
    vals = ["Arabic" , "English" , "Fransh"]
    root_compo = ttk.Combobox(values=vals , width = 30)
    root_compo.place(x = 10 , y = 50)
else :
    root_l4 = Label(root,text = "Text Lang :" , bg="#202020" , fg = "#ffffff").place(x = 17 , y = 50)
    vals = ["Arabic" , "English" , "Fransh"]
    root_compo = ttk.Combobox(values=vals , width = 30)
    root_compo.place(x = 100 , y = 50)

def root_save():
    root_path_to_save = filedialog.asksaveasfilename()

    try :
        if (root_compo.get() == vals[0]):

            audio = gTTS(text=root_text["text"].replace(".mp3","") , lang = "ar" , slow=False)

            audio.save(root_path_to_save.replace(".mp3","").replace(".","") + ".mp3")

        elif (root_compo.get() == vals[1]) :

            audio = gTTS(text=root_text["text"].replace(".mp3","") , lang = "en" , slow=False)

            audio.save(root_path_to_save.replace(".mp3","").replace(".","") + ".mp3")
    
        elif (root_compo.get() == vals[2]) :

            audio = gTTS(text=root_text["text"].replace(".mp3","") , lang = "fr" , slow=False)

            audio.save(root_path_to_save.replace(".mp3","").replace(".","") + ".mp3")

    except :
        if "Arabic" in userlang :
            message_1 = messagebox.showinfo("Error","يرجى الاتصال بالانترنت")
        else :
            message_1 = messagebox.showinfo("Error" , "Please get online")

if "Arabic" in userlang :
    root_bt1 = ttk.Button(text = "فتح ملف النص" , command = root_btcommand1 , width = 15).place(x = 200 , y = 20 + 70)

    root_bt2 = ttk.Button(text = "حفظ الملف الصوتي" , command = root_save).place(x = 20 , y = 20 + 70)

    root_l1 = Label(root,text = "<-----|" , bg="#202020" , fg = "#ffffff").place(x = 140 , y = 20 + 70)

else :
    root_bt1 = ttk.Button(text = "Open TXT file" , command = root_btcommand1 , width = 15).place(x = 200 , y = 20 + 70)

    root_bt2 = ttk.Button(text = "Save Mp3 file" , command = root_save).place(x = 20 , y = 20 + 70)

    root_l1 = Label(root,text = "<-----------|" , bg="#202020" , fg = "#ffffff").place(x = 115 , y = 20 + 70)


if "Arabic" in userlang :

    root_lm1 = Label(root,text = "عندما تقوم بتحويل مستندات عربية الى ملفات صوتية قم " , bg="#202020" , fg = "red").place(x = 30 , y = 60 + 70)

    root_lm2 = Label(root,text = "بتشكيل النص ليتم نطقه بالشكل الصحيح" , bg="#202020" , fg = "red").place(x = 106 , y = 80 + 70)

else :
    root_lm1 = Label(root,text = " - This app need Internet" , bg="#202020" , fg = "red" , font=("Bold",10)).place(x = 10 , y = 60 + 70)

root_l0 = Label(text = "Convert txt To mp3" , height=2 , fg = "#ffffff" , bg = "#454567").pack(fill =X)

root.mainloop()
