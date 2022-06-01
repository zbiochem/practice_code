# ゲーム盤の設定
table = [["0", "0" ,"0"],
        ["0", "0" ,"0"],
        ["0", "0" ,"0"]]
# ゲーム版の表示関数,1行ずつ取り出すことで3*3を表現している。
def output_():
    for i in range(3):
        print(table[i])
# 丸を打つ関数, 空の場所にのみ入れるようにする。
def input_maru():
    print ("maruのターン:")
    while True:
        i = int(input("上から何段目？:")) - 1
        j = int(input("左から何行目？:")) - 1
        if table[i][j] == "0":
            table[i][j] = "m"
            break
        else:
            print("error!")
# バツを打つ関数, 丸と同じ
def input_batu():
    print("batsuのターン:")
    while True:
        i = int(input("上から何段目？:")) - 1
        j = int(input("左から何行目？:")) - 1
        if table[i][j] == "0":
            table[i][j] = "b"
            break
        else:
            print("error!")
# 勝利判定関数
def ruler_():
    if (table[0][0] == table[1][1] == table[2][2] != "0") or (table[0][2] == table[1][1] == table[2][0] != "0"):
        return table[0][0]
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != "0":
            return table[i][0]
            break
        if table[0][i] == table[1][i] == table[2][i] != "0":
            return table[0][i]
            break
# 全てのマスが埋まった時の判定用
# 外の変数でterminaterをグローバル変数に変えている。中の変数は2回目以降の初期化用
terminter = 1
def terminate():
    terminater = 1
    for i in range(3):
        for j in range(3):
            if table[i][j] == "0":
                terminater *= 0
    return terminater

# ゲーム開始   
output_()
# ゲーム中処理, 勝敗決定時と盤面が埋まった時にループ処理を抜ける
while True:
    input_maru()
    output_()
    if ruler_() == "m" or terminate() == 1:
        break
    input_batu()
    output_()
    if ruler_() == "b":
        break
# 結果表示
if ruler_() != None:
    print ("勝者:" + str(ruler_()))
else:
    print ("draw!")