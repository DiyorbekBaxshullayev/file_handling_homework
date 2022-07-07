def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x=[]
    list1 = data.split()
    for i in list1:
        x.append(len(i))

    return x

f=open('txt_file/data06.txt')
data=f.read()
print(main(data))

    
# Read data from file