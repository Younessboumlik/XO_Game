from PyQt5 import QtWidgets,QtCore
from choices_window import choice_window


choices = ["X","O"]


"""The main window of the game"""
class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMaximumWidth(self.width())
        self.setMaximumHeight(self.height())
        self.resize(500,500)
        # self.setFixedSize(self.size())
        self.setStyleSheet("background : #05313d")
        self.setWindowTitle("XO GAME")

        self.widget = QtWidgets.QWidget(self)

        buttonslayout = QtWidgets.QVBoxLayout(self.widget)

        label1 = QtWidgets.QLabel("XO GAME")
        label1.setStyleSheet("color: #004be7;font-size:40px;")
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label1.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        buttonslayout.addWidget(label1)

        button1 = QtWidgets.QPushButton("Jouer",self)
        button1.setStyleSheet("QPushButton{background: white;font-size:40px} QPushButton:hover {background-color: #90EE90;}")
        button1.clicked.connect(self.play_game)
        buttonslayout.addWidget(button1)

        button2 = QtWidgets.QPushButton("A propos",self)
        button2.setStyleSheet("QPushButton{background: white;font-size:40px} QPushButton:hover {background-color: #90EE90;}")
        button2.clicked.connect(self.about)
        buttonslayout.addWidget(button2)

        button3 = QtWidgets.QPushButton("Quitter",self)
        button3.setStyleSheet("QPushButton{background: white;font-size:40px} QPushButton:hover {background-color: #90EE90;}")
        buttonslayout.addWidget(button3)
        button3.clicked.connect(self.closing)
        
        self.setCentralWidget(self.widget)


    def play_game(self):
        self.win2 = choice_window()
        self.win2.show()
    def about(self):
        self.win3 = about()
        self.win3.show()
    def closing(self):
        self.close()
"""tha about window"""
class about(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #to stop user from accessing to main window until close this window
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setStyleSheet("background:#83BACF;font-size:20px")
        self.setMaximumWidth(self.width())
        self.setMaximumHeight(self.height())

        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("C’est un jeu XO, programmé par Youness Boumlik en utilisant PyQt5(Python). Amusez-vous bien !")

        layout.addWidget(label)

        github = QtWidgets.QLabel('<a href="https://github.com/Younessboumlik">Mon compte GitHub</a>')
        github.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        github.setOpenExternalLinks(True)
        github.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(github)


        linkedin = QtWidgets.QLabel('<a href="https://www.linkedin.com/in/youness-boumlik-a13935190/">Mon compte LinkedIn</a>')
        linkedin.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        linkedin.setOpenExternalLinks(True)
        linkedin.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(linkedin)


        self.setLayout(layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = mainwindow()
    win.show()
    app.exec_()