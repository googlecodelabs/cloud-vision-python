# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud import vision

IMAGE_URI = 'gs://cloud-samples-data/vision/face/face_no_surprise.jpg'
LIKELIHOOD = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = IMAGE_URI

response = client.face_detection(image=image)

print('=' * 79)
for face in response.face_annotations:
    vertices = [f'({v.x},{v.y})' for v in face.bounding_poly.vertices]
    print('Face surprised:', LIKELIHOOD[face.surprise_likelihood])
    print('Face bounds: {%s}' % ",".join(vertices))
