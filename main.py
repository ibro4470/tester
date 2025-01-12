from tkinter import*


windows2 = Tk()
windows2.geometry("300x300")
windows2.title("IGBO DICTIONARIES")
entry_text = Entry(windows2)
entry_text.pack()

result = StringVar()
result_label = Label(windows2, textvariable=result)
result_label.pack()
igbo_dictionary = {
    "stand": 'guo',
    "joy": 'onu',
    "healthy": 'ahu ike',
    "light": 'ohuru',
    "sit": 'nodu ala',
    "black": 'oji',
    "lies": 'ugha',
    "sickness": 'noria',
    "fire": 'oku',
    "come": 'bia',
    "child": 'nwa',
    "man": 'nweke',
    "cap": 'okpu',
    "house": 'ulo',
    "beans": 'agwa',
    "friend": 'enyi',
    "festival": 'emume',
    "crown": 'okpu eze',
    "clock": 'elekere',
}
def check(word):
    if word in igbo_dictionary:
        result.set(igbo_dictionary[word])
        print(igbo_dictionary[word])

    else:
        result.set("Not found")
        print("Not found")


igbo_button = Button(windows2, text="igbo", command=lambda: check(entry_text.get()))
igbo_button.pack()





windows2.mainloop()