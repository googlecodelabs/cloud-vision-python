# Using the Vision API with Python

Learn how to use various features found in the Google Cloud Vision API with Python.

## Prerequisites

- A Google account (G Suite accounts may require administrator approval)
- A Google Cloud Platform project
- An active GCP billing account
- A modern web browser such Chrome or Firefox
- Familiarity with standard Linux text editors such as Vim, Emacs or Nano
- Basic Python skills; at least Python 3.6+ (2.x is no longer supported but the code should still work provided you make the appropriate backports.)

## Description

The [Google Cloud Vision API](https://cloud.google.com/vision) allows developers to easily integrate vision detection features within applications, including image labeling, facial features detection, landmark detection, optical character recognition (OCR), "safe search", or tagging of explicit content, detecting product or corporate logos, and several others. These are sample scripts that demonstrate usage of the API for the Python language. It is possible to backport the code to 2.x provided you have the requisite libraries, however we recommend migrating to 3.x as soon as possible.

### Codelab

This repository consists of the sample scripts that correspond to the ["Using the Vision API with Python" hands-on codelab](http://g.co/codelabs/vision-python). That codelab teaches developers how to use some of the features described above with the Cloud Vision API using Python, namely label annotations, OCR/text extraction, landmark detection, and detecting facial features.

### Cost

Use of the [Vision API is not free](https://cloud.google.com/vision/pricing), however certain Google Cloud Platform (GCP) products feature an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#always-free) for which you have to exceed in order to incur billing. For the purposes of the codelab, each call to the Vision API counts as a single "unit," and so long as you stay under that limit in aggregate (within each month), you should not incur any charges.

## Support

- [Google Cloud Vision API home page and live demo](https://cloud.google.com/vision)
- [Vision API label detection/annotation](https://cloud.google.com/vision/docs/labels)
- [Vision API facial feature recognition](https://cloud.google.com/vision/docs/detecting-faces)
- [Vision API landmark detection](https://cloud.google.com/vision/docs/detecting-landmarks)
- [Vision API optical character recognition (OCR)](https://cloud.google.com/vision/docs/ocr)
- [Vision API "Safe Search"](https://cloud.google.com/vision/docs/detecting-safe-search)
- [Vision API product or corporate logo detection](https://cloud.google.com/vision/docs/detecting-logos)
- [Python on the Google Cloud Platform](https://cloud.google.com/python)
- [GCP Python client libraries](https://googlecloudplatform.github.io/google-cloud-python)
