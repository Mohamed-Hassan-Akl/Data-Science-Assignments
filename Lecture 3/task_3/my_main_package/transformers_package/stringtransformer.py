#this module has 2 functions one to reverse a string and second one to capitalize a  string



def reverse_str(t):
    # convert str into list to have ability to use reverse function 
    str_list= list(t)
    str_list.reverse()
    #convert list to str to  have ability to treat it as string 
    list_str_out = "".join(str_list)
    return (list_str_out)



def capitalize_str(x):

    for n in range(len(x)):
        #take only one iteam form the string as capitalize() will capital only the first letter     
        input_cap=x[n]
        #capitalize the letter 
        out_cap=x[n].capitalize()
        #replace the inpu_cap small letter with out_cap capital letter and update the string 
        x=x.replace(input_cap,out_cap)
        
    return x
        