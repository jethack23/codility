def solution(n):
    while 0 == n % 2:
        n //= 2
    rst = 0
    while n > 1:
        temp_rst = 0
        n //= 2
        while 0 == n % 2:
            n //= 2
            temp_rst += 1
        rst = max(rst, temp_rst)
    return rst
