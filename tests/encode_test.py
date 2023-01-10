import sys
# sys.path.append("/Users/arulh/Documents/Projects/ImageEncoder")
sys.path.append("../")

from encode import EncodedImage
import timeit

def testConstructor():
    # e = EncodedImage("Hello World", "/Users/arulh/Documents/Projects/ImageEncoder/resources/cat.jpg")
    e = EncodedImage("Hello World", "../resources/")
    e.create_text_image()
    e.encode_image()
    e.create_image()

    assert (e.text == "Hello World")
    assert (e.width == 4032)
    assert (e.height == 3024)

if __name__ == "__main__":
    start = timeit.default_timer()

    testConstructor()

    stop = timeit.default_timer()
    print('\x1b[6;30;42m' + "TESTS PASSED" + '\x1b[0m')
    print("Execution time: " + str(stop - start))