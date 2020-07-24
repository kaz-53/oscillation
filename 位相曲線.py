import math
import matplotlib.pyplot as plt

def phase_oscillation(g):  # 引数は減衰比
    x = []  # プロット用データ(x軸)
    y = []  # プロット用データ(y軸)
    for t in range(0, 40000):  # プロットデータ作成
        t *= 0.01
        w = t  # 入力の円振動数
        try:
            fi = math.atan(-2 * g * wn * w / (wn ** 2 - w ** 2)) / math.pi * 180  # 位相角φの値
        except:
            None
        x.append(w / wn)  # x軸データの追加    振動数比(円振動数/固有振動数)
        if w / wn > 1:  # 振動数比が１より大きいときの位相角の値
            y.append(fi - 180)  # y軸データの追加
        else:
            y.append(fi)  # y軸データの追加
    plt.plot(x, y, label="ζ = "+str(g))


m = 50  # 質量
k = 500000  # ばね定数
c = 100  # ダンパ
wn = (k / m) ** 0.5  # 固有振動数

phase_oscillation(0.05)  # 減衰比0.05の時のプロット作成
phase_oscillation(0.07)  # 減衰比0.07の時のプロット作成
phase_oscillation(0.10)  # 減衰比0.10の時のプロット作成
phase_oscillation(0.20)  # 減衰比0.20の時のプロット作成
phase_oscillation(0.50)  # 減衰比0.50の時のプロット作成

plt.legend(prop={"family":"MS Gothic"})  # 凡例表示
plt.title("位相曲線", fontname="MS Gothic")  # タイトル
plt.xlabel("ω/ωn", fontname="MS Gothic")  # x軸タイトル
plt.ylabel("φ[°]", fontname="MS Gothic")  # y軸タイトル
plt.grid()  # グリッド線表示
plt.savefig("位相曲線.png")  # 保存する
plt.show()  # プロット表示
