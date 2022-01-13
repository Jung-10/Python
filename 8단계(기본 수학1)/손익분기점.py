fixed_cost, variable_expenses, total_revenue = map(int, input().split())

if variable_expenses >= total_revenue :
    print(-1)
else :
    print(int(fixed_cost / (total_revenue - variable_expenses) + 1))
