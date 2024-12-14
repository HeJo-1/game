import curses
import random

def snake_game():
    screen = curses.initscr()
    curses.curs_set(0)
    screen.keypad(1)
    screen.timeout(100)

    # Oyun alanı boyutları
    height, width = 20, 60
    window = curses.newwin(height, width, 0, 0)
    window.keypad(1)
    window.timeout(100)

    # Yılanın başlangıç konumu
    snake = [[10, 15], [10, 14], [10, 13]]
    snake_direction = curses.KEY_RIGHT

    # İlk yem
    food = [random.randint(1, height - 2), random.randint(1, width - 2)]
    window.addch(food[0], food[1], curses.ACS_PI)

    while True:
        next_key = window.getch()
        if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            snake_direction = next_key

        # Yeni kafa pozisyonu
        head = snake[0]
        if snake_direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        elif snake_direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif snake_direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif snake_direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]

        # Yılanın kendini yemesi veya duvara çarpması
        if (new_head in snake or
            new_head[0] <= 0 or new_head[1] <= 0 or
            new_head[0] >= height - 1 or new_head[1] >= width - 1):
            break

        # Yılanın büyümesi
        snake.insert(0, new_head)
        if new_head == food:
            food = [random.randint(1, height - 2), random.randint(1, width - 2)]
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        # Yeni kafa pozisyonunu ekrana yaz
        window.addch(new_head[0], new_head[1], '*')

    curses.endwin()
    print("Oyun Bitti! Skorunuz: ", len(snake) - 3)

if __name__ == "__main__":
    snake_game()
