while True:
    try:
        n = int(input())
    except:
        break

    num = 1
    count = 1

    while True:
        if num % n == 0:
            break
        else:
            num = 10 * num + 1
            count += 1
        
    print(count)