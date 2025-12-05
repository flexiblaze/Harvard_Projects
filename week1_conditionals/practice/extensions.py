

extenstion = input("File name ").lower()


if extenstion.endswith('.gif',):
    print("image/gif")
elif extenstion.endswith('.jpg',):
    print("image/jpg")
elif extenstion.endswith('.jpeg',):
    print("image/jpeg")
elif extenstion.endswith('.png',):
    print("image/png")
elif extenstion.endswith('.pdf',):
    print("application/pdf")
elif extenstion.endswith('.txt',):
    print("text/plain")
elif extenstion.endswith('.zip',):
    print("application/zip")
else:
    print("application/octet-stream")

