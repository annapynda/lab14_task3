from tictac.board import Board


def get_coords():
    """
    :return: coordinates for move
    """
    coords = str(input("Enter coordinates to make your move, exapmle: 1 1 : "))
    if len(coords) != 3:
        print('Enter coordinates correctly')
        while len(coords) != 3:
            coords = str(input("Enter coordinates to make your move, exapmle: 1 1 : "))

    coords = coords.split(' ')
    try:
        coords = [int(i)-1 for i in coords]
    except ValueError:
        print('Enter coordinates correctly')
        return False

    for i in coords:
        if i <= 0 or i > 3:
            raise ValueError('enter in range 1 to 3')

    return coords

def play():
    """
    The process of playing a game
    """
    b = Board()
    print(b)
    result = b.check_the_Board()

    while result :
        player1 = 1
        player2 = 2


        if b.check_haveplace() != 0:
            print('Player 1')
            try:
                first = get_coords()
            except ValueError as e:
                print(e)
                first = get_coords()

            if first!= False:
                try:
                    b.put_move(1, first)
                except IndexError as e:
                    print(e)
                    print('Player 1')
                    first = get_coords()
                    b.put_move(1, first)
                print(b)

        if b.check_the_Board() in ['EQUITY noone won', 'winner is first player', 'winner is second player']:
            result = False

        if b.check_haveplace() != 0 and result!= False:
            print('Player 2')
            try:
                second = get_coords()
            except ValueError as e:
                print(e)
                second = get_coords()

            if second != False:

                try:
                    b.put_move(2, second)
                except IndexError as e:
                    print(e)
                    print('Player 2')
                    second = get_coords()
                    b.put_move(2, second)
                print(b)

        if b.check_the_Board() in ['EQUITY noone won', 'winner is first player', 'winner is second player']:
            result = False

        if b.check_haveplace() == 0:
            result = False
    print(b.check_the_Board())


if __name__ == '__main__':
    play()







