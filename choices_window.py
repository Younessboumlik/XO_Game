from PyQt5 import QtWidgets,QtCore


"""the window where we put players names and choices"""
class choice_window(QtWidgets.QWidget):

    def __init__(self):
        global choice2,choice,text,text1,choice_2,choice_1
        super().__init__()
        self.setStyleSheet("background: #83BACF")
        self.setMaximumWidth(self.width())
        self.setMaximumHeight(self.height())
        #set fixed size
        # self.setFixedSize(self.size())
        

        #defining the main layout
        layout = QtWidgets.QVBoxLayout()

        #defining two other horizental layouts, each one will contain information of each player
        layout2 = QtWidgets.QHBoxLayout()
        layout3 = QtWidgets.QHBoxLayout()
        layout4 = QtWidgets.QHBoxLayout()
        layout5 = QtWidgets.QHBoxLayout()



        #the informations for the first player
        label1 = QtWidgets.QLabel("Premier Joueur: ")
        layout2.addWidget(label1)
        label1.setStyleSheet("font-size:20px")
        
        text = QtWidgets.QLineEdit()
        layout2.addWidget(text)
        
        #choise for the first player
        label3 = QtWidgets.QLabel("Premier Joueur Choix: ")
        layout4.addWidget(label3)
        label3.setStyleSheet("font-size:20px")

        
        choice = QtWidgets.QComboBox()
        choice.addItems(["X","O"])
        #initialize the 2 choices
        choice_1 = "X"
        choice_2 = "O"

        choice.activated.connect(self.other_button)
        layout4.addWidget(choice)
        
        #informations for the second player
        label4 = QtWidgets.QLabel("Deusieme Joueur: ")
        layout3.addWidget(label4)
        label4.setStyleSheet("font-size:20px")


        text1 = QtWidgets.QLineEdit()
        layout3.addWidget(text1)
        p2 = text1.text()


        #choise for the second player
        label2 = QtWidgets.QLabel("Deusieme Joueur Choix: ")
        layout5.addWidget(label2)
        label2.setStyleSheet("font-size:20px")


        choice2 = QtWidgets.QComboBox()
        
        choice2.insertItem(0,choice_2)
        layout5.addWidget(choice2)        
        
        #confirmation button:
        button = QtWidgets.QPushButton("Jouer")
        #changing colors of the button
        button.setStyleSheet("QPushButton{background: #D8BACF;font-size:25px} QPushButton:hover{background: #FCBACF}")
        button.clicked.connect(self.button_clicked)



        #putting the horizentals layouts in the vertical one
        layout.addLayout(layout2)
        layout.addLayout(layout4)
        layout.addLayout(layout3)
        layout.addLayout(layout5)
        layout.addWidget(button)
        
        

        #set layout as the main layout in our layout.
        self.setLayout(layout)


    def other_button(self):
        global choice_2,choice_1
        choice_1 = choice.currentText()
        choice2.clear()
        if choice_1 == 'X':
            choice_2 = 'O'
        elif choice_1 == 'O':
            choice_2 = 'X'
        choice2.insertItem(0,choice_2)
    def button_clicked(self):
        global p1,p2
        p1 = text.text()
        p2 = text1.text()
        self.game_window = game_window()
        self.game_window.show()
        self.close()

