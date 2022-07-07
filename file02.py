def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s = 0
    for i in data:
        s += 1

    return s

f=open('txt_file/data02.txt')
data=f.read()
print(main(data))
# Read data from file