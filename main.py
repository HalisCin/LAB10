from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Se 226')
root.geometry("500x500")


def open_txt():
    my_text.delete("1.0",END)
    text_file = open("C:\\Users\\halis\\Desktop\\Marvelll.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def calculate_txt():
    my_text.delete("1.0", END)
    text_file = open("C:\\Users\\halis\\Desktop\\Marvelll.txt", 'r').read()

    dictionary = {}

    lst = text_file.split()
    for elements in lst:
        dictionary[elements] = 0

    for elements in lst:
        if elements[-1] == '.':
            elements = elements[0:len(elements) - 1]

        if elements in dictionary:
            dictionary[elements] += 1

        else:
            dictionary.update({elements: 1})

    for allKeys in dictionary:
        print("\"", allKeys, "\"", end=" ")
        print(dictionary[allKeys], end=" ")
        print()
        str_ = (allKeys, "=", (dictionary[allKeys]))
        my_text.insert(END, str_)
        my_text.insert(END, "\n")


my_text = Text(root, width=40, height=10, font=("helvetica", 16))
my_text.pack(pady=20)

open_button = Button(root, text="Read Text File", command=open_txt)
open_button.pack(pady=20)

calculate_button = Button(root, text="Calculate Text File", command=calculate_txt)
calculate_button.pack(pady=20)

root.mainloop()
