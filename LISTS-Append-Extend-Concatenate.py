# LISTS - Append, Extend, Concatenate
print('''LISTS - Assigning values by using Append, Extend, Concatenate
Learn more about Lists here:
https://www.w3schools.com/python/python_lists.asp
''')      
print('''
Challenge #1 Fi
Run, then Edit the code in the template example:
      
fibonacci_sequence = [0,1,1,2,3, 5, 8, 13, 21, 34]
Rather than just creating the list with the number, 
write a program to calculate the fibonacci number and then 
append, extend and concatenate the sequence
- See how the append works with fibonacci_sequence[0]+
  fibonacci_sequence[1]
- Do this again to append the next value in the sequence.
- Write a for loop to calcualte and append  
  10 more numbers in the sequence
Write a for loop to calcualte and extend 
  10 more numbers in the sequence
      ''')
fibonacci_sequence = [0,1]
print(fibonacci_sequence)
# .append method to Appending to the list
fibonacci_sequence.append(fibonacci_sequence[0]+fibonacci_sequence[1])
print(fibonacci_sequence)
# Use the .append or .extend to add teh next number in the sequence.
fibonacci_sequence.append(fibonacci_sequence[1]+fibonacci_sequence[2])
print(fibonacci_sequence)
# Use a for loop to .append or .extend 20 more of the next numbers in the sequence
for i in range(2,13) :
  print(i)
  fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
  print(fibonacci_sequence)
  
print(fibonacci_sequence[13])
print(fibonacci_sequence[14])

for i in range(13,24) :
  #print(i)
  f=fibonacci_sequence[i] + fibonacci_sequence[i+1]
  fibonacci_sequence.extend([f])
  #print(fibonacci_sequence)
print(fibonacci_sequence)
print('Challenge Complete')
