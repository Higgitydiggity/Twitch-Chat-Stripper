# seamus forscutt python Twitch chat splicer 1.0
# 20/06/2023-21/06/2023
# read a .txt file with raw chat copy/paste and output spliced
# twitch messages for organised input elsewhere.
# copy/paste twich chat into .txt file. 
# make sure that a time stamp is in the first line of .txt file
# open application and choose the desired .txt file.
# output to TCS-Output.txt   
import tkinter as tk
from tkinter import * 
from tkinter import filedialog as fd
import os 


class TwitchChatStripper(tk.Frame): 
#       initilises window        
        def __init__(self, master=None):
                tk.Frame.__init__(self,master)
                self.init_window()
#       set labels and buttons
        def init_window(self):
                self.pack(fill=tk.BOTH, expand=1)
                self.choosefile_label= Label(self,text='Choose ".txt" file to Strip')
                self.choosefile_label.pack()
                self.choosefile_button = Button(self, text='Find File', command=self.open_file)
                self.choosefile_button.pack()
                self.stripfile_button = Button(self, text= 'Strip Chat log', command= self.strip_file)
                self.stripfile_button.pack()
                self.finish_label=Label(self, text='waiting for file selection...')
                self.finish_label.pack()
                self.quit_button = Button(self, text="Quit", command=TCS_app.destroy)
                self.quit_button.pack()
#       function to strip unwanted text for raw twitch chat copy/paste
        def strip_file(self):
                self.contents = self.file_In.read()
                self.content_lines = self.contents.split('\n')
                self.content_slice1 = self.content_lines[2::]
                self.content_slice2 = self.content_slice1[0::4]
                file_OUT = open('TCS_Output.txt', 'w')
                for line in self.content_slice2:
                        line = line.partition(':')[2]
                        data = ''.join(line)
                        file_OUT.write(data)  
                        file_OUT.write('\n')
                self.finish_label['text'] = 'Finished!'
                os.startfile('TCS_Output.txt')
#       open file directory funtion        
        def open_file(self):
                filetypes = (('Text files', '*.txt'),('All files', '*.*'))
                file_name = fd.askopenfilename(filetypes=filetypes,initialdir="")
                self.file_In = open(file_name)
                print('Selcted: ', file_name)
               
        
# main tkinter app specifications         
TCS_app = tk.Tk()
TCS_app.title ('Twitch Chat Stripper 1.0') 
TCS_app.geometry("300x200")
app = TwitchChatStripper(TCS_app)
TCS_app.mainloop()







      





 

