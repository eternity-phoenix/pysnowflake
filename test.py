from pysnowflake import getId
import threading

def getIds(l):
    l.extend([getId() for i in range(10)])


if __name__ == '__main__':
    l = []
    ts = []
    for i in range(10):
        ts.append(threading.Thread(target=getIds, args=(l,)))
    for t in ts:
        t.start()
        t.join()
    assert len(l) == 100, 'Error'