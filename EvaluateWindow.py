# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaluateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from ScoreCalc import Player

class Ui_EvaluateWindow(object):
    def setupUi(self, EvaluateWindow):
        EvaluateWindow.setObjectName("EvaluateWindow")
        EvaluateWindow.resize(693, 632)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        EvaluateWindow.setFont(font)
        EvaluateWindow.setWindowOpacity(1.0)
        EvaluateWindow.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(EvaluateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_player = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_player.setFont(font)
        self.lbl_player.setObjectName("lbl_player")
        self.horizontalLayout_2.addWidget(self.lbl_player)
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lbl_score = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_score.setFont(font)
        self.lbl_score.setObjectName("lbl_score")
        self.horizontalLayout_2.addWidget(self.lbl_score)
        self.ln_score = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ln_score.setFont(font)
        self.ln_score.setStyleSheet("QLineEdit {\n"
"    Border-style: none;\n"
"    color:rgb(41, 196, 198);\n"
"}")
        self.ln_score.setReadOnly(True)
        self.ln_score.setObjectName("ln_score")
        self.horizontalLayout_2.addWidget(self.ln_score)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lst_player = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lst_player.setFont(font)
        self.lst_player.setStyleSheet("QListWidget {\n"
"    padding: 10px;\n"
"    border: 1px solid rgba(70, 70, 70, 70);\n"
"    border-radius: 10px;\n"
"}")
        self.lst_player.setObjectName("lst_player")
        item = QtWidgets.QListWidgetItem()
        self.horizontalLayout_3.addWidget(self.lst_player)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lst_score = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lst_score.setFont(font)
        self.lst_score.setStyleSheet("QListWidget {\n"
"    padding: 10px;\n"
"    border: 1px solid rgba(70, 70, 70, 70);\n"
"    border-radius: 10px;\n"
"}")
        self.lst_score.setObjectName("lst_score")
        self.horizontalLayout_3.addWidget(self.lst_score)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 12, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cmbo_select_team = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbo_select_team.sizePolicy().hasHeightForWidth())
        self.cmbo_select_team.setSizePolicy(sizePolicy)
        self.cmbo_select_team.setStyleSheet("")
        self.cmbo_select_team.setObjectName("cmbo_select_team")
        self.horizontalLayout.addWidget(self.cmbo_select_team)
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.cmbo_select_match = QtWidgets.QComboBox(self.centralwidget)
        self.cmbo_select_match.setObjectName("cmbo_select_match")
        self.horizontalLayout.addWidget(self.cmbo_select_match)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.lbl_heading_evaluate = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_heading_evaluate.sizePolicy().hasHeightForWidth())
        self.lbl_heading_evaluate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.lbl_heading_evaluate.setFont(font)
        self.lbl_heading_evaluate.setStyleSheet("QLabel {\n"
"    color: rgb(41, 196, 198);\n"
"}")
        self.lbl_heading_evaluate.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_heading_evaluate.setObjectName("lbl_heading_evaluate")
        self.gridLayout.addWidget(self.lbl_heading_evaluate, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 8, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_evaluate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_evaluate.sizePolicy().hasHeightForWidth())
        self.btn_evaluate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_evaluate.setFont(font)
        self.btn_evaluate.setStyleSheet("QPushButton {\n"
"    Color: rgb(22, 108, 108);\n"
"    padding: 7px;\n"
"    Border:2px solid rgb(41, 196, 198);\n"
"    border-radius:10px;\n"
"    width: 60%;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(46, 223, 223);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.btn_evaluate.setObjectName("btn_evaluate")
        self.horizontalLayout_4.addWidget(self.btn_evaluate)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        EvaluateWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EvaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(EvaluateWindow)

        # Adding Items to the Combo box1
        command = f"SELECT name FROM teams;"
        rows = self.sql_cmd(command, "get")
        self.teams = []
        for team_name in rows:
            self.teams.append(team_name[0])
        self.cmbo_select_team.addItems(self.teams)

        # Adding Items to the Combo box2
        self.cmbo_select_match.addItem("match")

        self.cmbo_select_team.view().pressed.connect(self.team_selected)
        self.cmbo_select_match.view().pressed.connect(self.match_selected)

        # Evaluate Button

        self.btn_evaluate.clicked.connect(self.evaluate)

        # Team
        self.current_team = []
        self.current_match = ""



    def retranslateUi(self, EvaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        EvaluateWindow.setWindowTitle(_translate("EvaluateWindow", "Fantasy Cricket"))
        self.lbl_player.setText(_translate("EvaluateWindow", "Players:"))
        self.lbl_score.setText(_translate("EvaluateWindow", "Score:"))
        self.lbl_heading_evaluate.setText(_translate("EvaluateWindow", "<strong>Evaluate</strong> the performance of your Fantasy Team"))
        self.btn_evaluate.setText(_translate("EvaluateWindow", "Evaluate"))

    # Getting the players of the current team selected
    def team_selected(self, index):
        item = self.cmbo_select_team.model().itemData(index)
        self.lst_player.clear()
        team = item[0]

        command = f'SELECT players FROM teams WHERE name = "{team}";'
        rows = self.sql_cmd(command, "get")

        # Getting the players names
        players = rows[0][0].strip().split(",")
        self.lst_player.addItems(players)
        self.current_team = players

    # Setting the name of the match selected
    def match_selected(self, index):
        self.current_match = self.cmbo_select_match.model().itemData(index)[0]

    # Event Handler for evaluate button
    def evaluate(self):
        self.lst_score.clear()

        if self.current_match == "":
            self.current_match = self.cmbo_select_match.currentText()

        command = f"SELECT * from {self.current_match};"
        match_data = self.sql_cmd(command, "get")

        total_score = 0
        scores = []

        # Getting the scores
        for player in self.current_team:
            for row in match_data:
                if player == row[0]:
                    x = Player(row[0])
                    x.score_setter(self.current_match)
                    total_score += x.points
                    scores.append(str(x.points))

        # Showing the scores and total score
        self.lst_score.addItems(scores)
        self.ln_score.setText(str(int(total_score)))

        # Update the value in DB
        team_name = self.cmbo_select_team.currentText()
        sql = f'SELECT * FROM teams WHERE name = "{team_name}";'
        team_info = self.sql_cmd(sql, "get")
        team_value = 0
        for row in team_info:
            team_value += row[2]

        if team_value == 0:
            cmd = f'UPDATE teams SET value = {int(total_score)} WHERE name = "{team_name}";'
            self.sql_cmd(cmd, "update")

    # Filling the Player list with names based on the team selected
    def fill_player_list(self, name):
        self.lst_player.clear()
        team = name
        command = f'SELECT players FROM teams WHERE name = "{team}";'
        rows = self.sql_cmd(command, "get")
        players = rows[0][0].strip().split(",")

        self.lst_player.addItems(players)

    # SQL connection
    def sql_cmd(self, command, action):
        connect_db = sqlite3.connect("fantasy_cricket.db")
        cursor = connect_db.cursor()
        cmd = command
        cursor.execute(cmd)
        if action.lower() == "get":
            rows = cursor.fetchall()
            return rows
        elif action.lower() == "update":
            connect_db.commit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateWindow = QtWidgets.QMainWindow()
    ui = Ui_EvaluateWindow()
    ui.setupUi(EvaluateWindow)
    EvaluateWindow.show()
    sys.exit(app.exec_())