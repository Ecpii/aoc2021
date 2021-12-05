from first import check_board, update_board, score_board, nums, boards


def run_bingo(nums, boards) -> int:
    for num in nums:
        for i in range(len(boards) - 1, -1, -1):  # reverse order because removing items
            board = boards[i]
            update_board(board, num)
            if check_board(board):
                if len(boards) == 1:
                    return score_board(board) * num
                boards.remove(board)


print(run_bingo(nums, boards))
