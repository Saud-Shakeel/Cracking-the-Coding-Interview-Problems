def fibonacci_series(n):
    series_list=[]
    if n == 0:
        return 0
    elif n == 1:
        return [0,1]
    else:
        series_list = fibonacci_series(n-1)
        series_list.append(series_list[-1] + series_list[-2])
        return series_list

print(fibonacci_series(10))
