# 例5-7：lambda 表达式
fruits = ['strawberry','apple','banana','cherry','fig']
new_fruit = sorted(fruits,key = lambda word:word[::-1])
print(new_fruit)    # ['banana', 'apple', 'fig', 'strawberry', 'cherry']