from random import randint

def gen_arr (lenght):
    return [randint (1,100) for i in range (lenght)]
def pearson(X, Y):
    return ((len(X) * sum(map(lambda z: z[0] * z[1], zip(X, Y))) - sum(X) * sum(Y)) /
            ((len(X) * sum(map(lambda x: x ** 2, X)) - sum(X) ** 2) *
             (len(Y) * sum(map(lambda y: y ** 2, Y)) - sum(Y) ** 2)) ** 0.5)

if __name__ == '__main__':
    arr1,arr2 = gen_arr (10),gen_arr (10)
    print (f"Для списков:\n{arr1}\nи\n{arr2}\nкоффициент корреляция Пирсона:\n{pearson(arr1, arr2)}")