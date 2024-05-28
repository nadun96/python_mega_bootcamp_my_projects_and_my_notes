import zipfile

def extract_archive(archivepath, destination):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(destination)

if __name__ == "__main__":
    extract_archive(r"E:\Portfolio\UDEMY\CURRENT\Python mega\s19 day 18 - gui styles\archive extractor\compressed.zip",r"E:\Portfolio\UDEMY\CURRENT\Python mega\s19 day 18 - gui styles\archive extractor")       
