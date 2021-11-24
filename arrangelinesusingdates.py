import re
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

def arangelinesusingdates(lines:list):
    ''' arange the lines in descending order using the dates.'''
    pattern = r"(\d+(-|/)\d+(-|/)\d+)"
    date_line_list = list()
    for line in lines:
        if date_s := re.search(pattern, line):
            date_g = date_s.group(1) #get the first group found
            date_d = datetime.strptime(date_g, r"%d/%m/%Y") #convert the string into a date. for sorting purposes
            date_line_list.append([date_d, line])
    
    date_line_list = sorted(date_line_list, key= lambda x : x[0], reverse=True) #sort using the dates
    line_list = [data[1] for data in date_line_list] #get only the lines and leave dates
    return line_list
        
master = tk.Tk()
master.title("A ranger")
master.geometry("400x400")     

text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=10, font=("Times New Roman", 9))
text_area.pack()
master.rowconfigure(1, weight=1)

def settextarea():
    '''retrieves the text in the text area, and arange them and re display'''
    linesinserted = text_area.get("1.0", tk.END).split('\n')
    arangedlines =  arangelinesusingdates(linesinserted)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.INSERT,  "" if not isinstance(arangedlines, list) else '\n'.join([ str(d) for d in arangedlines]))

button = tk.Button(master, text="Process", command=settextarea)
button.pack()
master.mainloop()
        

#can't process 20/12/21
