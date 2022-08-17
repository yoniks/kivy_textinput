

class resize_of_img:
    def resize_images(self):
      #new_images = p.convert('RGBA').getdata()
      img_example = Image.open(path)
      a = np.asarray(img_example)
      im = Image.fromarray(a)  # <PIL.Image.Image image mode=RGBA size=128x127 at 0x10B01AF70>
      sizes = len(im.getdata())
      print(im, sizes, im.size)
      img = Image.new('RGBA', im.size)
      for i in range(0, 70):# option to do (im.size[0]/2)
          for j in range(0, 126):#im.size[1]
              coordinate = x, y = i,j# result (5, 5)
              print(im.getpixel(coordinate),coordinate, " index: ", i, j)#im.getpixel(coordinate) tuple
              img.putpixel((i, j),im.getpixel(coordinate))  # i=x ___,j=y |    im.getdata(coordination) object
      img.show()



class ConvertImgToAscii:
    def set_path_img(self, path):
        im = Image.open(path)
        print(im)
        new_images = self.pixels_to_ascii(self.grayify(self.resize_image(im)))
        print(type(new_images))
       

        pixel_count = len(new_images)
        print(pixel_count, new_images[0:100])
       

        ascii_image = "\n".join(new_images[i:i + 100] for i in range(0, pixel_count, 100))
        with open("/path/name.txt", "w+") as f:
            f.write(path + ascii_image)

    

    # resize image according to a new width
    def resize_image(self, image, new_width=50):
        width, height = image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        resized_image = image.resize((new_width * 2, new_height))
        print(new_width, new_height, resized_image.size[0])
        return (resized_image)

    # convert each pixel to grayscale
    def grayify(self, image):
        grayscale_image = image.convert("L")
        print(grayscale_image)
        return (grayscale_image)

    # convert pixels to a string of ASCII characters
    def pixels_to_ascii(self, image):
        pixels = image.getdata()
        characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
        return (characters)
