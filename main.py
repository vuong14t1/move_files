import sys, getopt
import os
import shutil

images_file_exts = ["PNG", "png", "jpg", "jpeg", "JPG"]
FOLDER_DESTINATION = os.path.join(os.path.dirname(__file__), "static/image_1px/1x1.png")
FOLDER_SAVE = os.path.join(os.path.dirname(__file__), "static/save_images/")


def remove_and_move_file(path_des):
    os.remove(path_des)
    print(FOLDER_DESTINATION)
    shutil.copy(FOLDER_DESTINATION, path_des)
    print("Optimize done file: " + path_des)


def is_image(_file_name):
    file_name, file_extension = os.path.splitext(_file_name)
    for ext in images_file_exts:
        if file_extension == "." + ext:
            return True
    return False


def list_folder(folder):
    for f in os.listdir(folder):
        sub_file = os.path.join(folder, f)
        if os.path.isdir(sub_file):
            list_folder(sub_file)
        if os.path.isfile(sub_file):
            remove_and_move_file(sub_file)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            list_folder(arg)


if __name__ == "__main__":
    main(sys.argv[1:])
