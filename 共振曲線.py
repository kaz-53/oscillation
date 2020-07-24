import matplotlib.pyplot as plt

def forced_oscillation(g):  # 引数は減衰比
    x = []  # プロット用データ(x軸)
    y = []  # プロット用データ(y軸)
    for t in range(0, 40000):  # プロットデータ作成
        t *= 0.01
        w = t  # 入力の円振動数
        Xs = 1 / ((wn ** 2 - w ** 2) ** 2 + (2 * g * wn * w) ** 2) ** 0.5  # 振幅
        XsXst = Xs * wn ** 2  # 振幅倍率
        x.append(w / wn)  # x軸データの追加
        y.append(XsXst)  # y軸データの追加
    plt.plot(x, y, label="ζ = "+str(g))  # プロットする


m = 50  # 質量
k = 500000  # ばね定数
c = 100  # ダンパ
wn = (k / m)**0.5  # 固有振動数

forced_oscillation(0.05)  # 減衰比0.05の時のプロット作成
forced_oscillation(0.07)  # 減衰比0.07の時のプロット作成
forced_oscillation(0.1)  # 減衰比0.1の時のプロット作成
forced_oscillation(0.2)  # 減衰比0.2の時のプロット作成
forced_oscillation(0.5)  # 減衰比0.5の時のプロット作成

plt.legend(prop={"family":"MS Gothic"})  # 凡例表示
plt.title("共振曲線", fontname="MS Gothic")  # タイトル
plt.xlabel("ω/ωn", fontname="MS Gothic")  # x軸タイトル
plt.ylabel("Xs/Xst", fontname="MS Gothic")  # y軸タイトル
plt.grid()  # グリッド線表示
plt.savefig("共振曲線.png")  # 保存する
plt.show()  # プロット表示
