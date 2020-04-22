# organize imports
import sys
import numpy as np
from keras.models import Model
from keras.preprocessing import image
from keras.applications import imagenet_utils, mobilenet

# process an image to be mobilenet friendly
def process_image(img_path):
  img = image.load_img(img_path, target_size=(224, 224))
  img_array = image.img_to_array(img)
  img_array = np.expand_dims(img_array, axis=0)
  pImg = mobilenet.preprocess_input(img_array)
  return pImg

# main function
if __name__ == '__main__':

  # path to image
  #img_path = "trixi.png"
  #img_path = "trixi_frog.png"
  #img_path = "trixi_sealion.png"
  img_path = sys.argv[1]

  # process the image
  pImg = process_image(img_path)

  # define the mobilenet model
  mobilenet = mobilenet.MobileNet()

  # make predictions on image using mobilenet
  prediction = mobilenet.predict(pImg)

  # obtain the top-5 predictions
  results = imagenet_utils.decode_predictions(prediction)
  print(results)

