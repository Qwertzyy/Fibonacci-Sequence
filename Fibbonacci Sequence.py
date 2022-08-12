def fib(number_of_terms):

   #The lower the numeral gets, the longer the sequence goes on.
   counter = 0

   first = 0
   second = 1
   adding = 0
 
   while counter <= number_of_terms:
      print(first)
      adding = first + second
      first = second
      second = adding
      counter = counter + 1

fib(10)