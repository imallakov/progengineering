from math import sqrt


class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        print('Weapon.hit()')
        if not target.is_alive():
            print('Враг уже повержен')
        else:
            if get_distance(actor, target) <= self.range:
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
                target.get_damage(self.damage)
            else:
                print(f'Враг слишком далеко для оружия {self.name}')


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.x = pos_x
        self.y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def is_alive(self) -> bool:
        if self.hp > 0:
            return True
        else:
            return False

    def get_damage(self, amount):
        self.hp -= min(amount, self.hp)

    def get_coords(self):
        return self.x, self.y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon: Weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        print('BaseEnemy.hit()')
        if type(target) is MainHero:
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.weapon_index = -1

    def hit(self, target):
        if len(self.weapons) == 0:
            print('Я безоружен')
        else:
            if type(target) is BaseEnemy:
                if not target.is_alive():
                    print('Враг уже повержен')
                else:
                    if get_distance(self, target) <= self.weapons[self.weapon_index].range:
                        print(
                            f'Врагу нанесен урон оружием {self.name} в размере {self.weapons[self.weapon_index].damage}')
                        target.get_damage(self.weapons[self.weapon_index].damage)
                    else:
                        print(f'Враг слишком далеко для оружия {self.weapons[self.weapon_index].name}')
            else:
                print('Могу ударить только Врага')

    def add_weapon(self, weapon):
        if type(weapon) is Weapon:
            self.weapons.append(weapon)
            self.weapon_index = 0
            print(f'Подобрал {weapon.name}')
        else:
            print('Это не оружие')

    def next_weapon(self):
        if len(self.weapons) == 0:
            print('Я безоружен')
        elif len(self.weapons) == 1:
            print('У меня только одно оружие')
        else:
            self.weapon_index += 1
            if self.weapon_index == len(self.weapons):
                self.weapon_index = 0
            print(f'Сменил оружие на {self.weapons[self.weapon_index].name}')

    def heal(self, amount):
        self.hp += amount
        self.hp = min(self.hp, 200)
        print(f'Полечился, теперь здоровья {self.hp}')


def get_distance(person1: BaseCharacter, person2: BaseCharacter):
    x1, y1 = person1.get_coords()
    x2, y2 = person2.get_coords()
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)
