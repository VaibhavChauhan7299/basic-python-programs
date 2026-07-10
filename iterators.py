#iterators: iterators are objects that allow you to traverse through a collection of elements, such as lists, tuples, or dictionaries. In Python, an iterator is an object that implements the iterator protocol, which consists of two methods: __iter__() and __next__().
#iterators are advanced python concepts that allow for efficient looping and memory management. Iterators provide a way to access elements of collection sequentially without exposing the underlying structure.

# my_list = [1, 2, 3, 4, 5, 6]
# for i in my_list:
#     print(i)

# print(type(my_list))


#creating iterator using iterator() function:

#  iterator = iter(my_list)
# print(type(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  # This will raise StopIteration error since there are no more elements to iterate over.
