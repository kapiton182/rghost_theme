import shutil
import os

def getFilename(endFile): #возвращает файл из директории запуска переданного расширения
    for i in os.listdir():
        if os.path.isfile(i) and i.endswith(endFile):
            return i
    else:
        print('В директории нет нужных файлов')


def createFolder(name):
    try:
        os.mkdir(name)
    except OSError:
        print("Такая папка уже создана")


def main():
    nameArchive = getFilename('zip')
    nameFileKeys = getFilename('txt')
    keys = []
    with open(nameFileKeys, 'r') as keys:
        keys = [s for s in keys.read().split('\n') if s != '']
    nameFolder = nameFileKeys[:-4]
    createFolder(nameFolder)
    for i in keys:
        shutil.copy(nameArchive, nameFolder+'\\'+i+'.zip')


if __name__ == "__main__":
    main()
