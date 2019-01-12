from time import time
from projet_function import *


def listSomma(l):
    sum=0
    for i in range(0,len(l)):
        sum+=l[i]
    return sum

def test_and_csv(func):
    def wrapping_function(*args, **kwargs):
        time_list=[]
        for _ in range(0,args[2]):
            start=time()
            func(*args, **kwargs)
            elapsed = time()-start
            time_list.append(elapsed)
        medium_time = listSomma(time_list)/len(time_list)
        file = open(f'{func.__name__}.csv','a')
        file.write("{},{}\n".format(args[1],medium_time))
        file.close()
    return wrapping_function

@test_and_csv
def testUF(graph,edges,repeat):
    hasCycleUF(graph)

@test_and_csv
def testDFS(graph,edges,repeat):
    hasCycleDFS(graph)


if __name__ == "__main__":

    for n in range (21000,100001,500):
        g = makeGraph(n,randint(0,1))
        testUF(g,len(g.trovaArchi()),2)
        testDFS(g,len(g.trovaArchi()),2)
