N = int(input())
navi = list(input().split())

navi_dic = dict()
navi_dic['L'] = [0, -1]
navi_dic['R'] = [0, +1]
navi_dic['U'] = [-1, 0]
navi_dic['D'] = [+1, 0]

pos = [0, 0]
for i in navi:
    moved_x = pos[0] + navi_dic[i][0]
    moved_y = pos[1] + navi_dic[i][1]
    if moved_x < N and moved_x >= 0 and moved_y < N and moved_y >= 0:
        pos = [moved_x, moved_y]
print(pos[0]+1, pos[1]+1)
