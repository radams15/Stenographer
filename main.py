from basicstenographer import BasicStenographer
from sys import argv as args

testing = False

if __name__ == '__main__':
    if testing:
        basic_stenographer = BasicStenographer(testing=True)

        data = "a"*basic_stenographer.max_data_length

        basic_stenographer.hide(data, "original.bmp", "new.bmp")

        print()

        data1 = basic_stenographer.unhide("new.bmp")

        print()

        print(f"{len(data)} vs {len(data1)}")

        assert data == data1

        print(data1)
    else:
        basic_stenographer = BasicStenographer()

        op_type = args[1]
        if op_type == "hide":
            data = args[2]
            in_file = args[3]
            out_file = args[4]

            basic_stenographer.hide(data, in_file, out_file)

        elif op_type == "unhide":
            in_file = args[2]

            data = basic_stenographer.unhide(in_file)
            print(f"Data:\n{data}")