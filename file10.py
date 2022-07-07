def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x=[]
    list1=data.split('\n')
    for i in list1:
        x.append(int(len(i)))

    
    return max(x)

f=open('txt_file/data10.txt')
data=f.read()
print(main(data))


# Read data from file