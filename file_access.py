import os

path = os.getcwd()
input_file = path + "/input_file.txt"
output_file = path + "/output_file.txt"

def make_file(data):
    data = data.decode("utf-8")
    print("Creating file")
    with open(output_file, 'w') as f:
        f.write(data)
    return True

def in_byte(file_path=input_file):
    data = None
    with open(file_path, 'r') as f:
        data = f.read()
    return data.encode("utf-8")


def main():
    data = in_byte()
    make_file(data)


if __name__ == "__main__":
    main()
