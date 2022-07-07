def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=0
    x=0
    s=[]
    i=0
    while i<len(data):
        if data[i].isdigit():
            x+=1
        else:
            a+=1
        i+=1
    s.append(x)
    s.append(a)
    return s

f=open('txt_file/data05.txt')
data=f.read()
print(main(data))

    
# Read data from file