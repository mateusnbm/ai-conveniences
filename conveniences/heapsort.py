#
# heapsort.py
#

def sort(data):

    # ...

    n = len(data)
    i = n // 2

    while True:

        if i > 0:

            # ...

            i -= 1
            t = data[i]

        else:

            # ...

            n -= 1
            if n == 0: return
            t = data[n]
            data[n] = data[0]

        pai = i
        filho = i * 2 + 1

        while filho < n:

            if ( (filho + 1 < n) and (data[filho + 1] > data[filho]) ): filho += 1

            if data[filho] > t:

                data[pai] = data[filho]
                pai = filho
                filho = pai * 2 + 1

            else:

                break

        data[pai] = t

    return data
