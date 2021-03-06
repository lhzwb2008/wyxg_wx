#!/usr/bin/python
# -*- coding: utf-8 -*-
  
""" 关于section的信息 """

# 歌曲结构section的序号
""" 
# 空白、前奏、主歌1-1、主歌1-2、桥段1、副歌1-1、副歌1-2 
# 间奏1、间奏2、主歌2-1、主歌2-2、副歌2-1、副歌2-2、尾奏
# 主歌1-3、主歌2-3、主歌3-1、主歌3-2、主歌3-3、副歌3-1、副歌3-2
# 桥段2
"""
sec_blank, sec_intro, sec_a11, sec_a12, sec_bridge1, sec_b11, sec_b12, \
 sec_mid1, sec_mid2, sec_a21, sec_a22, sec_b21, sec_b22, sec_end, \
 sec_a13, sec_a23, sec_a31, sec_a32, sec_a33, sec_b31, sec_b32, \
 sec_bridge2 = \
        0, 1, 2, 3, 4, 5, 6, \
        7, 8, 9, 10, 11, 12, 13, \
        14, 15, 16, 17, 18, 19, 20, \
        21
 
# 结构类型个数
COUNT_SEC_TYPE = 21
 
# 表明如果没有符合section时，找哪个section, (0表示随机) 
CANDIDATE_SECTION_MATCHING_LIST = ([0, 2, ], [1, 7, ], [2, 1, ], [3, 2, 1], [4, 2, 1], [5, 2, 4], [6, 5, 2, 4], 
                        [7, 1, 2, 4, 5], [8, 7, 1, 2, 4, 5],
                        [9, 2, 3], [10, 9, 3, 2], [11, 5, 6], [12, 11, 6, 5], [13, 1, 7, 8], [14, 2, 3], [15, 14, 2, 3], 
                        [16, 9, 2, 3], [17, 10, 16, 3, 2], [18, 15, 13, 2, 3], [19, 11, 5, 6], [20, 12, 6, 5], [21, 4, 2, 1], 
                        [22, 3, 2], [23, 22, 10, 9, 3, 2], [24, 32, 17, 16, 3, 2], [25, 21, 4, 2, 1], )


# section 是否需要歌词
def section_has_lyric(sec_index):
    return sec_index in (sec_a11, sec_a12, sec_bridge1, sec_b11, sec_b12, \
                                 sec_a21, sec_a22, sec_b21, sec_b22, 
                                 sec_a13, sec_a23, sec_a31, sec_a32, sec_a33, sec_b31, sec_b32, \
                                 sec_bridge2)
          
 
if __name__ == "__main__": 
    pass
