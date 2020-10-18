import random as r
def main():
    fb = open("C:/Users/admin/Desktop/data.csv", 'r')
    ss = fb.readlines()
    loc = []
    date = []
    vis = flag = True
    for s in ss:
        if vis == True:
            vis = False
            continue
        i = 0
        for j in range(12):
            temp = ''
            while s[i] != ',':
                temp += s[i]
                i += 1
                if (i >= len(s)): break
            i += 1
            if flag == True: loc.append(temp.replace('\n', ''))
            else: date.append(temp.replace('\n', ''))
        flag = False
    fb.close()
    print("--------地点--------")
    for i in range(12): print("%d.%s"%(i, loc[i]), end='\t')
    print("\n--------时间--------")
    for i in range(12): print("%d.%s"%(i, date[i]), end='\t')
    a = r.randint(0, 11)
    b = r.randint(0, 11)
    print("\n随机分配的地点与事件为%d,%d:%s%s"%(a, b, loc[a], date[b]))
    n=int(input("Lvzhou地址与事件："))
    m=int(input())
    print("%s%s"%(loc[n], date[m]), end='')
    if n == a and m == b:
        print("正确\nLvzhou获得200MB")
    else:
        print("不正确")
        n = int(input("请输入地址与事件："))
        m = int(input())
        print("%s%s" % (loc[n], date[m]), end='')
        if n == a and m == b:
            print("正确\n")
            print("Lvzhou获得100MB")
            print("用户1获得100MB")
        else:
            print("不正确")
            n = int(input("请输入地址与事件："))
            m = int(input())
            print("%s%s" % (loc[n], date[m]), end='')
            if n == a and m == b:
                print("正确")
                print("Lvzhou获得100MB")
                print("用户1获得50MB\n用户2获得50MB")
            else:
                print("不正确")
                n = int(input("请输入地址与事件："))
                m = int(input())
                print("%s%s" % (loc[n], date[m]), end='')
                if n == a and m == b:
                    print("正确\n")
                    print("Lvzhou获得100MB\n用户1获得25MB\n用户2获得25MB\n用户3获得50MB")
                else: print("不正确")
if __name__ == '__main__':
    main()