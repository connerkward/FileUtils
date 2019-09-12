import shutil
import os
import json

rootdir = '/Volumes/new'
type_path = "/Users/sysadmin/Desktop/foobar/new/"

garbage_types = [".txt", ".csv",".png",".plist",".tif",".ini",".sqlite",
                  ".java",
                 ".gz",".html",".xml",".prproj", ".h", ".wav", ".mp3",
                ".zip", ".aif",".f",'.jsp','.sh','.class','.asp','.ogg',
                 ".exe",".elf",".caf",".tar", '.c', '.lzo',
                  "._501",".dat",".DS_Store",".a",'.xz','.sldprt','.woff',
                 '.vmdk',
                 '.dll','.json','.pl','.ps','.mbox','.icc','.jar','.py',
                 ".bz2"] #

okay_types = [".pdf", ".doc",".docx",".svg",".mov",".mp4",".stl",".xcf",
              ".ttf",".avi",".rtf","m4p",".ai",".psd",'.gif',".webm",'.ppt',
              ".pptx"]

nameset = {"none"}

def json_work():
    if os.path.isfile('utiloutput.txt'):
        with open('utiloutput.txt', 'r') as filehandle:
            working_file_extensions = json.load(filehandle)
        for extension in working_file_extensions:
            garbage_types.append(extension)
def count_files():
    return sum([len(files) for r, d, files in os.walk(rootdir)])

def deleteops():
    i = 0
    length = count_files()
    print(length)
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print("{0:.2f}".format((i / length)*10),"%")
            i += 1
            newpath = os.path.join(subdir, file) # set path name
            if file.endswith(tuple(garbage_types)):
                try:
                    os.remove(os.path.join(subdir, file))
                except FileNotFoundError:
                    print(file, "not found")
            elif file.endswith(".jpg"):
                empty, file_extension = os.path.splitext(newpath)
                location = os.path.join(type_path, file_extension[1:])
                create_folder(location)
                size = os.path.getsize(os.path.join(subdir, file))
                if size > 42000:
                    shutil.copy(newpath, location)
                else:
                    small_loc = os.path.join(location, "small")
                    shutil.copy(newpath, small_loc)
                os.remove(os.path.join(subdir, file))
            elif file.endswith(tuple(okay_types)):
                empty, file_extension = os.path.splitext(newpath)
                location = os.path.join(type_path, file_extension[1:])
                create_folder(location)
                shutil.copy(newpath, location)
                os.remove(os.path.join(subdir, file))
            else:
                print("--------------------")
                print(file, " not recognized")
                name = os.path.splitext(os.path.join(file))[1]
                print("type of file", name)
                nameset.add(str(name))
                print("--------------------")
        if not os.listdir(subdir):
            print("---------empty Directory deleted----------")
            os.rmdir(subdir)
    print("filetypes not recognized", nameset)

def create_folder(location):
    try:
        os.makedirs(location)
    except OSError:
        pass
        #print("Creation of the directory %s failed" % location)
    else:
        pass
        #print("Successfully created the directory %s" location)

def list_types():
    nameset = {"none"}
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            name = os.path.splitext(os.path.join(file))[1]
            print("type of file", name)
            nameset.add(str(name))
    print(nameset)


json_work()
try:
    deleteops()
except KeyboardInterrupt:
    with open('utiloutput.txt', 'w') as filehandle:
        json.dump(list(nameset), filehandle)
    print("filetypes not recognized", nameset)