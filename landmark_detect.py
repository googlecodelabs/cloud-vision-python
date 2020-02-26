
from google.cloud import vision

image_uri = 'gs://cloud-vision-codelab/eiffel_tower.jpg'

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = image_uri

response = client.landmark_detection(image=image)

for landmark in response.landmark_annotations:
    print('=' * 79)
    print(landmark)
