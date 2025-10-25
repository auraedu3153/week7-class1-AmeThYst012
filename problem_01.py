# 요구사항은 https://www.acmicpc.net/problem/1018을 확인하세요
def min_count_of_squares(board: list[list[str]]) -> int:
        return min([min([sum([(i+j+(a[start+i][end+j]=='W'))%2==0 for i in range(8) for j in range(8)]), 64-sum([(i+j+(a[start+i][end+j]=='W'))%2==0 for i in range(8) for j in range(8)])]) for start in range(len(a)-7) for end in range(len(a[0])-7)])
