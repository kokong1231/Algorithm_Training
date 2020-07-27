from googletrans import Translator
from tkinter import *
import clipboard



######## 번역 동작 영역 ########

save_text = ""

def tranc(event):
    global save_text

    translator = Translator()
    result = translator.translate(str(entry.get()), dest="en")

    label.config(text=result.text)

    save_text = result.text

# print(result.text) ==> 번역 출력

######## 번역 동작 영역 ########


######## GUI 영역 ########

root = Tk()

root.title("Translator")
root.geometry("500x200+100+100")
root.resizable(False, False)

label = Label(root, text='Translator', width=500, height=6, fg="#000000", relief="solid", wraplength=200)
label.pack()


### 버튼 동작 ###

def countplus():
    clipboard.copy(save_text)

### 버튼 동작 ###



### Entry 생성 ###

entry = Entry(root, width=30)
entry.bind("<Return>", tranc)
entry.pack()

### Entry 생성 ###

button = Button(root, width=10, text="Copy", overrelief="solid", command=countplus)
button.pack()

root.mainloop()

######## GUI 영역 ########