# image_plot.py #  プログラム名

import os,glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def dataload(file_path,save_path):
    dirc = glob.glob(os.path.join(file_path,"*.npz"))
    for npz in dirc:
        makegif(npz,save_path)

def makegif(npz_path,save_path):
    ### npz用 ###
    with np.load(npz_path) as photos:# 写真データを読み込み
        
        x = photos['data']# 作成したnpzのキーの名前
        fig, ax = plt.subplots()
        picframe = x.shape[0]#　フレーム数 = 画像枚数
        # print(x.shape[0]) # フレーム数

        def drawframe(frame):
            plt.cla()
            plt.axis('off')
            ax.imshow(x[frame], cmap='gray')
            #ax.imshow(x[frame]) #RGBカラーの場合

        plt.axis('off') 
        ani = animation.FuncAnimation(fig,drawframe,frames =picframe, interval = 1)
        basename = (os.path.basename(npz_path)).split(".")[:1]
        ani.save("{}\\{}.gif".format(save_path,*basename), writer="imagemagick")
        print("saved : {}\\{}.gif".format(save_path,*basename))
        # plt.show() #表示したい場合はこちらを実行する
        
        plt.clf()
        plt.close()
        # メモリが解放される


def main():
    save_path = "saved_gif" # ""の中身を任意に変更可能
    file_path = r"ABOUT\test" # ""の中身を任意に変更可能
    if not os.path.isdir(save_path):
            os.makedirs(save_path)
    dataload(file_path,save_path)

if __name__ == '__main__':
    main()