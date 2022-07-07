def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=0
    i=0
    x=[]
    while i<len(data):
        if data[i].isdigit():
            x.append(int(data[i]))

        i+=1
    
    return min(x)

f=open('txt_file/data09.txt')
data=f.read()
print(main(data))


# Read data from file