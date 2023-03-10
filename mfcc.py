import os
import numpy as np
import pandas as pd
import librosa

X_data = []  # 特徴行列
y_data = []  # クラスラベルデータ
speakers_number = 7

for speaker_num in range(1, speakers_number + 1):  # 声優No.1~100
    # parallel100の音声データが入っているディレクトリ名
    dir_name = f'VoiceSamples/{str(speaker_num).zfill(3)}'
    for file_name in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file_name)  # 音声ファイルへのパス
        y, sr = librosa.load(file_path)  # 音声ファイルを読み込む
        mfcc = librosa.feature.mfcc(y, sr)  # MFCC
        mfcc = np.average(mfcc, axis=1)  # 時間平均を取る
        mfcc = mfcc.flatten()
        mfcc = mfcc.tolist()
        mfcc = mfcc[1:13]  # 低次の係数を取り出す（12次まで取り出すことが多い）
        X_data.append(mfcc)
        y_data.append(speaker_num)

X = pd.DataFrame(X_data, columns=[f'mfcc_{n}' for n in range(1, 13)])
y = pd.DataFrame({'target': y_data})

df = pd.concat([X, y], axis=1)
df.to_csv('mfcc.csv', index=False)  # csvで保存
df.head()