from basicstenographer import BasicStenographer

if __name__ == '__main__':
    basic_stenographer = BasicStenographer()

    data = """\
Dear Dad,
Let's Kill The Jambon,
Love From Rhys."""#"a"*basic_stenographer.max_data_length

    basic_stenographer.hide(data, "original.bmp", "new.bmp")

    print()

    data1 = basic_stenographer.unhide("new.bmp")

    print()

    #print(f"{len(data)} vs {len(data1)}")

    #assert data == data1

    print(data1)