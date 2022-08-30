name,ext = input("File Name:").split(".")
if ext == "gif" or ext == "jpg" or  ext == "jpeg" or ext =="png":
    print(f"image/{ext}")
elif ext == "pdf":
    print(f"application/{ext}")
elif ext == "txt":
    print(f"text/{ext}")
elif ext == "zip":
    print(f"application/{ext}")
else:
    print("application/octet-stream")