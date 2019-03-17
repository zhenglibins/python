# -*- coding: utf-8 -*-
class Student:
	'所有学生的基类'
	cou = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Student.cou += 1

	def displayCount(self):
		print("Total Student %d" % self.cou)

	def displayInfo(self):
		print("Name : ", self.name,  ", age: ", self.age)

	def nullFunc(self):
		print("1")

def nullFunc():
    print("123")
zhang = Student("zhangsan",27);
zhang.displayCount()
li = Student("lisi",29);
li.displayCount();
zhang.nullFunc()
nullFunc()
