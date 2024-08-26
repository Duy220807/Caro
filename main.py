import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
GRID_SIZE = 15
CELL_SIZE = 40
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE
LINE_WIDTH = 1  # Đường kẻ ô mỏng

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)  # Màu xám nhạt cho đường kẻ
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game Cờ Caro')

# Tạo bảng cờ
board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

def draw_board():
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(screen, GRAY, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), LINE_WIDTH)  # Đổi màu đường kẻ
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * CELL_SIZE + 5, row * CELL_SIZE + 5), ((col + 1) * CELL_SIZE - 5, (row + 1) * CELL_SIZE - 5), 4)  # Đậm hơn
                pygame.draw.line(screen, RED, ((col + 1) * CELL_SIZE - 5, row * CELL_SIZE + 5), (col * CELL_SIZE + 5, (row + 1) * CELL_SIZE - 5), 4)  # Đậm hơn
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLUE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5, 4)  # Đậm hơn
    pygame.display.flip()

def check_winner():
    def check_line(start_row, start_col, delta_row, delta_col):
        player = board[start_row][start_col]
        if player is None:
            return None
        count = 1
        for i in range(1, 5):
            row = start_row + i * delta_row
            col = start_col + i * delta_col
            if row < 0 or row >= GRID_SIZE or col < 0 or col >= GRID_SIZE or board[row][col] != player:
                return None
            count += 1
        return player if count == 5 else None
    
    # Kiểm tra hàng
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE - 4):
            winner = check_line(row, col, 0, 1)
            if winner:
                return winner
    
    # Kiểm tra cột
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 4):
            winner = check_line(row, col, 1, 0)
            if winner:
                return winner
    
    # Kiểm tra đường chéo
    for row in range(GRID_SIZE - 4):
        for col in range(GRID_SIZE - 4):
            winner = check_line(row, col, 1, 1)
            if winner:
                return winner
            winner = check_line(row, col + 4, 1, -1)
            if winner:
                return winner
    
    return None

def main():
    current_player = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE

                if board[row][col] is None:
                    board[row][col] = current_player
                    winner = check_winner()
                    if winner:
                        print(f'Người chơi {winner} thắng!')
                        game_over = True
                    current_player = 'O' if current_player == 'X' else 'X'

        draw_board()

if __name__ == '__main__':
    main()
