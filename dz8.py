class Player:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f"Игрок: {self.name}\nЗдоровье: {self.hp}\nУрон: {self.damage}\nБроня: {self.armor}"

    def get_damage(self, damage):
        damage_taken = max(damage - self.armor, 1)
        self.hp -= damage_taken

    def heal(self, heal_amount):
        self.hp += heal_amount

player1 = Player("Игрок 1", 100, 10, 5)
print(player1)
player1.get_damage(15)
print(f"После получения урона:\n{player1}")
player1.heal(20)
print(f"После восстановления здоровья:\n{player1}")
