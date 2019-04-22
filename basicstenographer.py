from PIL import Image

class BasicStenographer:
    def __init__(self, gap=1000):
        self.gap = gap
        self.max_data_length = 255*3*2 #765 as r,g,b (3 times) 255 (max rgb val) times 2 for two pixels
        self.pixels_to_skip = [[0,0], [0,1]]

    def split_list(self, a_list):
        half = len(a_list) // 2
        return a_list[:half], a_list[half:]

    def calculate_gap(self, data_len, img, gap):
        area = (img.size[0]*img.size[1])
        return (data_len*gap)**2%(area/data_len)

    def even_divide(self, number, values):
        floor = number // values
        remainder = number % values
        out = [floor]*(values-1)
        out.append(floor+remainder)
        return tuple(out)

    def hide(self, data, img_path, out_path):
        img = Image.open(img_path)
        pixels = img.load()

        i=0
        data_len = len(data)

        if data_len > self.max_data_length:
            print(f"Data must be less than {self.max_data_length} chars")

        data_len_divided = self.even_divide(data_len, 6)
        print(len(data_len_divided))
        print(data_len_divided)
        pixels[0,0] = data_len_divided[:len(data_len_divided)//2]
        pixels[1, 0] = data_len_divided[len(data_len_divided)//2:]

        gap = self.calculate_gap(data_len, img, self.gap)
        gap_run=0

        for col in range(img.size[0]):
            for row in range(img.size[1]):
                if [col, row] in self.pixels_to_skip:
                    continue
                if i < data_len and gap_run >= gap: #if there is still data, and over the run
                    red, green, blue = pixels[col, row]

                    red = ord(data[i])
                    try:
                        green = ord(data[i+1])
                    except IndexError:
                        green = 32

                    try:
                        blue = ord(data[i+2])
                    except IndexError:
                        blue = 32

                    pixels[col, row] = red, green, blue

                    i += 3
                    gap_run = 0
                else:
                    gap_run += 1

        img.save(out_path)

    def read(self, img_path):
        img = Image.open(img_path)
        pixels = img.load()

        i=0
        data_len = sum(pixels[0,0])+sum(pixels[1,0])
        print(pixels[0,0], pixels[1,0])

        gap = self.calculate_gap(data_len, img, self.gap)
        gap_run=0
        data = [chr(32) for i in range(data_len+2)] # add two as dividing the data between three rgb colours means there could be two extra spaces

        for col in range(img.size[0]):
            for row in range(img.size[1]):
                if [col, row] in self.pixels_to_skip:
                    continue
                red, green, blue = pixels[col, row]

                if i < data_len and gap_run >= gap: #if there is still data, and over the current run
                    print(f"Read {red}, {green}, {blue}")

                    data[i] = chr(red)
                    data[i+1] = chr(green)
                    data[i+2] = chr(blue)

                    i += 3
                    gap_run = 0
                else:
                    gap_run += 1

        return "".join(data).strip()