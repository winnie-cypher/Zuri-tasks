Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'winner'
>>> name
'winner'
>>> CONST = 'unchangeable'
>>> name_of_intern = 'winner'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> age = 18
>>> name = 'winner'
>>> is_legal = True
>>> type(age)
<class 'int'>
>>> type(name)
<class 'str'>
>>> type(is_legal)
<class 'bool'>
>>> my_money = 0.00
>>> type(money)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(money)
NameError: name 'money' is not defined
>>> type(my_money)
<class 'float'>
>>> name + age
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name + age
TypeError: can only concatenate str (not "int") to str
>>> credit_alert = 50.00
>>> total_money = 50.00 + 0.00
>>> total money
SyntaxError: invalid syntax
>>> total_money
50.0
>>> total_money = my_money + credit_alert
>>> total_money
50.0
>>> money_left_after_purchase = total_money - debit_alert
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    money_left_after_purchase = total_money - debit_alert
NameError: name 'debit_alert' is not defined
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 6&4
4
>>> 6%4
2
>>> type(&)
SyntaxError: invalid syntax
>>> numbers = [1,4,6,3,7,9,0,3]
>>> for nums in numbers:
	if nums%2 == 0:
		print("{} is even".format(nums))

		
4 is even
6 is even
0 is even
>>> name
'winner'
>>> type(name)
<class 'str'>
>>> message = 'good morning'
>>> my_name = 'winner'
>>> print('welcome{}'.format(my_name))
welcomewinner
>>> print('welcome {}'.format(my_name))
welcome winner
>>> my_name[4]
'e'
 number = input("please enter a number")
print('number')





