# Player class
class Player:
    def __init__(self, id, name, teamname):
        self.id = id
        self.name = name
        self.teamname = teamname

# Team class contains a list of Player
# Objects
class Team:

    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)

# School class contains a list of Team
# objects.
class School:
    
    def __init__(self, name):
        self.name = name
        self.team = []

    def addTeam(self, team):
        self.team.append(team)
    
    def getTotalPlayersInSchool(self):
        count = 0
        for t in self.team:
            count += t.getNumberOfPlayers()
        return count


p1 = Player(1, 'John', 'Koalas')
p2 = Player(2, 'Jeremy', 'Koalas')
p3 = Player(3, 'Jackson', 'Koalas')

p4 = Player(1, 'Vince', 'Tigers')
p5 = Player(2, 'Jacob', 'Tigers')

t1 = Team('Koalas')
t1.addPlayer(p1)
t1.addPlayer(p2)

print(t1.getNumberOfPlayers())

t2 = Team('Tigers')
t2.addPlayer(p4)
t2.addPlayer(p5)

school1 = School('Seattle School')
school1.addTeam(t1)
school1.addTeam(t2)

res = school1.getTotalPlayersInSchool()
print("Total Number of students in the teams:", res)





# Task 2#
# The Team class will have two properties that will be set using an initializer:

# name
# players: a list with player class objects in it
# It will have two methods:

# addPlayer(), which will add new player objects in the players list

# getNumberOfPlayers(), which will return the total number of players in the players list

# Task 3#
# The School class will contain two properties that will be set using an initializer:

# teams, a list of team class objects
# name
# It will have two methods:

# addTeam, which will add new team objects in the teams list
# getTotalPlayersInSchool(), which will count the total players in all of the teams in the School and return the count