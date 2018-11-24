import random, string

# 生成14位码
def coupon_creator(digit):
    coupon = ''
    for word in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon

# 生成200个优惠码
def two_hundred_coupons():
    data = ''
    digit = 14  #十四位优惠券码
    for count in range(200):
        count += 1
        data += 'coupon num.' + str(count) + '  ' + coupon_creator(digit) + '\n'

    return data

# 存储到文件中
coupondata = open('coupondata.txt', 'w')
coupondata.write(two_hundred_coupons())
coupondata.close()




