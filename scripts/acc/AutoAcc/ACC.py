#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random

# 伴奏模板文件所在文件夹
dir = ".//AutoAcc//acc"
if not os.path.exists(dir):
    dir = ".//acc"

# 伴奏模板文件名
file_list = [ "acc00101.acc", "acc00102.acc", "acc00103.acc", "acc00104.acc", "acc00105.acc", 
                "acc00106.acc", "acc00107.acc", "acc00108.acc", "acc00109.acc", "acc00110.acc",
                "acc00111.acc", "acc00112.acc", "acc00114.acc", "acc00115.acc", "acc00116.acc", 
                "acc00117.acc", "acc00118.acc", "acc00119.acc", "acc00120.acc", "acc00121.acc", 
                "acc00122.acc", "acc00123.acc", "acc00124.acc", "acc00125.acc", "acc00126.acc", 
                "acc00127.acc", "acc00128.acc", "acc00129.acc", "acc00130.acc", "acc00131.acc", 
                "acc00132.acc", "acc00133.acc", "acc00134.acc", "acc00136.acc", "acc00137.acc", 
                "acc00138.acc", "acc00139.acc", "acc00143.acc", "acc00144.acc", "acc00148.acc", 
                "acc00150.acc", "acc00157.acc", "acc00159.acc", "acc00164.acc", "acc00167.acc", 
                "acc00168.acc", "acc00171.acc", "acc00173.acc", "acc00174.acc", "acc00175.acc", 
                "acc00181.acc", "acc00186.acc", "acc00188.acc", "acc00189.acc", "acc00194.acc", 
                "acc00196.acc", "acc00198.acc", "acc00205.acc", "acc00212.acc", "acc00214.acc", 
                "acc00215.acc", "acc00229.acc", "acc00234.acc", "acc00235.acc", "acc00249.acc",
                "acc00250.acc", "acc00255.acc", "acc00260.acc", "acc00287.acc", "acc00288.acc", 
                "acc00289.acc", "acc00290.acc", "acc00291.acc", "acc00292.acc", "acc00293.acc",
                "acc00294.acc", "acc00295.acc", "acc00296.acc", "acc00299.acc", "acc00302.acc", 
                "acc01261.acc", "acc01262.acc", "acc01263.acc", "acc01264.acc", "acc01265.acc", 
                "acc01153.acc", "acc01266.acc", "acc01267.acc", "acc01268.acc", "acc01270.acc", 
                "acc01271.acc", "acc01273.acc", "acc01275.acc", "acc01279.acc", "acc01282.acc", 
                "acc00151.acc", "acc00152.acc", "acc00160.acc", "acc00178.acc", "acc00182.acc", 

            ]

# 情感个数、曲风个数
EMOTION_COUNT = 2         # 高兴  悲伤
GENRE_COUNT = 4             # 流行 摇滚  民谣  电子

# 模板序号 与 情感曲风 对应表
TemplateIndex2EmotionGenre = [ #  """高兴"""              """悲伤"""
                                        (  0,  1,   9, 10, 13, 18, 19, 24, 29, 33, 34, 41, 45, 49, 59, 60, 81, 82, 83, 84, 88, 97, 98, ), ( 2,  7,  8, 13, 16, 17, 19, 25, 26, 27, 34, 36, 37, 39, 53, 54, 61, 62, 77, 86, 87, 91, 95, 96, 99 ), # 流行
                                        (12, 18, 20, 23, 28, 31, 35, 38, 42, 58, 60, 68, 69, 70, 72, 76, 82, 89, ),     ( 8, 11, 23, 25, 31, 46, 50, 55, 56, 57, 64, 66, 73, 75, 80, 90, ),   #摇滚   
                                        ( 9, 13, 24, 34, 40, 41, 43, 44, 51, 52, 59, 67, 71, 74, 78, 79,  93,     ),      (13, 22, 25, 26, 34, 37, 47, 48, 53, 54, 61, 62, 63, 65, 67, 77, 85, 92, ),    #民谣
                                        ( 3,  4,  5, 15, 18, 21, 30, 32, ),                                                           (4, 5, 6, 14, 21, 30, ),                     #电子
                                    ]  

# 曲速范围 与 情感曲风 对应表
BpmFloat2EmotionGenre = [ #  """高兴"""              """悲伤"""
                                        (90, 140),             (60, 100),  # 流行
                                        (105, 140),            (70, 100),  #摇滚   
                                        (95, 140),             (70, 100),  #民谣
                                        (110, 170),             (80, 110),  #电子
                                        ]

# 模板个数
TEMPLATE_COUNT = len(file_list)              # 100个
            
# 完整路径
ACC_FILE_LIST = [ os.path.join(dir, x) for x in file_list]

""" 根据emotion和genre，返回随机的template """
def getTemplateIndexByEmotionGenre(emotion, genre): 
    try:
        candidate_list = TemplateIndex2EmotionGenre[emotion + EMOTION_COUNT*genre]
    except:
        print "Error: list out of range by emotion and genre", emotion, genre, emotion + EMOTION_COUNT*genre, len(TemplateIndex2EmotionGenre)
        candidate_list = range(TEMPLATE_COUNT)
    return random.choice(candidate_list)
    
""" 根据emotion和genre，返回随机的曲速 """
def getBpmFloatByEmotionGenre(emotion, genre):
    bpm_min,  bpm_max = BpmFloat2EmotionGenre[emotion + EMOTION_COUNT*genre]
    return random.randint(bpm_min,  bpm_max)


if __name__ == "__main__": 
    print ACC_FILE_LIST
    