"""the game window"""
class game_window(QtWidgets.QMainWindow):
    global label,current_player,layout,k,listglobal
    def __init__(self):
        global buttons,choices,label,current_player,layout,k,listglobal
        list1=[1,2,3]
        list2=[4,5,6]
        list3=[7,8,9]
        listglobal=[list1,list2,list3]
        super().__init__()
        #to stop user from accessing to main window until close this window
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        k = 0
        self.resize(750,750)
        self.setStyleSheet("background:#E6E494")
        # self.setFixedSize(self.size())

        self.widget = QtWidgets.QWidget(self)

        layout = QtWidgets.QGridLayout(self.widget)


        self.setCentralWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        #defining the current player
        current_player = p1
        label = QtWidgets.QLabel("Le tour de : "+current_player)
        label.setStyleSheet("font-size: 30px;color: black;font: Arial;")

        layout.addWidget(label, 0, 0, 1, 3)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)


        #this list will contain all the 9 buttons
        buttons=[]
        choices=[choice_1,choice_2]
        # print(choices)
        self.c=choices[0]
        #setting this to be showen after clicking the button
        current_player = p2
        #now creating all buttons
        for i in range(3):
            for j in range(3):
                button = QtWidgets.QPushButton(self)
                buttons.append(button)
                sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
                button.setSizePolicy(sizePolicy)
                button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
                #this will connect the buttons with the main function that will verify the game.
                button.clicked.connect(lambda state, x=i, y=j: self.click(x,y))
                layout.addWidget(button,i+1,j)



    #the method that will work if any button is clicked
    def click(self,i,j):
        global current_player,new_button,k,possible_winner

        listglobal[i][j] = self.c
        (buttons[i*3+j]).setText(self.c)
        buttons[i*3+j].setStyleSheet("font-size:110px;background:#DE9F53;")
        buttons[i*3+j].setDisabled(True)

 
        label.setText("Le tour de : "+current_player)
        #incrementing the number of buttoons clocked
        k = k + 1

        if listglobal[0][0]==self.c and listglobal[1][0]==self.c and listglobal[2][0]==self.c:
            #change the color of buttons
            buttons[0].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[3].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[6].setStyleSheet("font-size:90px;background:#83DB30;")
            #show the winner
            label.setText(possible_winner+" a gagne!")
            #the function that will disable all buttons
            disablling = lambda  button : button.setDisabled(True)
            #using the magic function map to apply this to all buttons.
            list(map(disablling,buttons))
            #the button that will let us replaying the game.
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)



        if listglobal[0][1]==self.c and listglobal[1][1]==self.c and listglobal[2][1]==self.c:
            buttons[1].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[4].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[7].setStyleSheet("font-size:90px;background:#83DB30;")
            label.setText(possible_winner+" a gagne!")
            disablling = lambda  button : button.setDisabled(True)
            list(map(disablling,buttons))
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)

        if listglobal[0][2]==self.c and listglobal[1][2]==self.c and listglobal[2][2]==self.c:
            buttons[2].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[5].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[8].setStyleSheet("font-size:90px;background:#83DB30;")
            label.setText(possible_winner+" a gagne!")
            disablling = lambda  button : button.setDisabled(True)
            list(map(disablling,buttons))
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)

        if listglobal[0][0]==self.c and listglobal[0][1]==self.c and listglobal[0][2]==self.c:
            buttons[0].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[1].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[2].setStyleSheet("font-size:90px;background:#83DB30;")
            label.setText(possible_winner+" a gagne!")
            disablling = lambda  button : button.setDisabled(True)
            list(map(disablling,buttons))
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)

        if listglobal[1][0]==self.c and listglobal[1][1]==self.c and listglobal[1][2]==self.c:
            buttons[3].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[4].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[5].setStyleSheet("font-size:90px;background:#83DB30;")
            label.setText(possible_winner+" a gagne!")
            disablling = lambda  button : button.setDisabled(True)
            list(map(disablling,buttons))
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)

        if listglobal[2][0]==self.c and listglobal[2][1]==self.c and listglobal[2][2]==self.c:
            buttons[6].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[7].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[8].setStyleSheet("font-size:90px;background:#83DB30;")
            label.setText(possible_winner+" a gagne!")
            disablling = lambda  button : button.setDisabled(True)
            list(map(disablling,buttons))
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)

        if listglobal[0][0]==self.c and listglobal[1][1]==self.c and listglobal[2][2]==self.c:
            buttons[0].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[4].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[8].setStyleSheet("font-size:90px;background:#83DB30;") 
            label.setText(possible_winner+" a gagne!")
            disablling = lambda  button : button.setDisabled(True)
            list(map(disablling,buttons))
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)
              
        if listglobal[2][0]==self.c and listglobal[1][1]==self.c and listglobal[0][2]==self.c:
            buttons[2].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[4].setStyleSheet("font-size:90px;background:#83DB30;")
            buttons[6].setStyleSheet("font-size:90px;background:#83DB30;")
            label.setText(possible_winner+" a gagne!")
            disablling = lambda  button : button.setDisabled(True)
            list(map(disablling,buttons))
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)
        #taking the value of possible winner before changing the value
        possible_winner = current_player
        if current_player == p1:
            current_player = p2
        elif current_player == p2:
            current_player = p1
        if self.c == "X":
            self.c = "O"
        elif self.c == "O":
            self.c ="X"
        #in this case the came is draw
        if k == 9:
            new_button = QtWidgets.QPushButton("Rejouer")
            new_button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}")
            layout.addWidget(new_button,4,0,1,3)
            new_button.clicked.connect(self.restarting)
            label.setText("C'est un match nul")
        
    def restarting(self):
        global listglobal,k,current_player
        #initialising the counter to count how much buttons was clicked
        k = 0
        #intialising all buttons
        initialising = lambda button:(button.setStyleSheet("QPushButton{background: #99942E} QPushButton:hover{background:#DED643}"),button.setText(''),button.setDisabled(False))
        list(map(initialising,buttons))
        #reseting the array after restarting the game
        list1=[1,2,3]
        list2=[4,5,6]
        list3=[7,8,9]
        listglobal=[list1,list2,list3]
        #fixing players after restarting the game
        current_player = p1
        label.setText("Le tour de : "+current_player)
        current_player = p2
        #intialising choices after restarting
        self.c=choices[0]
        #removing the new button after restarting
        layout.removeWidget(new_button)
        new_button.hide()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = choice_window()
    win.show()
    app.exec_()