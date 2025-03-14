from random import randint

from graphic_arts.graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Генерирует количество очков атаки."""
    if char_class == 'warrior':
        return (f'{char_name: str} нанёс  урон противнику, равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name: str} нанёс  урон противнику, равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name: str} нанёс  урон противнику, равный '
                f'{5 + randint(-3, -1)}')
    return ('урон противнику не нанесен')


def defence(char_name: str, char_class: str) -> str:
    """Генерирует количество очков защиты."""
    if char_class == 'warrior':
        return (f'{char_name: str} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name: str} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name: str} блокировал {10 + randint(2, 5)} урона')
    return ('не заблокировано')


def special(char_name: str, char_class: str) -> str:
    """Возвращает сообщениео применении специального усилия."""
    if char_class == 'warrior':
        return (f'{char_name: str} применил специальное умение «Выносливость '
                f'{80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name: str} применил специальное умение «Атака '
                f'{5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name: str} применил специальное умение «Защита '
                f'{10 + 30}»')
    return ('ничего не применял')


def start_training(char_name: str, char_class: str) -> str:
    """Запускает цикл тренировки навыков персонажа."""
    if char_class == 'warrior':
        print(f'{char_name: str}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name: str}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name: str}, ты Лекарь — чародей, '
              'способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Позволяет игроку выбрать тип игрового персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, '
                  'выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
