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

image_uri = 'gs://cloud-vision-codelab/otter_crossing.jpg'

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = image_uri

response = client.text_detection(image=image)

for text in response.text_annotations:
    print('=' * 79)
    print(f'"{text.description}"')
    vertices = [f'({v.x},{v.y})' for v in text.bounding_poly.vertices]
    print(f'bounds: {",".join(vertices)}')
