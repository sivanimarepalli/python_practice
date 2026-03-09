# .+ => to print plus before a value
# .^ => to align value at center
# .< => to align value at left
# .> => to align value at right
# ., => to separate a 1000's value with a comma

price1=3.14159
price2=-987.65
price3=12.34
print(f"price 1 is: {price1:^+,.2f}/-")# : after price1 is a format specifier and .2f is for decimal precesion
print(f"price 2 is: {price2}/-")
print(f"price 3 is: {price3}/-")