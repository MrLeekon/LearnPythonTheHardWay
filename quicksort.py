# -*- coding: utf-8 -*-
from sys import argv

def quicksort(array):
    if len(array)<2:
	   return array # 基线条件：为空或只包含一个元素的数据是『有序』的
    else:
       pivot = array[0] # 递归条件（基准）
       less= [i for i in array[1:] if i <= pivot]
       greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

def main():
	array = []
	for i in argv[1:]:
		array.append(int(i))
	print quicksort(array)

if __name__ == "__main__":
	main()

