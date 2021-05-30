# This is a module to calculate the scores of the players
import sqlite3


class Player:
    def __init__(self, name):
        self.name = name
        self.scored = 0
        self.faced = 0
        self.fours = 0
        self.sixes = 0
        self.bowled = 0
        self.maiden = 0
        self.given = 0
        self.wkts = 0
        self.catches = 0
        self.stumping = 0
        self.ro = 0
        self.points = 0

    # Sql command that return the rows
    def sql_cmd(self, command):
        connect_db = sqlite3.connect("fantasy_cricket.db")
        Cursor = connect_db.cursor()
        cmd = command
        Cursor.execute(cmd)
        rows = Cursor.fetchall()
        return rows

    # Gets and sets the values from the DB into instance variables
    def score_setter(self, table):
        command = f'SELECT * FROM {table} WHERE player = "{self.name}"'
        rows = self.sql_cmd(command)
        self.scored = rows[0][1]
        self.faced = rows[0][2]
        self.fours = rows[0][3]
        self.sixes = rows[0][4]
        self.bowled = rows[0][5]
        self.maiden = rows[0][6]
        self.given = rows[0][7]
        self.wkts = rows[0][8]
        self.catches = rows[0][9]
        self.stumping = rows[0][10]
        self.ro = rows[0][11]
        self.points = self.score_calc(self.scored, self.faced, self.fours,
                                      self.sixes, self.bowled, self.given,
                                      self.wkts, self.catches, self.stumping, self.ro)

    # Score Calculator
    def score_calc(self, scored, faced, fours, sixes, bowled, given, wkts, catches, stumping, ro):
        points = 0
        points += scored/2
        points += wkts * 10
        points += catches * 10
        points += stumping * 10
        points += ro * 10
        points += fours * 1
        points += sixes * 2

        if scored >= 50:
            points += 5
        if scored >= 100:
            points += 10

        if wkts >= 3:
            points += 5
        if wkts >= 5:
            points += 10

        if faced != 0:
            strike_rate = scored / faced * 100
            if 100 >= strike_rate >= 80:
                points += 2
            if strike_rate > 100:
                points += 4

        if bowled != 0:
            overs = bowled / 6
            economy_rate = given / overs
            if 3.5 >= economy_rate >= 2:
                points += 7
            elif economy_rate < 2:
                points += 10

        return points










