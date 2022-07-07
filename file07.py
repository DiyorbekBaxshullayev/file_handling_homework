def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=0
    i=0
    while i<len(data):
        if data[i].isdigit():
            a += int(data[i])
        i+=1
        
    return a

f=open('txt_file/data07.txt')
data=f.read()
print(main(data))
# Read data from file