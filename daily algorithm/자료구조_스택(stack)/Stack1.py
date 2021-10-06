def solution(board, moves):
    stacklist = [] # list로 스택을 구현
    answer = 0

    for i in moves:
        for j in range(len(board)): # 인형이 몇개가 쌓여 있는지 모르기 때문에 가장 위에부터 탐색
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]: # 가장 위에 있는 요소 2개가 같다면 pop을 이용해 삭제
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer