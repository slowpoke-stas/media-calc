mode = 4
while mode == 4:
    print("Расчет величин медиа-файла. Введите порялковый номер:")
    print("  1.Объем файла")
    print("  2.Время звучания")
    print('  3.Частота дискретизации')
    print("  ")
    mode = int(input("№:"))
if mode == 1:
    M = input("Введите частоту дискретизации (в Гц):")
    i = input("Введите глубину кодирования (в бит):")
    t = input("Введите время звучания (в сек):")
    M = float(M)
    i = float(i)
    t = float(t)
    print("  ")
    print("Расчеты:")
    print("---------------------------------")
    print("V = M*i*t")
    print("V = ",M,"*",i,"*",t)
    result = M*i*t
    print (result,'бит')
    print (result/8,'байт')
    print (result/8/1024,'кб')
    print (result/8/1024/1024,'мб')
    print (result/8/1024/1024/1024,'гб')
    mode = 4
    print("---------------------------------")
elif mode == 2:
    M = float(input("Частота дискретизации (в Гц):"))
    i = float(input("Введите глубину кодирования (в бит):"))
    V = float(input("Введите объем файла (в бит):"))
    print("  ")
    print("Расчеты:")
    print("---------------------------------")
    print("t = V/(M*i)")
    print("t = ",V,"/ (",M,"*",i,")")
    ck = M * i
    result = float(V) / float(ck)
    print (result,'сек')
    print (result/60,'мин')
    print (result/60/60,'часов')
    mode = 4
    print("---------------------------------")
elif mode == 3:
    t = float(input("Время звучания (в сек):"))
    i = float(input("Введите глубину кодирования (в бит):"))
    V = float(input("Введите объем файла (в бит):"))
    print("  ")
    print("Расчеты:")
    print("---------------------------------")
    print("M = V/(t*i)")
    print("M = ",V,"/ (",t,"*",i,")")
    ck = t * i
    result = float(V) / float(ck)
    print (result,'Гц')
    mode = 4
    print("---------------------------------")
    
