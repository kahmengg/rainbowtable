Description of Reduction Function:
Reduction function takes in the hash value and finds an index/integer 
to point to the next password. It is calculated by converting it to long
and then modulus the amount of passswords there are.

Formular is as such:  index = long_number % num_of_passwords

Note:
The program processes 2100 words per minute to rainbow.txt file. 
It will prompt an input for a hash after generating the rainbow.txt file.

It took me about 6 minutes to generate the rainbow.txt as it has 25k passswords
but i have checked that the output is correct using another shorter password file to text.

Program will keep asking for user input after generating rainbow.txt 
Will display invalid if hash is invalid
After displaying the preimage it will prompt hash value again
Ctrl+C to end
