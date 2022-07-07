def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=0
    x=[]
    i=0
    while i<len(data):
        if data[i].isdigit():
            x.append(int(data[i]))

        i+=1
    
    return max(x)

f=open('txt_file/data08.txt')
data=f.read()
print(main(data))

# Read data from file