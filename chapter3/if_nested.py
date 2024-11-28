low_level = 0
has_house = True
has_car = False

if not low_level :
    # 考虑其他
    if has_house and has_car :
        print("非你莫属")
    elif has_house or has_car :
        print("非常满意")
    else:
        print("满意")
else:
    print("你不符合条件")