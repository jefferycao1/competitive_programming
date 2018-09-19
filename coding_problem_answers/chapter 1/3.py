def removespace(a):
    a = a.strip()
    a = a.replace(" ", "%20")
    print(a)



if __name__ == "__main__":
    a = "Mr John Smith   "
    removespace(a)
    
