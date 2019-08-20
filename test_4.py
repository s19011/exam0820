# codeing=utf-8
import random
import tkinter as tk
import tkinter.messagebox as tkmsg


#ボタンをクリックしたとき
def ButtonClick():

    #入力欄の内容を取得
    b = entry_01.get()

    #正しい入力か判定する
    input_ok = False
    if len(b) != 4:
        tkmsg.showerror("エラー", "4桁の数字を入れてね")
    else:
        input_ok = True
        for i in range(4):
            if(b[i]<"0") or (b[i]>"9"):
                    input_ok = False
                    tkmsg.showerror("エラー", "数字じゃないよ")
                    break

    #ヒットとブローを判定する①②
    if input_ok == True:
        #①ヒット
        hit = 0

        for i in range(4):
            if a[i] == int(b[i]):
                hit = hit+1
        #②ブロー
        blow = 0
        for j in range(4):
            for i in range(4):
                if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] !=int(b[j])):
                    blow = blow+1
                    break

        #ヒットが4なら終了
        if hit==4:
            #メッセージをだしてウィンドウを閉じる
            tkmsg.showinfo("アタリ", "アタリです！")
            root.destroy()
        else:
            #ヒット数とブロー数を表示
            rireki_01.insert(tk.END, b + " / H:" + str(hit) + ", B:" + str(blow) + "\n")


#4桁のランダムな数字をつくる
a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]

#ウィンドウを作る
root = tk.Tk()
root.geometry("600x400")
root.title("数当てゲーム")

#履歴のテキストボックスを作る
rireki_01 = tk.Text(root, font=("Helvetica",14))
rireki_01.place(x=400, y=0, width=200, height=400)

#ラベルを作る
label_01 = tk.Label(root, text="4桁の数字をいれてね", font=("Helvetica",14))
label_01.place(x=20, y=20)

#入力欄を作る
entry_01 = tk.Entry(width = 6, font=("Helvetica",28))
entry_01.place(x=20, y=45)

#ボタンを作る
button_01 = tk.Button(root, text="確定", font=("Helvetica",20), command=ButtonClick)
button_01.place(x=170, y=54)

root.mainloop()
