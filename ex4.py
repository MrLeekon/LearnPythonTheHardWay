# -*- coding: utf-8 -*-  
# 有100辆车
cars = 100
# 每辆车有四个座位
space_in_a_car = 4.0
# 有司机30人
drivers = 30
# 总共有90个乘客
passengers = 90
# 没人开的车辆数
cars_not_driven = cars - drivers
# 开了的车辆数
cars_driven = drivers
# 总共能载的人数
carpool_capacity = cars_driven * space_in_a_car
# 平均一个乘客开的车辆数
average_passengers_per_car = passengers / cars_driven

# 有多少辆车可以开
print "There are", cars, "cars available."
# 只有为数不多的老司机
print "There are only", drivers, "drivers available."
# 那就有一些剩下的没用的垃圾车
print "There will be:|", cars_not_driven, "empty cars today."
# 这些司机总共可以载一些人
print "We can transport", carpool_capacity, "people today."
# 我们今天呀，有一些乘客要乘车
print "We have", passengers, "to carpool today."
# 我们平均吧不知道多少位乘客放进一辆车
print "We need to put about", average_passengers_per_car, "in each car."
