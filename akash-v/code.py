# --------------
#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file=open(path,"r")
    #Reading of the first line of the file and storing it in a variable
    sentence= file.readline()
    #Closing of the file
    file.close()
    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
sample_message=read_file(file_path)
#Printing the line of the file
message_1= read_file(file_path_1)
message_2= read_file(file_path_2)
print(message_1)
print(message_2)

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient=int(message_b)//int(message_a)
    #Returning the quotient in string format
    quotient=str(quotient)
    return quotient
#Calling the function to read file  
secret_msg_1= fuse_msg(message_1,message_2)
#Calling the function to read file
message_3= read_file(file_path_3)

#Calling the function 'fuse_msg'
print(message_3)

#Printing the secret message 



#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if(message_c=="Red"):
        sub= "Army General"
    if(message_c=="Green"):
        sub= "Data Scientist"
    if(message_c=="Blue"):
        sub= "Marine Biologist"
    return sub

    
    #Returning the substitute of the message
secret_msg_2= substitute_msg(message_3)    
    

#Calling the function to read file
message_4= read_file(file_path_4)
message_5= read_file(file_path_5)

print(message_4)
print(message_5)

#Calling the function 'substitute_msg'

#Printing the secret message



#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list= message_d.split()
    b_list= message_e.split()
    c_list=[]
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    for i in a_list:
        if(i in a_list) and (i not in b_list):
            c_list.append(i)
    
    final_msg=c_list[0]+" "+c_list[1]+" "+c_list[2]
    return final_msg
    

    
    #Combining the words of a list back to a single string sentence
secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)
    
    #Returning the sentence
message_6=read_file(file_path_6)
print(message_6)    
    

#Calling the function to read file


#Calling the function to read file


#Calling the function 'compare messages'


#Printing the secret message


#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list=message_f.split()
    even_word= lambda x: len(x)%2==0
    b_list=list(filter(even_word,a_list))
    final_msg=b_list[0]+" "+b_list[1]+" "+b_list[2]+" "+b_list[3]
    return final_msg

secret_msg_4= extract_msg(message_6)
    
    #Creating the lambda function to identify even length words
    
    
    #Splitting the message into a list
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg= message_parts[0]+" "+message_parts[1]+" "+message_parts[2]+" "+message_parts[3]



# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message


#Function to write inside a file
def write_file(secret_msg,path):
       
    #Opening a file named 'secret_message' in 'write' mode
    a=open(path,"a+")
    a.write(secret_msg)
    a.close()


    #Writing to the file
write_file(secret_msg,final_path)

    #Closing the file
print(secret_msg)

#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


