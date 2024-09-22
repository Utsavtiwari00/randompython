filesuffix = input("File name: ").lower().strip()
if filesuffix.endswith(".gif"):
     print("images/gif")
elif filesuffix.endswith(".jpg") or filesuffix.endswith("jpeg"):
      print("images/jpeg")
elif filesuffix.endswith(".png"):
      print("images/png")
elif filesuffix.endswith(".pdf"):
     print("application/pdf")
elif filesuffix.endswith(".txt"):
     print("text/plain")
elif filesuffix.endswith(".zip"):
     print("application.zip")
else:
     print("application/octet-stream")

