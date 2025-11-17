#sales=[[100,200],[300,400]]
# # 1
# def add_sale(sales,day,amount):
#     sales.append([day,amount])
#     return sales
# # print(add_sale(sales,1000,100))

# 2
# sales=[[100,200],[300,400]]
# def get_total_sales(sales,day):
#     x=0
#     for i in sales[day]:
#         x+=i
#     return x 
# print(get_total_sales(sales,int(input())))

# 3 
# sales=[[100,200],[300,400]]
# day=[0,2]
# def find_best_sales_day(sales,day):
#     mx=[]
#     for i in range(len(day)):
#         mx.append(sum(sales[day[i]]))
#     return(max(mx))
# print(find_best_sales_day(sales,day))


# 4
# sales=[[100,200],[300,400]]
# def get_unique_sale_amounts(sales,day):
#     x=set()
#     for i in sales[day]:
#         x.add(i)
#     return list(x)
# print(get_unique_sale_amounts(sales,1))


# 5
# sales=[[100,200],[300,400]]
# def find_sales_target(sales,day,target_amount):
#     day_sales = sorted(sales[day])
#     left, right = 0, len(day_sales) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if day_sales[mid] == target_amount:
#             return True
#         elif day_sales[mid] < target_amount:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return False
# print(find_sales_target(sales,0,100))