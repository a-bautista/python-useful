from Player import Player

def main():
    p1 = Player('Florian', 100000)
    p2 = Player('Johannes', 200000)
    p1.formerTeams.append('Bayern Munich')
    p1.formerTeams.append('Liverpool')
    p2.formerTeams.append('Real Madrid')

    print(p1.name)
    print(p1.teamName)
    print(p1.teamMembers)
    print(p1.formerTeams)
    print('*'*40)
    print(p2.name)
    print(p2.teamName)
    print(p2.teamMembers)
    print(p2.formerTeams)
    
    # print(p1.demo(10, 20, 30))
    # for some reason the class and static methods return None at the end
    print('*'*40)
    print(p2.demo(40, 50, 60 , 70, 80))
    print(Player.teamName)
    print(p1.static_method())
    print(Player.static_method())
    print(p1.reveal_salary())
    print(p1._Player__salary) # trick to access the private property


if __name__ == "__main__":
    main()