def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    i=0
    while i<len(data):
        if data[i].isdigit():
            a.append(data[i])

        i+=1

    return a

f=open('txt_file/data03.txt')
data=f.read()
print(main(data))