from stenographer import Stenographer

if __name__ == '__main__':
    stenographer = Stenographer(gap=1000)

    data = "a"*stenographer.max_data_length

    stenographer.hide(data, "original.bmp", "new.bmp")

    print()

    data1 = stenographer.read("new.bmp")

    print()

    print(f"{len(data)} vs {len(data1)}")

    assert data == data1

    print(data1)