if you take sequence of chr1 and replace 10 bp with a single number, it will be 25 million number 
sequence , it takes a hell lot of time to run any algorithm on it.
that's where numpy and scipy comes

3 million number for a given chromosome in slide page 5
zip fxn use 


T = np.array(treated)
C = np.array(control)

lfc = np.log2(T/C)

A Python list stores pointers to objects scattered in memory
Every element carries a type tag, a reference count, and a header —
about 32 bytes for one float
Every + goes through the interpreter: check types, dispatch, allocate a new object


A= [3,"a",7]
B= [9,"b",18]
for x,y in zip(A,B):
    print(x-y)

=====> this will raise an error as the str-str is not a valid operation

===> str + str opertaion is supported so it don't



=================
we can convert a list containing string in numpy array it will not raise and error 
but when doing operation which are not suited for strings then we will get the error.

=======================
class assignment 
zcat matrix_data.tsv.gz | python3 filter_sparse_rows.py argument

the argument will be the number of zeros we want in that line to be

=======================
zcat matrix_data.tsv.gz | python3 filter_spares_rows.py 500 

500 is the argument[1] for the python3 command 
so to take in as input in file we write
sys.argv[1] to access the value of 500
sys.argv[0] will give us the file name
sys.stdin will be the data, unzipped using the zcat command
