from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys
from csv import *

class MainUI(QDialog):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("Qt_GUI_Form2CSV.ui", self)
        self.main_list=[]
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.save)
        
    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        
    def add(self):
        lst=[self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text()]
        self.main_list.append(lst)
        QMessageBox.about(self, "Information", "The data has been added succesfully")
        
    def save(self):
        with open("data_entry.csv","a") as file:
            Writer=writer(file)
            #Writer.writerow(["Name","Age","Contact"])
            Writer.writerows(self.main_list)
            QMessageBox.about(self,"Information","The file has been saved succesfully")
       
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    ui=MainUI()
    ui.show()
    app.exec_()