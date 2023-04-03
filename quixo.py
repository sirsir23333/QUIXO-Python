import random
import math


def check_move(board, turn, index, push_from):
    n = int(math.sqrt(len(board)))
    left_check = []  # store numbers which can do left
    right_check = []  # store numbers which can do right
    top_check = []  # store numbers which can't do top
    bot_check = []  # store numbers which can't do bot
    if index < 0 or index >= n * n:  # Index can't be negative or greater or equals to the squared of size
        return False
    if push_from == "L":
        for j in range(1, int(n - 1)):  # top row without 2 edge
            left_check.append(j)
        for i in range(n - 1, n * n, n):  # right side whole colomn
            left_check.append(i)
        for k in range(int(n * (n - 1) + 1), int(n * n - 1)):  # bottom row without 2 edge
            left_check.append(k)
        if index not in left_check:
            return False
    elif push_from == "R":
        for j in range(1, int(n - 1)):  # top row without 2 edge
            right_check.append(j)
        for k in range(int(n * (n - 1) + 1), int(n * n - 1)):  # bottom row without 2 edge
            right_check.append(k)
        for m in range(0, n * n, n):  # left side whole column
            right_check.append(m)
        if index not in right_check:
            return False
    elif push_from == "T":
        for i in range(int(n * (n - 1)), int(n * n)):  # bottom row
            top_check.append(i)
        for lelf_column in range(int(n), int(n * n - n), int(n)):  # left column without 2 edge
            top_check.append(lelf_column)
        for right_column in range(int(2 * n - 1), int(n * n - 1), int(n)):  # right column without 2 edge
            top_check.append(right_column)
        if index not in top_check:
            return False
    elif push_from == "B":
        for num in range(int(n)):  # top row
            bot_check.append(num)
        for lelf_column in range(int(n), int(n * n - n), int(n)):  # left column without 2 edge
            bot_check.append(lelf_column)
        for right_column in range(int(2 * n - 1), int(n * n - 1), int(n)):  # right column without 2 edge
            bot_check.append(right_column)
        if index not in bot_check:
            return False
    else:  # This is for if player enter an invalid character
        return False
    if turn == 1:  # this is for making sure that player 1 cannot move 2
        if board[index] != 1 and board[index] != 0:
            return False
    if turn == 2:  # this is for making sure that player 2 cannot move 1
        if board[index] != 2 and board[index] != 0:
            return False
    return True  # Other than all the invalid moves, we shall return True


