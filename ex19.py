# -*- coding: utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a balket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 5)

print "And we can combine the two, varibles and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 尝试过使用*表达式解压切片，失败 星号表达式不能单独使用
amount_of_cheese_and_crackers = [10, 100]
cheese_and_crackers(*amount_of_cheese_and_crackers)
cheese_and_crackers(int(raw_input("总共有多少个汉堡？",)), int(raw_input("总共有多少片薄饼")))

