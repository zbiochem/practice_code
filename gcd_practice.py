# 変数入力部分
a_origin = input("一つ目の整数を入力して下さい: ")
b_origin = input("二つ目の整数を入力してください: ")
a = int(a_origin)
b = int(b_origin)

# a >= bになるように変数の値をスワップ
if a < b:
    a, b = b, a

# ユークリッドの互除法
while True:
    a %= b
    if a == 0:
        gcd = b
        break
    else:
        b %= a
        if b == 0:
            gcd = a
            break

# 出力部分
if gcd == 1:
    print (a_origin + "と" + b_origin + "は互いに素")
else:
    print (a_origin + "と" + b_origin + "の最大公約数は" + str(gcd))