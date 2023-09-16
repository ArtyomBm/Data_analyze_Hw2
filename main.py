import numpy as np
import matplotlib.pyplot as plt

profit = []
quantity = []
region = []
segment = []
discount = []
Check = True
with open('data.csv') as f:
    for i in f:
        if Check:
            Check = False
            continue
        profit.append(float(i.split(',')[-1]))
        quantity.append(int(i.split(',')[-3]))
        region.append(i.split(',')[12])
        segment.append(i.split(',')[7])
        discount.append(float(i.split(',')[-2]))
print('Коэффициент корреляции Пирсона между доходом и числом проданного товара = ', np.corrcoef(profit, quantity)[0, 1])
print('Коэффициент корреляции Пирсона между доходом и скидкой = ', np.corrcoef(profit, discount)[0, 1])

segments = segment
segments.sort()
profit_each_segment = dict()
for i in segments:
    profit_each_segment[i] = []
    for j in range(len(segment)):
        if i == segment[j]:
            profit_each_segment[i].append(profit[j])
sums = []
for i in profit_each_segment:
    sums.append(sum(profit_each_segment[i]))
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(profit_each_segment.keys(), sums)
plt.title('Доход на каждый сегмент')

unique_regions = region
unique_regions.sort()
profit_each_region = dict()
for i in unique_regions:
    profit_each_region[i] = []
    for j in range(len(region)):
        if i == region[j]:
            profit_each_region[i].append(profit[j])
sums = []
for i in profit_each_region:
    sums.append(sum(profit_each_region[i]))
plt.subplot(132)
plt.bar(profit_each_region.keys(), sums)
plt.title('Доход на каждый регион')

each_quantity = quantity
each_quantity.sort()
profit_each_quantity = dict()
for i in each_quantity:
    profit_each_quantity[i] = []
    for j in range(len(quantity)):
        if i == quantity[j]:
            profit_each_quantity[i].append(profit[j])
sums = []
for i in profit_each_quantity:
    sums.append(sum(profit_each_quantity[i]))
plt.subplot(133)
plt.plot(profit_each_quantity.keys(), sums)
plt.title('Доход на количество проданного товара')
plt.show()