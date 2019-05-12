import pandas as pd
import numpy as np
import tkinter as tk
from os import listdir


class Dictionary:
    def __init__(self, master, lang):
        self.master = master
        self.lang = lang
        
        self.filelist = sorted([f for f in listdir(lang) if f.endswith('.csv')])
        
        self.ipadx = 10
        self.ipady = 5
        self.padx = 10
        self.pady = 5
        
        self.bright = '#fffa66'
        self.solid = '#e2fcfb'
    
    def start(self):
        self.master.title('words to learn')
        self.master.geometry('800x300')
        
        self._create_frame()
            
        self.modeVar = tk.StringVar(self.mainframe)
        modes = ['meaning', 'word']
        self.modeVar.set(modes[0])
        tk.Label(self.mainframe, text='which card would you like to see first').grid(row=0, sticky=tk.W)
        tk.OptionMenu(self.mainframe, self.modeVar, *modes).grid(row=0, column=1, sticky=tk.E,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
        
        self.chapterVar = tk.StringVar(self.mainframe)
        chapters = self.filelist[:]
        chapters.append('all')
        self.chapterVar.set(chapters[0])
        tk.Label(self.mainframe, text='choose chapter to practice').grid(row=1, sticky=tk.W)
        tk.OptionMenu(self.mainframe, self.chapterVar, *chapters).grid(row=1, column=1, sticky=tk.E,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
        
        tk.Button(self.mainframe, text='start', command=self._start).grid(row=2, column=1, sticky=tk.E,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)

    def _start(self):
        self.chapter = self.chapterVar.get()
        self.mode = self.modeVar.get()
        
        if self.chapter == 'all':
            li = []
            for file in self.filelist:
                df = pd.read_csv(self.lang+'/'+file, index_col=None, header=0, sep=';')
                li.append(df)

            words = pd.concat(li, axis=0, ignore_index=True)
        
        else:
            words = pd.read_csv(self.lang+'/'+self.chapter, index_col=None, header=0, sep=';')
        
        self.words = words.sample(frac=1).reset_index(drop=True)

        self.i = 0
        self._show_word()
    
    def _show_word(self):
        self._destroy_frame()
        self._create_frame()

        if self.mode == 'word':
            tk.Label(self.mainframe, text=self.words.iloc[self.i][0], bg=self.solid).grid(row=0, column=0,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
        
        if self.mode =='meaning':
            tk.Label(self.mainframe, text=self.words.iloc[self.i][2], bg=self.solid).grid(row=0, column=0,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
            
            tk.Label(self.mainframe, text=self.words.iloc[self.i][1]).grid(row=1, column=0,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)


        tk.Button(self.mainframe, text='check', command=self._check_result).grid(row=2, column=0, 
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=25)
        
    def _check_result(self):
        self._destroy_frame()     
        self._create_frame()
        
        if self.mode == 'word':
            
            tk.Label(self.mainframe, text=self.words.iloc[self.i][0], bg=self.solid).grid(row=0, column=0, columnspan=2,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
                
            tk.Label(self.mainframe, text=self.words.iloc[self.i][2], bg=self.bright).grid(row=1, column=0, columnspan=2,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
            
            tk.Label(self.mainframe, text=self.words.iloc[self.i][1]).grid(row=2, column=0, columnspan=2, 
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
            if type(self.words.iloc[self.i].sentence) is str:
                tk.Label(self.mainframe, text=self.words.iloc[self.i].sentence).grid(row=3, column=0, columnspan=2,
                                                                                          ipady=self.ipady,
                                                                                          ipadx=self.ipadx,
                                                                                          padx=self.padx,
                                                                                          pady=self.pady)
            
            
        if self.mode =='meaning':
            tk.Label(self.mainframe, text=self.words.iloc[self.i][0], bg=self.bright).grid(row=0, column=0, columnspan=2, 
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
                
            tk.Label(self.mainframe, text=self.words.iloc[self.i][2], bg=self.solid).grid(row=1, column=0, columnspan=2,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
            
            if type(self.words.iloc[self.i].sentence) is str:
                tk.Label(self.mainframe, text=self.words.iloc[self.i].sentence).grid(row=2, column=0, columnspan=2,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
        
        tk.Button(self.mainframe, text='next', command=self._next).grid(row=4, column=1,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
        
        tk.Button(self.mainframe, text='put back', command=self._put_back).grid(row=4, column=0,
                                                                          ipady=self.ipady,
                                                                          ipadx=self.ipadx,
                                                                          padx=self.padx,
                                                                          pady=self.pady)
        
    def _next(self):
        if len(self.words) == self.i+1:
            self._destroy_frame()
            self._create_frame()
            self.master.title('end')
            tk.Label(self.mainframe, text='no more words left to practice').grid(row=0, column=0)
            tk.Button(self.mainframe, text='quit', command=self.master.quit).grid(row=1, column=0,
                                                                                  ipady=self.ipady,
                                                                                  ipadx=self.ipadx,
                                                                                  padx=self.padx,
                                                                                  pady=self.pady)
        
        else:
            self.i = self.i + 1    
            self._show_word()

    
    def _put_back(self):
        self.words.loc[len(self.words)+1] = self.words.iloc[self.i]
        self._next()
    
    def _destroy_frame(self):
        self.mainframe.destroy()
    
    def _create_frame(self):
        self.mainframe = tk.Frame(self.master)
        self.mainframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        
LANG = input('Which language: ')
root = tk.Tk()
my_dic = Dictionary(root, LANG)
my_dic.start()
root.mainloop()
