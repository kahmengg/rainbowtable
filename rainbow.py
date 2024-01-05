import hashlib

input_file = "Passwords.txt"
output_File = 'Rainbow.txt'

# Define the hash function 
def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

# Read password.txt
def password_list(file_name):
    with open(file_name, 'r') as fp:
        return [j.strip() for j in fp] #Return a list of all passwords


# Reduction function
def reduction(text):
    with open(input_file, 'r') as file:
        line_count = sum(1 for line in file)  # returns the number of words
        
    # Convert hash digest to long number
    long_number = int(text,16)
    reduced_password_index = long_number % line_count  # reduce password formular
    return reduced_password_index  # returns index for next password

# Q4
def write(rainbow_dict):
    with open('Rainbow.txt', 'w') as file:
        #loop dict and write to txt.file
        for hashed_value, original_pass in rainbow_dict.items():
            file.write(f"{hashed_value} {original_pass}\n")
          
       
def generate_rainbow_dictionary(passwords):
    # Initialize rainbow table in dictionary
    rainbow_table = {}
    # Declare to store used passwords
    used_pass = set()
    
    # Q2
    for i in passwords:
        hashed_value = md5(i)  # hashed value for password
        original_pass = i  
        if i not in used_pass: # if password is not used
            
            for j in range(5):   #reduce 5 times and find the next password
                reduced_index = reduction(hashed_value)  #gives index of next password
                next_password = password_list(input_file)[reduced_index-1] #find password associated with index
                hashed_of_nextpassword = md5(next_password)
                #Add the used password to set
                used_pass.add(next_password)
                # assign next hashed password
                hashed_value = hashed_of_nextpassword
                # Store the next password and the final current hash in the rainbow table
                rainbow_table[original_pass] = hashed_value 

    sorted_rainbow_table = {k: v for k, v in sorted(rainbow_table.items(), key=lambda item: item[1])}
    return sorted_rainbow_table

# Q3
def preimage(rainbowtable, user_hash_input):
    # length of a MD5 hash is 32 bit
    md5_length = 32
    while len(user_hash_input)!= md5_length:
        user_hash_input = input("Invalid hash value, please input a 32-bit MD5 Hash \nEnter a hash value: ")
    else:
        # hash cannot be found  rainbow table
        i = 0 # number of times reduced
        while user_hash_input in rainbowtable.values():
        #when its found in rainbow table
            for k, v in rainbowtable.items():
                if v == user_hash_input:
                    final_password = k
                    break# Find the final password/ matched password
            # hash & reduct final password to get pre image
            hashed_of_final_pass = md5(final_password)
            while user_hash_input != hashed_of_final_pass: 
                reduced = reduction(hashed_of_final_pass)
                next_password = password_list(input_file)[reduced-1]
                hashed_of_final_pass = md5(next_password)

            print("The preimage for your hash is: ", next_password)
            break
        else: 
            # reduction function
            if i < 10: #loop to reduce
                pass_index = reduction(user_hash_input)
                next_password = password_list(input_file)[pass_index-1]
                hashed_of_nextpassword = md5(next_password)
                user_hash_input = hashed_of_nextpassword
                i+=1
            else:
                input("Unable to find pre-image")
        
        
def main():
    # generate rainbow table txt file
    with open(input_file, 'r') as file:
        line_count = sum(1 for line in file)
        # Q1
        print("Q1. There are ", line_count ," passwords in ", input_file, "\nWill take awhile depending how many passwords there are")
    all_passwords = password_list(input_file)  # list of passwords
    rain_dict = generate_rainbow_dictionary(all_passwords)
    write(rain_dict)
    with open(output_File, 'r') as file:
        line_count = sum(1 for line in file)
        print("Q4. There are ", line_count ," passwords in readbow.txt!")

    while True:
        # Keep asking
        userinput = input("Enter a hash value: ")
        preimage(rain_dict,userinput)

    
    
if __name__ == "__main__": 
    main()    




