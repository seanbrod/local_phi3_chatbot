import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton,
    QTextEdit, QHBoxLayout, QVBoxLayout, QFileDialog
)
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QFont  # Import QFont
from back import generation

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets

        # Title label
        self.label = QLabel("Friend")  # Title text at the top
        self.label.setAlignment(Qt.AlignCenter)  # Center the title text
        self.label.setStyleSheet("color: black;")

        # Set a larger font for the label
        label_font = QFont()
        label_font.setPointSize(24)  # Adjust as desired
        label_font.setBold(True)
        self.label.setFont(label_font)
        
        # Input text area
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Enter Text:")
        self.edit.setStyleSheet("color: black;")  # Set input text color to black

        # Set a larger font for the input field
        input_font = QFont()
        input_font.setPointSize(14)  # Adjust as desired
        self.edit.setFont(input_font)
        
        # Buttons
        self.button = QPushButton("Generate")  # Button to change output field
        self.save = QPushButton("Save")        # Button to save text to file

        # Set a larger font for the buttons
        button_font = QFont()
        button_font.setPointSize(14)  # Adjust as desired
        self.button.setFont(button_font)
        self.save.setFont(button_font)
        
        # Output text field
        self.text = QTextEdit()
        self.text.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.text.setReadOnly(True)
        self.text.setStyleSheet("color: black;")  # Set output text color to black

        # Set a larger font for the output field
        output_font = QFont()
        output_font.setPointSize(14)  # Adjust as desired
        self.text.setFont(output_font)
        
        self.edit.returnPressed.connect(self.generate)
        
        # Create layout and add widgets
        layout = QHBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.save)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.label)  # Add the label to the layout
        layout2.addWidget(self.text)
        layout2.addLayout(layout)
        
        # Set dialog layout
        self.setLayout(layout2)
        
        # Link function calls to buttons
        self.button.clicked.connect(self.generate)
        self.save.clicked.connect(self.saves)
        self.setStyleSheet("background-color: #87CEEB;")  # Light pink background
    
    # Move copy input text to output
    def generate(self):
        self.update_str("\n" + "You: " + '"' + self.edit.text() + '"'+ "\n")
        self.update_str('-----------------------------------------------------------------------------------------------')
        self.update_str("\n" +"Friend: ")
        generation(self, self.edit.text()) 
        self.update_str("\n" + 'Im always here for you' + "\n")
        self.update_str('-----------------------------------------------------------------------------------------------')
        self.edit.clear()

    # Saves text in output to file
    def saves(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if file_path:
            # Ensure the file has a .txt extension
            if not file_path.endswith('.txt'):
                file_path += '.txt'
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text.toPlainText())

    def update_str(self, text):
        self.text.insertPlainText(text)
        self.text.verticalScrollBar().setValue(self.text.verticalScrollBar().maximum())
        QCoreApplication.processEvents()

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Set global stylesheet to set all text color to black
    app.setStyleSheet("""
        * {
            color: black;
        }
        QWidget {
            background-color: #FFB6C1;
        }
    """)
    
    win = QMainWindow()
    win.resize(800, 600)    
    # Create and show the form
    form = Form()
    win.setCentralWidget(form)
    win.show()
    # Run the main Qt loop
    sys.exit(app.exec())
