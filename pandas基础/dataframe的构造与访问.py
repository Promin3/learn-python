import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)  # 输出对齐方向设置
scores = [['男', 108, 115, 97], ['女', 115, 87, 105], ['女', 100, 60, 130], ['男', 112, 80, 50]]
names = ['promin', 'jackey', 'mikey', 'jenny']
coures = ['gendar', 'chinese', 'math', 'english']
df = pd.DataFrame(data=scores, index=names, columns=coures)
print(df)

# DataFrame的切片
# iloc[行选择器,列选择器] 用下标做切片
# loc[行选择器,列选择器]  用标签做切片
# DataFrame的切片是视图

df2 = df.iloc[0:2]
df3 = df.loc['promin': 'jenny': 2]
