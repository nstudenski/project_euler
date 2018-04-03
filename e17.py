l0 = 0
l1 = len('one')
l2 = len('two')
l3 = len('three')
l4 = len('four')
l5 = len('five')
l6 = len('six')
l7 = len('seven')
l8 = len('eight')
l9 = len('nine')

singles = [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9]
hundreds = [l1,l2,l3,l4,l5,l6,l7,l8,l9]

l10 = len('ten')
l11 = len('eleven')
l12 = len('twelve')
l13 = len('thirteen')
l14 = len('fourteen')
l15 = len('fifteen')
l16 = len('sixteen')
l17 = len('seventeen')
l18 = len('eighteen')
l19 = len('nineteen')

teens = [l10,l11,l12,l13,l14,l15,l16,l17,l18,l19]

l20 = len('twenty')
l30 = len('thirty')
l40 = len('forty')
l50 = len('fifty')
l60 = len('sixty')
l70 = len('seventy')
l80 = len('eighty')
l90 = len('ninety')

tens = [l20,l30,l40,l50,l60,l70,l80,l90]

lx00 = len('hundred')

nd = 3

thous = len('onethousand')

nums = []
#1-9
for single in singles:
    nums.append(single)
#10-19
for teen in teens:
    nums.append(teen)
#20-99
for ten in tens:
    for one in singles:
        nums.append(ten+one)
#100 - 999
for h in hundreds:
    #x01-x09
    nums.append(h+lx00)
    for one in hundreds:
        nums.append(h+lx00+nd+one)
    #x10-x19
    for teen in teens:
        nums.append(h+lx00+nd+teen)
    for t in tens:
        for i in singles:
            nums.append(h+lx00+nd+t+i)
nums.append(thous)

print(sum(nums))
