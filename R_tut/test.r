x <- 5

y<- as.integer(x)

print(y)

z = "Hello world"
print(z[1])

vec_of_number = c(1,2,3,4,5,3,1)
print(vec_of_number[1:4])

#index starts from 1 and the spliting contains both ends. 


#named vectors
dict_equivalent = c(T1=2,T3=4,T5=3,T2=4)
print(names(dict_equivalent))
print(unname(dict_equivalent))

#in python dictionary works with multiple data types
#d[x]= [1,2,3,4]
#d[y]= 5
#d[z]= {"a":"apple","b":"banana"}

check_if_it_is_dict = c(x=c(4,1,3))
print(check_if_it_is_dict)

print(vec_of_number[4])

##multiple ways to slice a list , sequence of 10 integers

first_10_nums = seq(10)
print(first_10_nums[-5:0])
print(first_10_nums[-c(1,2,3,4,5)])
print(first_10_nums[- (1:5)])
some_numbers = seq(1,10,2)
print(some_numbers)
