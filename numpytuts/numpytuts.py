[[123,12,123,12,33],[],[]]

import numpy
n = numpy.arange(27)
n

n = numpy.arange(27).reshape(3,9)
n

n = numpy.arange(27).reshape(3,3,3)
n

import numpy
m = numpy.asarray([[123,12,123,12,33],[],[]])
m
# array([list([123, 12, 123, 12, 33]), list([]), list([])], dtype=object)

print(m)
# [list([123, 12, 123, 12, 33]) list([]) list([])]

type(m) # numpy.ndarray

im_g = cv2.imread("smallgray.png", 0) # 0 is greyscale and 1 is BGR (RGB)
im_g
"""
array([[187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182]], dtype=uint8)
"""
# create image from array
cv2.imwrite("newsmallimage.png", im_g)

# indexing and slicing
im_g[0:2,2:4]
"""
array([[104, 121],
       [255, 255]], dtype=uint8)
"""

im_g[1,4]
"""
147
"""

# iterating
for i in im_g:
    print(i)
"""
[187 158 104 121 143]
[198 125 255 255 147]
[209 134 255  97 182]
"""

# iterate through columns
for i in im_g.T:
    print(i)
"""
[187 198 209]
[158 125 134]
[104 255 255]
[121 255  97]
[143 147 182]
"""

# iterate by one by one
for i in im_g.flat:
    print(i)
"""
187
158
104
121
143
198
125
255
255
147
209
134
255
97
182
"""

# Horizontal STACKING
imhs = numpy.hstack((im_g,im_g,im_g))
print(imhs)
"""
[[187 158 104 121 143 187 158 104 121 143 187 158 104 121 143]
 [198 125 255 255 147 198 125 255 255 147 198 125 255 255 147]
 [209 134 255  97 182 209 134 255  97 182 209 134 255  97 182]]
"""

# Vertical STACKING
imvs = numpy.vstack((im_g,im_g,im_g))
print(imvs)
"""
[[187 158 104 121 143]
 [198 125 255 255 147]
 [209 134 255  97 182]
 [187 158 104 121 143]
 [198 125 255 255 147]
 [209 134 255  97 182]
 [187 158 104 121 143]
 [198 125 255 255 147]
 [209 134 255  97 182]]
"""

# Horizontal SPLITTING
imhs = numpy.hstack((im_g,im_g,im_g))
imhsp = numpy.hsplit(imhs,5)
print(imhsp)
"""
[array([[187, 158, 104],
       [198, 125, 255],
       [209, 134, 255]], dtype=uint8), array([[121, 143, 187],
       [255, 147, 198],
       [ 97, 182, 209]], dtype=uint8), array([[158, 104, 121],
       [125, 255, 255],
       [134, 255,  97]], dtype=uint8), array([[143, 187, 158],
       [147, 198, 125],
       [182, 209, 134]], dtype=uint8), array([[104, 121, 143],
       [255, 255, 147],
       [255,  97, 182]], dtype=uint8)]
"""

# Vertical SPLITTING
imhs = numpy.hstack((im_g,im_g,im_g))
imvsp = numpy.hsplit(imvs,3)
print(imvsp)
"""
[array([[187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182]], dtype=uint8), array([[187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182]], dtype=uint8), array([[187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182]], dtype=uint8)]
"""