# For apply move, we basically divide in four parts, which is the four directions
def apply_move(board, turn, index, push_from):
    n = int(math.sqrt(len(board)))
    board_1 = board[:]  # we duplicate the board in order to not modify on board directly,
    # we will also return board_1 instead of board
    if push_from == 'T':
        if n * (n - 1) <= index < n ** 2:  # bottom row
            # below is the arranging method like bubble sort.
            # and we will use the same method throughout the whole apply move!!
            for i in range(0, n ** 2 - n, n):
                board_1[index - i] = board_1[index - (i + n)]
            board_1[index - index // n * n] = turn
            return board_1
        elif index % n == 0 and index != 0 and index != n * (n - 1):  # left column without both edge
            for i in range(0, index, n):
                board_1[index - i] = board_1[index - (i + n)]
            board_1[index - index // n * n] = turn
            return board_1
        elif index % n == n - 1 and index != n - 1 and index != n ** 2 - 1:  # right column without both edge
            for i in range(0, index // n * n, n):
                board_1[index - i] = board_1[index - (i + n)]
            board_1[index - index // n * n] = turn
            return board_1
    elif push_from == "B":
        if 0 < index < n - 1:  # top row without 2 edges
            for i in range(0, int(n ** 2 - n), int(n)):
                board_1[index + int(i)] = board_1[index + int((i + n))]
            board_1[index - index // n * n + n * (n - 1)] = turn
            return board_1
        elif index % n == 0 and index != n * (n - 1):  # left column wihtout bottom left element
            for i in range(0, -1 * index + n * (n - 1), n):
                board_1[index + i] = board_1[index + (i + n)]
            board_1[index - index // n * n + n * (n - 1)] = turn
            return board_1
        elif index % n == n - 1 and index != n ** 2 - 1:  # right column without bottom right element
            for i in range(0, n * (n - (index // n + 1)), n):
                board_1[index + i] = board_1[index + (i + n)]
            board_1[index - index // n * n + n * (n - 1)] = turn
            return board_1

    elif push_from == "R":
        if index % n == 0 and index != 0 and index != n * (n - 1):  # left column without both edges
            for i in range(0, n - 1, 1):
                board_1[index + i] = board_1[index + i + 1]
            board_1[index // n * n + n - 1] = turn
            return board_1
        elif 0 <= index < n:  # top row without top right element
            for i in range(0, -1 * index + (n - 1), 1):
                board_1[index + i] = board_1[index + i + 1]
            board_1[index // n * n + n - 1] = turn
            return board_1
        elif n * (n - 1) <= index < n ** 2 - 1:  # bottom row without bottom right element
            for i in range(0, -1 * index + n ** 2 - 1, 1):
                board_1[index + i] = board_1[index + i + 1]
            board_1[index // n * n + n - 1] = turn
            return board_1
    elif push_from == "L":
        if index % n == n - 1 and index != n - 1 and index != n ** 2 - 1:  # right column without both edges
            for i in range(0, n - 1, 1):
                board_1[index - i] = board_1[index - i - 1]
            board_1[index // n * n] = turn
            return board_1
        elif 0 < index <= n - 1:  # top row without top left element
            for i in range(0, index, 1):
                board_1[index - i] = board_1[index - i - 1]
            board_1[index // n * n] = turn
            return board_1
        elif n * (n - 1) < index <= n ** 2 - 1:  # bottom row without bottom left element
            for i in range(0, index - n * (n - 1), 1):
                board_1[index - i] = board_1[index - i - 1]
            board_1[index // n * n] = turn
            return board_1


def check_victory(board, who_played):
    # global n
    n = int(math.sqrt(len(board)))
    winner = ""  # winner is for showing who is winner, but since this is just the start
    # of the function, so we just assign a empty value first
    diagonal1 = []  # the check list for diagonal from top left to bottom right
    diagonal2 = []  # the check list for diagonal from bottom left to top right
    column = []  # each column
    check = []  # this is a list to check victory
    row = []  # each row
    for i in range(0, int(n * n), int(n + 1)):  # all the index of diagonal1,
        diagonal1.append(i)
    for j in diagonal1:
        check.append(board[j])  # now check list have 1st diagonal values
    if (0 not in check) and (1 not in check):  # this means player 2 win!
        winner += "2"
    elif (0 not in check) and (2 not in check):  # this means player 1 win!
        winner += "1"

    check = []  # reset

    # the second diagonal check is same as the first
    for k in range(n - 1, int(n * n - 1), int(n - 1)):  # 2nd diagonal check
        diagonal2.append(k)
    for m in diagonal2:
        check.append(board[m])
    if (0 not in check) and (1 not in check):
        winner += "2"
    elif (0 not in check) and (2 not in check):
        winner += "1"
    check = []  # reset

    # now we start to check each columns
    for counter in range(int(n)):  # counter is the index of column, starts from 0, until n-1
        for r in range(int(counter), int(n * n), int(n)):  # index of the corresponding column
            column.append(r)
        for index in column:
            check.append(board[index])  # now check list have corresponding column for each iteration
        if (0 not in check) and (1 not in check):  # player 2 win
            winner += "2"
        elif (0 not in check) and (2 not in check):  # player 1 win
            winner += "1"
        column = []  # reset
        check = []  # reset

    # now we check for the row! it is basically same as column check, so i won't do further explainations
    for counter in range(int(n)):  # counter is the index of rows, starts from 0, until n-1
        for r in range(counter * n, n + counter * n):
            row.append(r)
        for index in row:
            check.append(board[index])
        if (0 not in check) and (1 not in check):
            winner += "2"
        elif (0 not in check) and (2 not in check):
            winner += "1"
        row = []
        check = []
    if winner == "":  # no one win
        return 0
    elif len(winner) != 1:  # got more than one line of 1 or 2
        check_1 = []
        for i in winner:
            check_1.append(int(i))  # we change winner into a list
            # for instance, in winner="1212", then check_1=[1,2,1,2]
        check_1 = list(set(check_1))  # this step is to get rid of the repeated elements
        if len(check_1) == 1:  # means that this is not a move that leads to a line of 1 plus a line of 2
            if 1 not in check_1:  # means the list only have 2
                return 2
            else:  # means the list only have 1
                return 1
        else:  # means that this is a step that leads to at least a line of 1 plus a line of 2
            # in such case, whoever makes the move lose
            if who_played == 1:
                return 2
            else:
                return 1
    else:
        return int(winner)  # if the length of winner is 1, then the winner is obvious!


def computer_move(board, turn, level):
    global n
    n = math.sqrt(len(board))
    who_played = 1

    # this is the computer level 1 case
    if level == 1:
        while True:  # this loop will only break when computer picks a valid move
            index = random.randint(0, n * n - 1)
            push_from = random.choice("TBLR")
            if check_move(board, turn, index, push_from):
                break
        return index, push_from


    # This is the level 2 case.
    # We define computer move as cpt,****** important
    # We define player move as plt.***** important
    # Inside the function, I have defined a "direct_win_check(board,turn)",
    # this function is for checking whether a board satisfy the condition when it is only one move to win

    elif level == 2:
        n = int(math.sqrt(len(board)))
        cpt = turn  # because this is a computer move function, so the turn is always computer turn
        # the if-else part is for assigning correspoding value to plt when cpt is 1 or 2
        if cpt == 1:
            plt = 2
        else:
            plt = 1

        # The start of direct_win_check function!!
        # For this function, we divided into: column check, row check, and two diagonal check
        # For column check, we divide into 9 parts, which is 4*edge elements,
        # 4*sides without edges part  and the rest of the board(which is the middle)
        # For row check, we also apply the same concept as column
        # For diagonal check, there is no need to divide parts, just 2 different diagonals
        # k is the index where when it is replaced by plt or cpt, respective player will win
        # The important concept of this function is finding the index_of_k
        # Once we find index_of_k, we just need to see the index beside it, so that we find
        # a way to push those index to k if it can win!
        # There will be left_number, right_number, top_number,bottom_number in this function
        # these four variable simply means the value of the index beside k
        def direct_win_check(board, turn):
            turn = cpt  # turn and cpt should be the same in this function

            # This is the start of column direct win check
            column_inlist = []  # column_inlist is for storing values for each column
            for column_index in range(n):  # This is to check one column at a time.
                for index in range(column_index, n * n, n):  # This is to represent the indexes in one column
                    column_inlist.append(board[index])  # From here, column_inlist have stored one column of value
                count_of_cpt = column_inlist.count(cpt)  # this is to count how many cpt are there in a column
                # When cpt in one to n, then we can say that it is going to win
                # While this also implies that the outlier value that is not cpt can only
                # be plt or 0
                if count_of_cpt == n - 1:
                    row_of_k = 0
                    for k in column_inlist:
                        if k == cpt:
                            row_of_k += 1  # we know where k's row is
                        else:
                            break
                    # we know the row and column of k, then we have index_of_k
                    index_of_k = (column_index) + (row_of_k) * n

                    # from here onwards, we start to divide the board into 9 parts,
                    # which i have already mentioned.

                    if 0 < column_index < n - 1:  # middle columns
                        left_number = board[index_of_k - 1]
                        right_number = board[index_of_k + 1]

                        # under this line will be the middle elements of the board!
                        # for this part we will check if the left_number and right_number
                        # is k or not, if it is, then we will find corresponding index to push
                        # and we also need to make sure the index cannot be plt, or else it
                        # will be an invalid move!
                        if 1 <= index_of_k // n < n - 1:  # middle elements in the middle columns
                            if left_number == cpt:  # left side of k is cpt
                                index = index_of_k // n * n + (n - 1)
                                if board[index] != plt:
                                    push_from = "L"
                                    # under this line will be a test to ensure such a move will
                                    # not make the player win strait away after computer move
                                    # I will implement this before every return in this function
                                    # I will not explain this again for making the program tidier...
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from

                            if right_number == cpt:  # right side is cpt
                                index = index_of_k // n * n
                                if board[index] != plt:
                                    push_from = "R"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from


                        elif index_of_k // n == 0:  # top elements in the middle columns
                            # which is the top row without edges
                            first_row = []
                            if left_number == cpt:  # left hand side is cpt
                                # if the left hand side is cpt, then we will need to check
                                # the right side of the cpt in the top row excluding the top right element
                                # if there is cpt or 0, then we can move
                                # so below is checking if there is any 0 or cpt
                                for index in range(index_of_k, n):
                                    first_row.append(board[index])
                                count = 0
                                for i in first_row:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                if len(first_row) != count:  # ensure that first_row have 0 or cpt
                                    index = index_of_k + count
                                    push_from = "L"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                            # below is the situation where right hand side is cpt
                            # which is about the same as above
                            if right_number == cpt:
                                first_row = []
                                for index in range(0, index_of_k + 1):
                                    first_row.append(board[index])
                                count = 0
                                for i in first_row:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                if len(first_row) != count:  # ensure that first_row have 0 or cpt
                                    index = count
                                    push_from = "R"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from

                            # we also need to consider when k is 0, then we can win with a simple move
                            # because we can just move k!
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "B"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                        # below is just the bottom row without 2 edges
                        # this is applying the same concept as above!

                        elif index_of_k // n == n - 1:  # bottom elements in the middle columns
                            bottom_row = []
                            if left_number == cpt:
                                for index in range(index_of_k, n * n):
                                    bottom_row.append(board[index])
                                count = 0
                                for i in bottom_row:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                if len(bottom_row) != count:  # ensure have 0 or cpt
                                    index = index_of_k + count
                                    push_from = "L"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                            if right_number == cpt:
                                bottom_row = []
                                for index in range(n * (n - 1), index_of_k + 1):
                                    bottom_row.append(board[index])
                                count = 0
                                for i in bottom_row:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                if len(bottom_row) != count:  # ensure have 0 or cpt
                                    index = index_of_k - count
                                    push_from = "R"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "T"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                    # until now,we have left with the left column and right column element to check

                    # below is the left column
                    # there is 3 part out of the 9 parts in here
                    # which is the 2 edges and the rest(left column without edges)
                    elif column_index == 0:  # left extreme side columns
                        # actually the left hand side means the right extreme value!
                        left_number = board[index_of_k + n - 1]
                        right_number = board[index_of_k + 1]
                        # left column wihtout edges
                        if 0 < index_of_k // n < n - 1:  # middle elements
                            if left_number == cpt or left_number == 0:  # if such, then we can just move left number to win
                                index = index_of_k + n - 1
                                push_from = "L"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            # after checking the lhs, we check rhs
                            if right_number == cpt and index_of_k != plt:

                                index = index_of_k

                                if board[index] != plt:

                                    push_from = "R"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from

                            # we just consider the case when k is 0
                            # it is an easy win again
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "B"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                                    # We start to check the edges
                        elif index_of_k // n == 0:  # tl element
                            if board[index_of_k] == 0:  # if top left equal 0, then can win directly
                                index = index_of_k
                                push_from = "B"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            else:  # if top left is not equal to 0, then we need to check
                                # the first row if there is any cpt or 0
                                first_row = []
                                for index in range(0, n):
                                    first_row.append(board[index])
                                count = 0
                                for i in first_row:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                index = count
                                push_from = "L"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                        elif index_of_k // n == n - 1:  # bl element
                            # this is same as above
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "T"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            else:
                                bottom_row = []
                                for index in range(n * (n - 1), n * n):
                                    bottom_row.append(board[index])
                                count = 0
                                for i in bottom_row:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                index = index_of_k + count
                                push_from = "L"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from


                    # this is same as left extreme side column
                    else:  # right extreme side column

                        left_number = board[index_of_k - 1]
                        right_number = board[index_of_k - n + 1]
                        if 0 < index_of_k // n < n - 1:  # middle elements
                            if left_number == cpt:
                                index = index_of_k
                                if board[index] != plt:
                                    push_from = "L"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return (index, push_from)

                            if right_number == cpt or right_number == 0:
                                index = index_of_k - n + 1
                                push_from = "R"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return (index, push_from)

                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "B"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return (index, push_from)


                        elif index_of_k // n == 0:  # tr element
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "B"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            else:
                                first_row = []
                                for index in range(0, n - 1):
                                    first_row.append(board[index])
                                count = 0
                                for i in first_row:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                index = count
                                push_from = "R"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                        elif index_of_k // n == n - 1:  # br element
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "T"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            else:
                                bottom_row = []
                                for index in range(n * (n - 1), n * n - 1):
                                    bottom_row.append(board[index])
                                count = 0
                                for i in bottom_row:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                index = n * (n - 1) + count
                                push_from = "R"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                    column_inlist = []
                else:
                    column_inlist = []  # reset

            # this is the start of row check
            # all concpet is same as the column check
            # we just need to check the top number and bottom number of k
            # instead of left and right in the column check
            # I won't do explanation because of such

            row_inlist = []
            for row_index in range(n):
                for index in range(row_index * n, row_index * n + n):
                    row_inlist.append(board[index])
                count_of_2 = row_inlist.count(cpt)
                # print(row_inlist)
                # print(cpt)

                if count_of_2 == n - 1:  # we check if the row that need one more cpt to win
                    column_of_k = 0
                    for k in row_inlist:
                        if k == cpt:
                            column_of_k += 1
                        else:
                            break

                    index_of_k = (row_index) * n + (column_of_k)

                    # print(row_index,column_of_k,index_of_k)

                    if 0 < row_index < n - 1:  # middle rows
                        if 0 < index_of_k % n < n - 1:  # middle elements in middle rows
                            top_number = board[index_of_k - n]
                            bottom_number = board[index_of_k + n]
                            if top_number == cpt:
                                index = index_of_k - index_of_k // n * n + n * (n - 1)
                                if board[index] != plt:
                                    push_from = "T"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from

                            if bottom_number == cpt:
                                index = index_of_k - index_of_k // n * n
                                if board[index] != plt:
                                    push_from = "B"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                                else:
                                    pass

                        elif index_of_k % n == 0:  # left column elements in middle rows
                            top_number = board[index_of_k - n]
                            bottom_number = board[index_of_k + n]
                            left_column = []
                            if top_number == cpt:  # top element of k is cpt
                                for index in range(index_of_k, n * (n - 1) + 1, n):
                                    left_column.append(board[index])
                                count = 0
                                for i in left_column:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                if len(left_column) != count:  # ensure that left_column have 0 or cpt
                                    index = index_of_k + count * n
                                    push_from = "T"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                            if bottom_number == cpt:
                                left_column = []
                                for index in range(0, index_of_k + 1, n):
                                    left_column.append(board[index])
                                count = 0
                                for i in left_column:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                if len(left_column) != count:  # ensure that left_column have 0 or cpt
                                    index = count * n
                                    push_from = "B"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "R"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                        elif index_of_k % n == n - 1:  # right column elements in the middle rows
                            top_number = board[index_of_k - n]
                            bottom_number = board[index_of_k + n]
                            right_column = []
                            if top_number == cpt:
                                for index in range(index_of_k, n * n, n):
                                    right_column.append(board[index])
                                count = 0
                                for i in right_column:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                if len(right_column) != count:  # ensure have 0 or cpt
                                    index = index_of_k + count * n
                                    push_from = "T"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                            if bottom_number == cpt:
                                right_column = []
                                for index in range(n - 1, index_of_k + 1, n):
                                    right_column.append(board[index])
                                count = 0
                                for i in right_column:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                if len(right_column) != count:  # ensure have 0 or cpt
                                    index = (count + 1) * n - 1
                                    push_from = "B"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "T"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                    elif row_index == 0:  # top extreme row
                        # print("a")
                        top_number = board[index_of_k + n * (n - 1)]
                        bottom_number = board[index_of_k + n]
                        if 0 < index_of_k < n - 1:  # middle element in top row
                            if top_number == cpt or 0:
                                index = index_of_k + (n - 1) * n
                                push_from = "T"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                            if bottom_number == cpt:
                                index = index_of_k
                                if board[index] != plt:
                                    push_from = "B"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                                else:
                                    pass

                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "R"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                        elif index_of_k == 0:  # top left element
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "R"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            else:
                                left_column = []
                                for index in range(0, n * (n - 1) + 1, n):
                                    left_column.append(board[index])
                                count = 0
                                for i in left_column:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                index = count * n
                                push_from = "T"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                        elif index_of_k == n - 1:  # top right element
                            # print("b")
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "L"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            else:
                                right_column = []
                                for index in range(n - 1, n * n, n):
                                    right_column.append(board[index])
                                count = 0
                                for i in right_column:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                index = index_of_k + count * n
                                push_from = "T"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from


                    else:  # bottom extreme row
                        if n * (n - 1) < index_of_k < n * n - 1:  # middle elements in bottom row
                            top_number = board[index_of_k - n]
                            bottom_number = board[index_of_k - (n * (n - 1))]
                            if top_number == cpt:
                                index = index_of_k
                                if board[index] != plt:
                                    push_from = "T"
                                    temp = apply_move(board, turn, index, push_from)
                                    if check_victory(temp, who_played) != plt:
                                        return index, push_from
                            if bottom_number == cpt or 0:
                                index = index_of_k - (n * (n - 1))
                                push_from = "B"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "R"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                        elif index_of_k == n * (n - 1):  # bottom left element
                            top_number = board[index_of_k - n]
                            bottom_number = board[index_of_k - (n * (n - 1))]
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "R"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            else:
                                left_column = []
                                for index in range(0, n * (n - 1) + 1, n):
                                    left_column.append(board[index])
                                count = 0
                                for i in left_column:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                index = count * n
                                push_from = "B"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                        elif index_of_k == n * n - 1:  # bottom right element
                            top_number = board[index_of_k - n]
                            bottom_number = board[index_of_k - (n * (n - 1))]
                            if board[index_of_k] == 0:
                                index = index_of_k
                                push_from = "L"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from
                            else:
                                right_column = []
                                for index in range(n - 1, n * n, n):
                                    right_column.append(board[index])
                                count = 0
                                for i in right_column:
                                    if i == plt:
                                        count += 1
                                    else:
                                        break
                                index = (count + 1) * n - 1
                                push_from = "B"
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:
                                    return index, push_from

                    row_inlist = []
                else:
                    row_inlist = []

            diagonal_inlist_1 = []
            # The first diagonal will the the one from the top left to bottom right
            # we also divide it into 3 parts
            # the top left, the bottom right , and the rest(the middle)

            for i in range(0, int(n * n), int(n + 1)):  # 1st diagonal
                diagonal_inlist_1.append(board[i])
            count_of_2 = diagonal_inlist_1.count(cpt)

            if count_of_2 == n - 1:
                column_of_k = 0
                for k in diagonal_inlist_1:
                    if k == cpt:
                        column_of_k += 1
                    else:
                        break

                row_of_k = column_of_k
                index_of_k = (row_of_k) * n + (column_of_k)

                # below is the start of the middle part
                # for the middle, we just need to combine the strategy of row and column check
                # this means that we need to check top, bot, left and right side of k together
                if 0 < row_of_k < n - 1:  # middle diagonal
                    top_number = board[index_of_k - n]
                    bottom_number = board[index_of_k + n]
                    left_number = board[index_of_k - 1]
                    right_number = board[index_of_k + 1]
                    if top_number == cpt:
                        index = index_of_k - index_of_k // n * n + n * (n - 1)
                        if board[index] != plt:
                            push_from = "T"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                    if bottom_number == cpt:
                        index = index_of_k - index_of_k // n * n
                        if board[index] != plt:
                            push_from = "B"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                    if left_number == cpt:
                        index = index_of_k // n * n + (n - 1)
                        if board[index] != plt:
                            push_from = "L"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                    if right_number == cpt:
                        index = index_of_k // n * n
                        if board[index] != plt:
                            push_from = "R"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from


                # below is to check the top left for 1st diaganol
                elif row_of_k == 0:  # tl element
                    # below is to check the first row wheter have 0 or cpt to move for a win
                    index = 1
                    for first_row in range(1, n):
                        if board[first_row] != cpt and board[first_row] != 0:

                            index += 1

                        else:
                            push_from = "L"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from
                    # below is to check the left column whether have 0 or cpt to move for win
                    index = n
                    for first_column in range(n, n * n, n):
                        if board[first_column] != cpt and board[first_row] != 0:
                            index += n
                        else:
                            push_from = "T"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                # same as top left checking method
                elif row_of_k == n - 1:  # br element
                    index = n - 1
                    for right_column in range(n - 1, n * n, n):
                        if board[right_column] != cpt and board[right_column] != 0:
                            index += n
                        else:
                            push_from = "B"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                    index = n * (n - 1)
                    for last_row in range(index, n * n - 1, 1):
                        if board[last_row] != cpt and board[last_row] != 0:
                            index += 1
                        else:
                            push_from = "R"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

            # this is same as the other diaganol checking above
            diagonal_inlist_2 = []
            for q in range(n - 1, int(n * n) - 1, int(n - 1)):  # 2nd diagonal check
                diagonal_inlist_2.append(board[q])
            count_of_2 = diagonal_inlist_2.count(cpt)

            if count_of_2 == n - 1:
                row_of_k = 0
                for k in diagonal_inlist_2:
                    if k == cpt:
                        row_of_k += 1
                    else:
                        break

                column_of_k = n - 1 - row_of_k
                index_of_k = row_of_k * n + column_of_k

                if 0 < row_of_k < n - 1:  # middle diagonal
                    top_number = board[index_of_k - n]
                    bottom_number = board[index_of_k + n]
                    left_number = board[index_of_k - 1]
                    right_number = board[index_of_k + 1]

                    if top_number == cpt:
                        index = index_of_k - index_of_k // n * n + n * (n - 1)
                        if board[index] != plt:
                            push_from = "T"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                    if bottom_number == cpt:
                        index = index_of_k - index_of_k // n * n
                        if board[index] != plt:
                            push_from = "B"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                    if left_number == cpt:
                        index = index_of_k // n * n + (n - 1)
                        if board[index] != plt:
                            push_from = "L"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                    if right_number == cpt:
                        index = index_of_k // n * n
                        if board[index] != plt:
                            push_from = "R"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from


                elif row_of_k == 0:  # tr element
                    index = 0
                    for first_row in range(0, n - 1):
                        if board[first_row] != cpt and board[first_row] != 0:
                            index += 1
                        else:
                            push_from = "R"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                    index = 2 * n - 1
                    for last_column in range(index, n * n, n):
                        if board[last_column] != cpt and board[last_column] != 0:
                            index += n
                        else:
                            push_from = "T"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

                elif row_of_k == n - 1:  # bl element
                    index = 0
                    for right_column in range(index, n * n, n):
                        if board[right_column] != cpt and board[right_column] != 0:
                            index += n
                        else:
                            push_from = "B"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return (index, push_from)

                    index = n * (n - 1) + 1
                    for last_row in range(index, n * n, 1):
                        if board[last_row] != cpt and board[last_row] != 0:
                            index += 1
                        else:
                            push_from = "L"
                            temp = apply_move(board, turn, index, push_from)
                            if check_victory(temp, who_played) != plt:
                                return index, push_from

            index = ""  # if no direct win case
            push_from = ""
            return (index, push_from)  # no direct win step, then index,push_from= ("","")

        result = direct_win_check(board, turn)  # if no dierect win for computer, result is always "",""
        # print(result)

        # after checking if there is any direct win case(also prevent player for winning before next round)
        # we still need to check if the player can win with one move the next turn
        # the basic idea is we pick a random move at the start, and we test if it is valid
        # we also test if it can make the player win without next round
        # after it passes these two tests, we then creat a temporary board for such a move
        # then we check such a board have a direct win case or not!
        # We also create a all_move list, this contain all the possible move!
        # we will delete the moves in all_move once the move have been shown by our
        # algorithm that it cannot pass all the test stated above
        # if not a move can prevent winne from winning the next round, then computer
        # have no choice but to pick a random move!

        all_move = []
        for direction in "TBRL":
            for number in range(0, n * n):
                t = (number, direction)
                all_move.append(t)

        while result in [("", "")]:  # if don't have direct win
            # print('i am here')
            index = random.randint(0, n * n - 1)
            push_from = random.choice("TBLR")
            if (index, push_from) in all_move:
                all_move.remove((index, push_from))
            if check_move(board, turn, index, push_from):  # if move is valid
                temp = apply_move(board, turn, index, push_from)
                if check_victory(temp, who_played) != plt:  # make sure the step dont make player win
                    if cpt == 1:  # need to change the turn to check for player for direct_win_check
                        cpt = 2
                        plt = 1
                    else:
                        cpt = 1
                        plt = 2
                    # print("CPT SHOULD BE 1")
                    if direct_win_check(temp, cpt) not in [("", "")]:  # player can win next round
                        if cpt == 1:  # need to change the turn back before check_move again
                            cpt = 2
                            plt = 1
                        else:
                            cpt = 1
                            plt = 2
                        if not all_move:
                            index = random.randint(0, n * n - 1)
                            push_from = random.choice("TBLR")
                            if check_move(board, turn, index, push_from):  # if move is valid
                                temp = apply_move(board, turn, index, push_from)
                                if check_victory(temp, who_played) != plt:  # make sure the step dont make player win
                                    return index, push_from
                        else:
                            continue

                    else:  # player won't win next round
                        if cpt == 1:
                            cpt = 2
                            plt = 1
                        else:
                            cpt = 1
                            plt = 2
                        return (index, push_from)

        return result  # direct win result


# for display board, we use a for loop to slice the board list
def display_board(board):
    n = int(math.sqrt(len(board)))
    counter = n

    for num in range(0, n * n, n):
        row = board[num:counter]

        print(row)

        counter += n


# The basic idea for menu is to combine all the function defined above
# At the start we input n as the board size and we create board base on n
# then we let user choose to play with computer or other player
def menu():
    who_played = 1
    n = -1  # this is just a value to enter the loop
    while n < 2:  # we ensured that the board size must be at least 2!
        while True:  # ensure that user enter an integer for board size!
            try:
                n = input("Enter board size that is at least 2:")
                n_float = float(n)
            except ValueError:
                print("Please enter an number!")
                continue
            else:
                if math.floor(n_float) != n_float:  # this means that n is not integer
                    print("Please enter an integer!")
                else:  # this means that n is a integer and don't have error
                    n = int(n_float)
                    break

    board = [0] * (n * n)  # we create board
    # board = [1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0]

    turn = 1
    who_played = turn
    npc = "a"  # this is just a random value before the player input anything
    Winner = 0
    while True:  # this step make sure input is Computer or Player
        npc = input("Playing with Player or Computer ? :")
        if npc == "Computer" or npc == "Player":
            break
        else:
            print("Please enter correctly, Python is case sensitive")

    # this is when player vs player!
    if npc == "Player":
        display_board(board)
        while True:
            Winner = check_victory(board, who_played)  # we will put check victory at the start
            if Winner != 0:  # got someone win
                print("Winner is Player ", Winner)
                break
            else:  # no one win
                print("It is Player", turn, "'s turn.")

                while True:  # ensure that user enter an integer!
                    try:
                        index = input("Which index do you want to push? : ")
                        index_float = float(index)
                    except ValueError:
                        print("Please enter an integer!")
                        continue
                    else:
                        if math.floor(index_float) != index_float:
                            print("Please enter an integer!")
                        else:
                            index = int(index_float)
                            break

                push_from = input("Which direction would you like to push from? :")
            if check_move(board, turn, index, push_from) == True:  # valid move
                updated_list = apply_move(board, turn, index, push_from)
                board = updated_list
                display_board(board)
                if turn == 1:  # we will change turn after one player make a move
                    turn = 2
                else:
                    turn = 1
            else:  # invalid move
                print("Invalid move.")
                continue

        # for computer
        # we can choose to go first(turn 1) or second(turn 2)
        # after that, we can choose the level(1 or 2)
    elif npc == "Computer":  # when we choose to fight with a computer
        plt_1 = -1  # this is just a value to enter the loop
        while plt_1 != "1" and plt_1 != "2":  # we ensure that player turn must be either 1 or 2
            plt_1 = input("Choose your turn, Enter 1 to go first, Enter 2 to go second:")

        plt = int(plt_1)
        if plt == 1:  # this is just to assign value to plt and cpt
            cpt = 2
        else:
            cpt = 1

        while True:  # this is to ensure that no value error while entering level
            try:
                level = input("Please choose a level from 1 to 2 :")
                level_float = float(level)
            except ValueError:
                print("Enter a either 1 or 2!")
                continue
            else:
                if math.floor(level_float) != level_float:
                    print("Please enter an integer!")
                else:
                    level = int(level_float)
                    if level != 1 and level != 2:
                        print("Please enter either 1 or 2")
                        continue
                    else:
                        break  # we will break once the value have no error

        # for both computer 1 and 2, we first put it in a while loop
        # it is to ensure there must be someone wining before breaking the loop
        # We will always check victory first, follow with making the move by computer and player
        # before applying the move, we will also check move
        # it will always ask you to enter again if you enter something wrongly
        if level == 1:
            display_board(board)
            while True:  # this step ensure that need someone to win before going out
                Winner = check_victory(board, who_played)
                if Winner != 0:  # got someone win
                    if Winner == plt:
                        print("Winner is Player ", Winner)
                    elif Winner == cpt:
                        print("Winner is Computer Tom.")
                    break

                if turn == plt:  # no one win yet, and it is now player's turn
                    print("It is Player", plt, "'s turn.")
                    while True:  # ensure that user enter an integer!
                        try:
                            index = input("Which index do you want to push? : ")
                            index_float = float(index)
                        except ValueError:
                            print("Please enter an integer!")
                            continue
                        else:
                            if math.floor(index_float) != index_float:
                                print("Please enter an integer!")
                            else:
                                index = int(index_float)
                                break
                    push_from = input("Which direction would you like to push ? :")
                    if check_move(board, turn, index, push_from) == True:  # ensure a valid move
                        updated_list = apply_move(board, turn, index, push_from)
                        board = updated_list
                        display_board(board)
                        if turn == 1:
                            turn = 2
                        else:
                            turn = 1
                    else:
                        print("Invalid move.")
                        continue  # if invalid move, we will make the move until it is correct
                else:  # when turn==cpt
                    print("It is Computer Tom's turn.")
                    index, push = computer_move(board, 2, 1)
                    updated_list = apply_move(board, turn, index, push)
                    board = updated_list
                    display_board(board)
                    if turn == 1:  # we switch turn after move
                        turn = 2
                    else:
                        turn = 1


        elif level == 2:  # level 2
            display_board(board)
            while True:  # this step ensure got someone win before going out
                Winner = check_victory(board, who_played)
                if Winner != 0:  # got someone win
                    if Winner == plt:
                        print("Winner is Player ", Winner)
                    elif Winner == cpt:
                        print("Winner is Computer Xiao Ming.")
                    break
                if turn == plt:
                    print("It is Player", plt, "'s turn.")
                    while True:  # ensure that user enter an integer!
                        try:
                            index = input("Which index do you want to push? : ")
                            index_float = float(index)
                        except ValueError:
                            print("Please enter an integer!")
                            continue
                        else:
                            if math.floor(index_float) != index_float:
                                print("Please enter an integer!")
                            else:
                                index = int(index_float)
                                break

                    push_from = input("Which direction would you like to push ? :")
                    if check_move(board, turn, index, push_from) == True:
                        updated_list = apply_move(board, turn, index, push_from)
                        board = updated_list
                        display_board(board)
                        if turn == 1:
                            turn = 2
                        else:
                            turn = 1
                    else:
                        print("Invalid move.")
                        continue
                else:
                    print("It is Computer Xiao Ming's turn.")
                    index, push_from = computer_move(board, cpt, 2)
                    updated_list = apply_move(board, turn, index, push_from)
                    board = updated_list
                    display_board(board)
                    if turn == 1:
                        turn = 2
                    else:
                        turn = 1


    else:
        print("Please enter correctly xiexie")


if __name__ == "__main__":
    menu()
