import queue
n_rows, n_cols = 0, 0
visited = []
def search(imageArray, start_row, start_col, end_row, end_col):
    #find the base and height of my array
    global n_rows 
    n_rows = len(imageArray)
    global n_cols
    n_cols = len(imageArray[0])
    #initailize the visited array, make it all 1e9, this array also doubles as a distance array
    global visited
    visited = [[1 for x in range(n_cols)] for y in range(n_rows)]
    #start my dfs
    visited[start_row][start_col] = 0
    return bfs(start_row, start_col, imageArray, end_row, end_col)
#   print("{}{}".format(len(visited) , len(visited[0])))
#     for i in visited:
#         print()
#         for y in i:
#             print(y, end="")
def bfs(start_row, start_col, imageArray, end_row, end_col):#'1' means white, '0' means black
    d_row = [-1, 0, 1, 0]
    d_col = [0, -1, 0, 1]
    dis = [[1e9 for x in range(n_cols)] for y in range(n_rows)]
    pre = [[-1 for x in range(n_cols)] for y in range(n_rows)]
    dis[start_row][start_col] = 0
    q = []
    q.append((start_row,start_col))
    while(len(q) > 0):
        row, col = q[0][0], q[0][1]
        q.pop(0)
        for i in range(4):
            new_row = row + d_row[i]
            new_col = col + d_col[i]
            #if(new_x >= 0 and new_x < n and new_y >= 0 and new_y < m and imageArray[new_x][new_y] == 1 and dis[new_x][new_y] > dis[x][y]+1 and check(new_x, new_y, imageArray)):
            if(new_row >= 0 and new_row < n_rows and new_col >= 0 and new_col < n_cols and imageArray[new_row][new_col] == 1 and dis[new_row][new_col] > dis[row][col]+1) :
                dis[new_row][new_col] = dis[row][col] + 1
                pre[new_row][new_col] = i
                q.append((new_row, new_col))
    
    path_len = dis[end_row][end_col]
    sequence = ""
    row = end_row
    col = end_col
    while(row!= start_row or col!= start_col):
        if(pre[row][col] == 0):
#             print("HERE")
            sequence += "D"
            row = row + 1
        elif(pre[row][col] == 1):
            sequence += "L"
            col = col + 1
        elif(pre[row][col] == 2):
            sequence += "U"
            row = row - 1
        elif(pre[row][col] == 3):
            sequence += "R"
            col = col - 1 
        else:
            print("Impossible")
            exit()
    
#     print(sequence)
#     print(startX)
#     print(startY)
#     print(endX)
#     print(endY)
    return sequence[::-1]
            
def check(x, y, imageArray):
    n = len(imageArray)
    m = len(imageArray[0])
    for i in range (max(0, x-2), min(n, x+2)):
        for j in range(max(0, y-2), min(m, y+2)):
            if(imageArray[i][j] == 0):
                return False
    return True
