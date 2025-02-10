from tkinter import*


windows = Tk()
windows.geometry("300x300")
windows.title("EBIRA DICTIONARY")

window = Tk()
window.geometry("300x300")
window.title("EBIRA DICTIONARY")


entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

ebira_dictionary ={
        "them": 'enini',
        "believe" : 'oyidowu',
        "small bell": 'ikono',
        "tray": 'oda',
        "Bag": 'akoto',
        "spoon": 'iresi',
        "bed": 'odeh',
        "oigin": 'ovuvu',
        "beauty": 'ozoza',
        "man": 'onolu',
        "pulse": 'asunu',
        "cutlass": 'ukari',
        "cup": 'ako',
        "compound": 'ooba',
        "chair": 'ipeku',
        "room": 'akuu',
        "joy": 'iraje',
        "where": 'izovi',
        "also": 'bere',
        "and": 'oniri',
        "why": 'seve',
        "peace": 'engworo',
        "unity": 'evabe',
        "holy": 'onini',
        "no": 'heyiye',
}


def check(word):
        if word in ebira_dictionary:
            result.set(ebira_dictionary[word])
            print(ebira_dictionary[word])

        else:
            result.set("Not found")
            print("Not found")


ebira_button = Button(window)
ebira_button.config(text='check', command=lambda : check(entry_text.get().lower()))
ebira_button.pack()
window.mainloop()

windows.mainloop()