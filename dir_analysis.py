import os

# traverse root directory, and list directories as dirs and files as files
filetypes = {}
for root, dirs, files in os.walk("."):
    for f in files:
        filename, fileextnsion = os.path.splitext(f)
        try:
            filetypes[fileextnsion] = filetypes[fileextnsion] + 1
        except KeyError:
            filetypes[fileextnsion] = 1

