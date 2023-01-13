# -*- coding: utf-8 -*-
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

sourceFolder = "Source"
targetFolder = "VoiceSample"

folders = os.listdir(sourceFolder)
for folder in folders:
    srcFolderPath = os.path.join(sourceFolder, folder)
    tarFolderPath = os.path.join(targetFolder, folder)
    files = os.listdir(srcFolderPath)

    for f in files:
        path = os.path.join(srcFolderPath, f)
        fileName = f[:len(f) - 4]
        print(path)
        if os.path.isdir(path):
            continue
        # wavファイルのデータ取得
        sound = AudioSegment.from_file(path, format="wav")

        # wavデータの分割（無音部分で区切る）
        chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40, keep_silence=500)

        if(not os.path.exists(tarFolderPath)):
            os.mkdir(tarFolderPath)

        # 分割したデータ毎にファイルに出力
        for i, chunk in enumerate(chunks):
            chunk.export(tarFolderPath + "/" + fileName + "-" + str(i) +".wav", format="wav")
        
        os.remove(path)