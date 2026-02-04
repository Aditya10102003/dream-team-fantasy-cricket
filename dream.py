# -*- coding: utf-8 -*-
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

# Connect to database
conn = sqlite3.connect('fantasy.db')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 675)
        MainWindow.move(100, 10)
        MainWindow.setStyleSheet("QMainWindow {background-color: rgb(192, 200, 104);}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Top Horizontal layout: Player categories
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        # Labels and LineEdits
        self.label_4 = QtWidgets.QLabel("Batsmen", self.centralwidget)
        self.label_4.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        self.label_4.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.label_4)
        self.e1 = QtWidgets.QLineEdit(self.centralwidget)
        self.e1.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.e1)

        self.label_6 = QtWidgets.QLabel("Bowlers", self.centralwidget)
        self.label_6.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        self.label_6.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.label_6)
        self.e2 = QtWidgets.QLineEdit(self.centralwidget)
        self.e2.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.e2)

        self.label_7 = QtWidgets.QLabel("All Rounders", self.centralwidget)
        self.label_7.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        self.label_7.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.label_7)
        self.e3 = QtWidgets.QLineEdit(self.centralwidget)
        self.e3.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.e3)

        self.label_8 = QtWidgets.QLabel("Wicketkeepers", self.centralwidget)
        self.label_8.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        self.label_8.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.label_8)
        self.e4 = QtWidgets.QLineEdit(self.centralwidget)
        self.e4.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.e4)

        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        # Horizontal line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line)

        # Horizontal layout: Left (categories) + Right (selected players)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        # Left Section
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Player Categories", self.centralwidget)
        self.label.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addWidget(self.label)

        # Group Box for Radio Buttons
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.rb1 = QtWidgets.QRadioButton("BAT", self.groupBox)
        self.rb2 = QtWidgets.QRadioButton("BWL", self.groupBox)
        self.rb3 = QtWidgets.QRadioButton("AR", self.groupBox)
        self.rb4 = QtWidgets.QRadioButton("WK", self.groupBox)
        self.horizontalLayout_4.addWidget(self.rb1)
        self.horizontalLayout_4.addWidget(self.rb2)
        self.horizontalLayout_4.addWidget(self.rb3)
        self.horizontalLayout_4.addWidget(self.rb4)
        self.verticalLayout_8.addWidget(self.groupBox)

        # List of available players
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setStyleSheet("color: rgb(0,0,127); font: 75 12pt 'MS Shell Dlg 2';")
        self.verticalLayout_8.addWidget(self.list1)

        # Available Points Button
        self.btn1 = QtWidgets.QPushButton("Available Points : 1000", self.centralwidget)
        self.btn1.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        self.verticalLayout_8.addWidget(self.btn1)

        # Criteria Image
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setPixmap(QtGui.QPixmap("criteria.jpg"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_8.addWidget(self.label_5)

        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        # Right Section
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.label_2 = QtWidgets.QLabel("Selected Players", self.centralwidget)
        self.label_2.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_9.addWidget(self.label_2)

        self.l1 = QtWidgets.QLabel("???", self.centralwidget)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setFont(QtGui.QFont("MS Shell Dlg 2", 12))
        self.l1.setStyleSheet("background-color: rgb(0,0,127); color: white; font: 75 12pt 'MS Shell Dlg 2';")
        self.verticalLayout_9.addWidget(self.l1)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_9.addWidget(self.line_2)

        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setStyleSheet("color: rgb(0,0,127); font: 75 12pt 'MS Shell Dlg 2';")
        self.verticalLayout_9.addWidget(self.list2)

        self.btn2 = QtWidgets.QPushButton("Points used : 0", self.centralwidget)
        self.btn2.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        self.verticalLayout_9.addWidget(self.btn2)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setPixmap(QtGui.QPixmap("dream1.png"))
        self.verticalLayout_9.addWidget(self.label_3)

        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menuFile = QtWidgets.QMenu("File", self.menubar)
        self.menuHelp = QtWidgets.QMenu("Help", self.menubar)
        self.actionNew = QtWidgets.QAction("New Team", MainWindow)
        self.actionOpen = QtWidgets.QAction("Open Team", MainWindow)
        self.actionSave_Team = QtWidgets.QAction("Save Team", MainWindow)
        self.actionQuit = QtWidgets.QAction("Team Score", MainWindow)
        self.actionRules = QtWidgets.QAction("Rules", MainWindow)
        self.actionInstructions = QtWidgets.QAction("Instructions", MainWindow)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Team)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionRules)
        self.menuHelp.addAction(self.actionInstructions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        MainWindow.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # Class attributes
        self.bat = self.bwl = self.ar = self.wk = 0
        self.avl = 1000
        self.used = 0

        # Connect signals
        self.rb1.toggled.connect(self.ctg)
        self.rb2.toggled.connect(self.ctg)
        self.rb3.toggled.connect(self.ctg)
        self.rb4.toggled.connect(self.ctg)
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)
        self.menuFile.triggered[QtWidgets.QAction].connect(self.menufunction)

    # ---------------------- FUNCTIONS -----------------------
    def ctg(self):
        ctgr = ''
        if self.rb1.isChecked(): ctgr = "BAT"
        if self.rb2.isChecked(): ctgr = "BWL"
        if self.rb3.isChecked(): ctgr = "AR"
        if self.rb4.isChecked(): ctgr = "WK"
        self.fillList(ctgr)

    def fillList(self, ctgr):
        if self.l1.text() == "???":
            self.showdlg("Enter name of team first")
            return
        self.list1.clear()
        cursor = conn.execute("SELECT player FROM stats WHERE ctg=?", (ctgr,))
        selected = [self.list2.item(i).text() for i in range(self.list2.count())]
        for row in cursor:
            if row[0] not in selected:
                self.list1.addItem(row[0])

    def criteria(self, ctgr, item):
        msg = ''
        if ctgr == "BAT" and self.bat >= 5: msg = "Batsmen not more than 5"
        if ctgr == "BWL" and self.bwl >= 5: msg = "Bowlers not more than 5"
        if ctgr == "AR" and self.ar >= 3: msg = "Allrounders not more than 3"
        if ctgr == "WK" and self.wk >= 1: msg = "Wicketkeepers not more than 1"
        if msg != '' or self.avl <= 0:
            msg = msg if msg != '' else "You have exhausted your points"
            self.showdlg(msg)
            return False

        if ctgr == "BAT": self.bat += 1
        if ctgr == "BWL": self.bwl += 1
        if ctgr == "AR": self.ar += 1
        if ctgr == "WK": self.wk += 1

        cursor = conn.execute("SELECT value FROM stats WHERE player=?", (item.text(),))
        row = cursor.fetchone()
        self.avl -= int(row[0])
        self.used += int(row[0])
        return True

    def removelist1(self, item):
        ctgr = ''
        if self.rb1.isChecked(): ctgr = "BAT"
        if self.rb2.isChecked(): ctgr = "BWL"
        if self.rb3.isChecked(): ctgr = "AR"
        if self.rb4.isChecked(): ctgr = "WK"
        if self.criteria(ctgr, item):
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())
            self.showstatus()

    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        cursor = conn.execute("SELECT value, ctg FROM stats WHERE player=?", (item.text(),))
        row = cursor.fetchone()
        self.avl += int(row[0])
        self.used -= int(row[0])
        ctgr = row[1]
        if ctgr == "BAT": self.bat -= 1
        if ctgr == "BWL": self.bwl -= 1
        if ctgr == "AR": self.ar -= 1
        if ctgr == "WK": self.wk -= 1
        self.showstatus()

    def showstatus(self):
        self.e1.setText(str(self.bat))
        self.e2.setText(str(self.bwl))
        self.e3.setText(str(self.ar))
        self.e4.setText(str(self.wk))
        self.btn1.setText(f"Available Points : {self.avl}")
        self.btn2.setText(f"Points used : {self.used}")

    def showdlg(self, msg):
        Dialog = QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team Selector")
        Dialog.exec()

    def menufunction(self, action):
        txt = action.text()
        if txt == "New Team":
            self.bat = self.bwl = self.ar = self.wk = 0
            self.avl = 1000
            self.used = 0
            self.list1.clear()
            self.list2.clear()
            text, ok = QtWidgets.QInputDialog.getText(None, "Dream Team Selector", "Enter name of team:")
            if ok: self.l1.setText(str(text))
        elif txt == "Save Team":
            selected = ",".join([self.list2.item(i).text() for i in range(self.list2.count())])
            self.saveteam(self.l1.text(), selected, self.used)
        elif txt == "Open Team":
            cursor = conn.execute("SELECT name FROM teams")
            teams = [row[0] for row in cursor]
            if not teams:
                self.showdlg("No saved teams found")
                return 
            team_name, ok = QtWidgets.QInputDialog.getItem(None, "Open Team", "Select a team:", teams, 0, False)
            if ok:
                self.list1.clear()
                self.list2.clear()
                self.bat = self.bwl = self.ar = self.wk = 0
                self.avl = 1000
                self.used = 0
                self.l1.setText(team_name)
                cursor = conn.execute("SELECT players, value FROM teams WHERE name=?", (team_name,))
                row = cursor.fetchone()
            if row:
                players = row[0].split(",")
                self.used = int(row[1])
                for player in players:
                    self.list2.addItem(player)
                # Update category counts
                    cursor2 = conn.execute("SELECT ctg, value FROM stats WHERE player=?", (player,))
                    r2 = cursor2.fetchone()
                    if r2:
                        ctgr, val = r2
                        if ctgr == "BAT": self.bat += 1
                        if ctgr == "BWL": self.bwl += 1
                        if ctgr == "AR": self.ar += 1
                        if ctgr == "WK": self.wk += 1
                        self.avl -= int(val)
            self.showstatus()

    def saveteam(self, nm, string, val):
        if self.bat + self.bwl + self.ar + self.wk != 11:
            self.showdlg("Insufficient players")
            return
        try:
            conn.execute("INSERT INTO teams (name, players, value) VALUES (?, ?, ?);", (nm, string, val))
            conn.commit()
            self.showdlg("Team Saved successfully")
        except:
            conn.rollback()
            self.showdlg("Error saving team")

# ---------------------- MAIN -----------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
