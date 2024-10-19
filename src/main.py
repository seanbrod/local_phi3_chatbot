import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
#import qdarktheme
import re
from back import generation


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.label = QLabel("RizzBot")  # Title text at the top
        self.label.setAlignment(Qt.AlignCenter)               # Center the title text
        self.label.setStyleSheet("font-size: 20px; font-weight: bold;color: black;")  # Text color changed to black
        self.edit = QLineEdit()                         #Input text area
        self.edit.setPlaceholderText("Enter Text:")
        self.button = QPushButton("Generate")           #Button to change output field
        self.save = QPushButton("Save")                 #Button to save text to file
        self.text = QTextEdit()                   #Output text field
        self.text.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.text.setReadOnly(True)
        self.dialog = QFileDialog(self)                 #File explorer
        self.edit.returnPressed.connect(self.generate)
        
        # Create layout and add widgets
        layout = QHBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.save)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.text)
        layout2.addLayout(layout)
        # Set dialog layout
        self.setLayout(layout2)
        # Link function calls to buttons
        self.button.clicked.connect(self.generate)
        self.save.clicked.connect(self.saves)
        self.setStyleSheet("background-color: #FFB6C1;")  # Light pink background
    # Move copy input text to output
    def generate(self):
        self.update_str("User: "+self.edit.text()+"\n")
        generation(self,self.edit.text()) 
        self.update_str("\n")
        self.edit.clear()

    # Saves text in output to file
    def saves(self):
        f = self.dialog.getSaveFileUrl(self, "Save File", "", "Text (*.txt)")
        fp = f[0].toString()
        #Check if file ends with .txt
        if not re.search("\.txt$", fp):
            fp += ".txt"
        file = open(fp[8:], "w+")
        file.write(self.text.toPlainText())
        file.close()
    def update_str(self, str):
        self.text.insertPlainText(str)
        self.text.verticalScrollBar().setValue(self.text.verticalScrollBar().maximum())
        QCoreApplication.processEvents()

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    #qdarktheme.setup_theme("auto")
    
    win = QMainWindow()
    win.resize(800,600)    
    # Create and show the form
    form = Form()
    win.setCentralWidget(form)
    win.show()
    # Run the main Qt loop
    sys.exit(app.exec())