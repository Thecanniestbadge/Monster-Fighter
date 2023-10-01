# Name: Nicholas Vickery
# Date: 5/31/2023
# Project: MonsterFighter
# This program allows the player to fight monsters "unfortunately, only text based right now "

import random

class Player:
    def __init__(self, health=100):
        self.health = health
        self.special_ability = 2

    def is_alive(self):
        return self.health > 0

    def heal(self):
        if self.health <= 70:
            self.health += 30
            print("You've healed yourself by 30 health points!")
        else:
            print("Your health is high enough already. You can't heal right now.")

class Monster:
    def __init__(self, type):
        self.type = type
        if self.type == "goblin":
            self.health = 30
            self.damage = 15
        elif self.type == "orc":
            self.health = 50
            self.damage = 20
        elif self.type == "dragon":
            self.health = 100
            self.damage = 30

    def is_alive(self):
        return self.health > 0

class Room:
    def __init__(self, num_monsters=3):
        self.monsters = [Monster(random.choice(["goblin", "orc", "dragon"])) for _ in range(num_monsters)]

class Dungeon:
    def __init__(self, player, num_rooms=5):
        self.player = player
        self.rooms = [Room(random.randint(1, 3)) for _ in range(num_rooms)]

    def player_attack(self, monster):
        choice = input("Enter your action (attack/heal/special): ")
        if choice == "attack":
            damage = random.randint(10, 30)
            monster.health -= damage
            print(f"You attacked the {monster.type} and inflicted {damage} damage points!")
        elif choice == "heal":
            self.player.heal()
        elif choice == "special":
            if self.player.special_ability > 0:
                damage = random.randint(20, 40)
                monster.health -= damage
                self.player.special_ability -= 1
                print(f"You used your special ability and inflicted {damage} damage points!")
            else:
                print("You are out of special abilities. Choose another action.")

    def monster_attack(self, monster):
        damage = random.randint(5, monster.damage)
        self.player.health -= damage
        print(f"The {monster.type} attacked you and inflicted {damage} damage points!")

    def play(self):
        for i in range(len(self.rooms)):
            print(f"You enter room #{i+1}.")
            for j in range(len(self.rooms[i].monsters)):
                print(f"A terrifying {self.rooms[i].monsters[j].type} is in front of you!")
                while self.player.is_alive() and self.rooms[i].monsters[j].is_alive():
                    self.player_attack(self.rooms[i].monsters[j])
                    if self.rooms[i].monsters[j].is_alive():
                        self.monster_attack(self.rooms[i].monsters[j])

                if self.player.is_alive():
                    print(f"Congratulations! You defeated the {self.rooms[i].monsters[j].type}!")
                else:
                    print("Unfortunately, you were defeated by the monster. Try again!")
                    return

            if i < len(self.rooms) - 1:  # If not last room
                print("You move on to the next room...")

        if self.player.is_alive():
            print("You have successfully traversed the entire dungeon. You are victorious!")
        else:
            print("Your adventure ends here. Better luck next time!")

if __name__ == "__main__":
    player = Player()
    dungeon = Dungeon(player, num_rooms=3)
    dungeon.play()
