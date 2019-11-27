import random
import time
import multiprocessing


array = [ random.randint(0, 10) for i in range(1000000) ]


def count(data):
    result = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
    for i in data:
        result[i] += 1
    return result

start_1 = time.perf_counter()
result_1 = count(array)
hist_time_1 = time.perf_counter() - start_1
print(hist_time_1, ' -> ', result_1)


# ----------------------------------------------------
import multiprocessing

if __name__ == '__main__':
    array = [ random.randint(0, 10) for i in range(1000000) ]


    def process_worker(name, data, process_result):
        result = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
        for i in data:
            result[i] += 1
        process_result[name] = result

    manager = multiprocessing.Manager()
    process_result = manager.dict()
    jobs = []

    p1 = multiprocessing.Process(target=process_worker, args=(1, array[:200000], process_result))
    p2 = multiprocessing.Process(target=process_worker, args=(2, array[200000:400000], process_result))
    p3 = multiprocessing.Process(target=process_worker, args=(3, array[400000:600000], process_result))
    p4 = multiprocessing.Process(target=process_worker, args=(4, array[600000:800000], process_result))
    p5 = multiprocessing.Process(target=process_worker, args=(5, array[800000:], process_result))
    jobs.append(p1)
    jobs.append(p2)
    jobs.append(p3)
    jobs.append(p4)
    jobs.append(p5)

    for p in jobs: p.start()
    for p in jobs: p.join()
    print(process_result.values())



# ----------------------------------------------------
# import queue
# from threading import Thread
# start_2 = time.perf_counter()
# queue = queue.Queue()
# t0 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[:10]))
# t1 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[10:20]))
# t2 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[20:30]))
# t3 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[30:40]))
# t4 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[40:50]))
# t5 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[50:60]))
# t6 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[60:70]))
# t7 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[70:80]))
# t8 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[80:90]))
# t9 = Thread(target=lambda que, arg: queue.put(count(arg)), args=(queue, array[90:]))
# t0.start()
# t0.join()
# t1.start()
# t1.join()
# t2.start()
# t2.join()
# t3.start()
# t3.join()
# t4.start()
# t4.join()
# t5.start()
# t5.join()
# t6.start()
# t6.join()
# t7.start()
# t7.join()
# t8.start()
# t8.join()
# t9.start()
# t9.join()

# result_2 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
# for i in range(10):
#     thread_result = queue.get()
#     for item in thread_result:
#         result_2[item] += thread_result[item]

# hist_time_2 = time.perf_counter() - start_2
# print(hist_time_2, ' -> ', result_2)
