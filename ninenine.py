#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 99乘法表～～～
i = 1
while i < 10:
  j=1
  while j <= i:
  	count = i*j
  	print j,'x',i,'=',count,'  ',
  	if(j != i):
  	  j+=1
  	else:
  	  print '\n'
  	  break

  i+=1


width = int(raw_input('输入对角线长度： '))
for row in range(width + 1):
    for col in range(width + 1):
        if ((abs(row - width/2) + abs(col - width/2)) == width/2):
            print "*",
        else:
            print " ",
    print " "



  	