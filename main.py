import os
import tkinter as tk
from tkinter.filedialog import askdirectory
class main:
    def __init__(self):
        #window
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry("300x200")
        #string
        self.pathStr = tk.StringVar()
        self.pathOutStr = tk.StringVar()
        self.message = tk.StringVar()
        #button
        tk.Button(self.mainWindow,text="select",command=self.selectPath).grid(row=0,column=1)
        tk.Button(self.mainWindow,text="selectOutpath",command=self.selectOutPath).grid(row=1,column=1)
        tk.Button(self.mainWindow,text="创建文件夹",command=self.creatFolderByFileName).grid(row=2,column=1)
        #ENTRY
        tk.Entry(self.mainWindow,textvariable=self.pathStr,width=30).grid(row=0,column=0)
        tk.Entry(self.mainWindow,textvariable=self.pathOutStr,width=30).grid(row=1,column=0)
        #lable
        self.messageLable=tk.Label(self.mainWindow,textvariable=self.message,fg="red")
        self.messageLable.grid(row=2)
        #windon
        self.mainWindow.mainloop()

    def selectPath(self):
        path_=askdirectory()
        self.pathStr.set(path_)

    def selectOutPath(self):
        path_=askdirectory()
        self.pathOutStr.set(path_)

    def creatFolderByFileName(self):
        try:
            filenames = os.listdir(self.pathStr.get())
            for fileName in filenames:
                file=os.path.splitext(fileName)
                filename,fileSuffix=file
                if(fileSuffix!=""):
                    outputPath = self.pathOutStr.get()+"/"+filename
                    os.mkdir(outputPath)
            self.messageLable.config(fg="green")
            self.message.set("创建文件夹成功")
        except Exception as e:
            self.messageLable.config(fg="red")
            self.message.set(e)
            return None
main()