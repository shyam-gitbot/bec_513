import sys
import time
start_time = time.perf_counter()
file = sys.stdin

avg,cnt =0,0
for i in file:
    avg+= int(i)
    cnt+=1
# print(avg/cnt)
avg=avg/cnt

#var = sum(xi-avg)^2 /n
var = 0
for i in file:
    print(int(i))
    var+=((int(i)-avg)**2)
    print(var)
var=var/cnt
print("avg :",avg,"var :",var)
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")

file = "data.txt"
with open(file,"r") as file:
    avg,cnt =0,0
    for i in file:
        avg+= int(i)
        cnt+=1
    avg = avg/cnt

    var = 0
    for j in file:
        print(int(j))
        var+=((int(j)-avg)**2)
        print(var)
    var=var/cnt
    print("avg :",avg,"var :",var)