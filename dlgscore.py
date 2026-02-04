# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)

        # --- Layouts ---
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(25, -1, 25, -1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        # --- Team Selection ---
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont("Tahoma", 10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.cb0 = QtWidgets.QComboBox(Dialog)
        self.cb0.setFont(font)
        self.cb0.setObjectName("cb0")
        self.horizontalLayout.addWidget(self.cb0)

        # --- Populate teams ---
        conn = sqlite3.connect('fantasy.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM teams")
        for row in cursor.fetchall():
            self.cb0.addItem(row[0])
        conn.close()

        # --- Match Selection ---
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.cb1 = QtWidgets.QComboBox(Dialog)
        self.cb1.setFont(font)
        self.cb1.setObjectName("cb1")
        self.cb1.addItems(["Match1", "Match2", "Match3", "Match4", "Match5"])
        self.horizontalLayout.addWidget(self.cb1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # --- Separator Line ---
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line)

        # --- Score Labels ---
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.label_5 = QtWidgets.QLabel(Dialog)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        # --- Another Separator ---
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line_2)

        # --- Player and Score Lists ---
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.lw1 = QtWidgets.QListWidget(Dialog)
        self.lw1.setFont(font)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout_2.addWidget(self.lw1)

        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.lw2 = QtWidgets.QListWidget(Dialog)
        self.lw2.setFont(font)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout_2.addWidget(self.lw2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # --- Another Separator ---
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line_3)

        # --- Calculate Button and Total Score ---
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.horizontalLayout_3.addWidget(self.pushButton)

        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        self.scorelabel = QtWidgets.QLabel(Dialog)
        font.setBold(True)
        self.scorelabel.setFont(font)
        self.scorelabel.setObjectName("scorelabel")
        self.horizontalLayout_3.addWidget(self.scorelabel)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculate(self):
        import sqlite3
        conn = sqlite3.connect('fantasy.db')

        # Get selected team and match
        team = self.cb0.currentText()
        match_table = self.cb1.currentText()

         # Clear previous data
        self.lw1.clear()
        self.lw2.clear()
        team_total = 0

    # Map combo box match names to actual DB table names
       #match_table_map = {
        #"Match1": "match_1",
        #"Match2": "match_2",
        #"Match3": "match_3",
        #"Match4": "match_4",
        #"Match5": "match_5",
        #}

        '''if match_name not in match_table_map:
            self.scorelabel.setText("Error")
            return

        match_table = match_table_map[match_name]

         # Clear previous data
        self.lw1.clear()
        self.lw2.clear()
        team_total = 0'''

    # Get selected players from the team
        sql_team = "SELECT players FROM teams WHERE name=?"
        cur = conn.execute(sql_team, (team,))
        row = cur.fetchone()
        if not row:
            self.scorelabel.setText("0")
            return

        selected_players = row[0].split(',')
        self.lw1.addItems(selected_players)

        # Calculate score for each player
        for i in range(self.lw1.count()):
            player_name = self.lw1.item(i).text()
            total_score, batting_score, bowling_score, fielding_score = 0, 0, 0, 0
            try:
                sql_player = f"SELECT * FROM {match_table} WHERE player=?"
                cursor = conn.execute(sql_player, (player_name,))
                row = cursor.fetchone()
                if not row:
                    continue  # Skip if player not in this match table

            except sqlite3.OperationalError:
                self.scorelabel.setText("Table not found")
                return

            # Row structure: player, runs, balls, fours, sixes, overs, runs_given, wickets, catches, stumps, runouts
            # Example calculation (adjust indexes as per your DB)
            runs = int(row[1])
            balls = int(row[2])
            fours = int(row[3])
            sixes = int(row[4])
            overs = int(row[5])
            runs_given = int(row[6])
            wickets = int(row[7])
            catches = int(row[8])
            stumps = int(row[9])
            runouts = int(row[10])

            # Batting score
            batting_score = runs // 2
            if runs >= 50:
                batting_score += 5
            if runs >= 100:
                batting_score += 10
            if balls > 0:
                sr = runs / balls * 100
                if 80 <= sr < 100:
                    batting_score += 2
                elif sr >= 100:
                    batting_score += 4
            batting_score += fours + 2 * sixes

        # Bowling score
        bowling_score = wickets * 10
        if wickets >= 3:
            bowling_score += 5
        if wickets >= 5:
            bowling_score += 10
        if overs > 0:
            er = runs_given * 6 / overs
            if er <= 2:
                bowling_score += 10
            elif er <= 3.5:
                bowling_score += 7
            elif er <= 4.5:
                bowling_score += 4

        # Fielding score
        fielding_score = (catches + stumps + runouts) * 10

        # Total score
        total_score = batting_score + bowling_score + fielding_score
        self.lw2.addItem(str(total_score))
        team_total += total_score

        self.scorelabel.setText(str(team_total))
        conn.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Score Calculator"))
        self.label_2.setText(_translate("Dialog", "Choose Team"))
        self.label.setText(_translate("Dialog", "Choose Match"))
        self.label_5.setText(_translate("Dialog", "Players"))
        self.label_4.setText(_translate("Dialog", "Score"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))
        self.scorelabel.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
