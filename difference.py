import sys
from PIL import Image
from imagehash import phash

# I'm pretty sure I borrowed this function from somewhere, but cannot remember
# the source to cite them properly.
def hash_hamming_distance(h1, h2):
    s1 = str(h1)
    s2 = str(h2)
    return sum(map(lambda x: 0 if x[0] == x[1] else 1, zip(s1, s2)))

def is_similar_img(path1, path2):
    image1 = Image.open(path1)
    image2 = Image.open(path2)

    dist = hash_hamming_distance(phash(image1), phash(image2))
    return dist

if __name__ == "__main__":
    #img_path = "./trixi_frog.png"
    img_path = sys.argv[1]

    dist = is_similar_img("./trixi.png", img_path)
    print('P hash distance from original dog photo: %s'%(dist))

