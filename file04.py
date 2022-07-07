def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    i=0
    while i<len(data):
        if data[i].isalpha():
            a.append(data[i])

        i+=1
    
    return a

f=open('txt_file/data04.txt')
data=f.read()
print(main(data))

# Read data from file