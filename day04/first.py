with open("input.txt") as inp:
    nums, *boards = inp.read()[:-1].split("\n\n")


def format_board(raw: str):
    return [[(int(num), False) for num in row.split()] for row in raw.split('\n')]


def check_board(board: list) -> bool:
    # check rows
    for i in range(5):
        for j in range(5):
            if not board[i][j][1]:
                break
        else:
            return True

    # check columns
    for i in range(5):
        for j in range(5):
            if not board[j][i][1]:
                break
        else:
            return True


def update_board(board: list, num: int) -> None:
    for row in board:
        for i in range(len(row)):
            if row[i][0] == num:
                row[i] = (num, True)
                return


def score_board(board: list) -> int:
    score = 0
    for row in board:
        for num, selected in row:
            score += num if not selected else 0
    return score


def run_bingo(nums, boards) -> int:
    for num in nums:
        for board in boards:
            update_board(board, num)
            if check_board(board):
                return score_board(board) * num


nums = list(map(int, nums.split(',')))
boards = list(map(format_board, boards))

# print(run_bingo(nums, boards))
