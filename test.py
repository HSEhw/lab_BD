from DataBase import *
import matplotlib.pyplot as plt
import time


N = [10, 100, 500, 1000, 10000, 100000, 500000, 1000000]
add_times = []
edit_id_times = []
edit_name_times = []
delete_times = []

for n in N:
    db = DataBase('name')
    t = 0
    for i in range(n):
        start = time.time()
        db.add_with_phone(i, 'a', 'b', '111')
        t += time.time() - start
    add_times.append(t)

    t = 0
    for i in range(n):
        start = time.time()
        db.edit_name(i,'c')
        t += time.time() - start
    edit_name_times.append(t)

    t = 0
    for i in range(n):
        start = time.time()
        db.edit_id(i, i-1)
        t += time.time() - start
    edit_id_times.append(t)

    t = 0
    for i in range(n):
        start = time.time()
        db.del_by_id(i)
        t += time.time() - start
    delete_times.append(t)

print("add: ",add_times)
print("edit id: ", edit_id_times)
print("edit name: ", edit_name_times)
print("delete: ", delete_times)

plt.xlabel('Sizes')
plt.ylabel('Time')

plt.plot(N, add_times, label = 'Add')
plt.plot(N, edit_id_times, label='Edit id')
plt.plot(N, edit_name_times, label='Edit names')
plt.plot(N, delete_times, label='Delete')
plt.legend()
plt.grid()

plt.show()
