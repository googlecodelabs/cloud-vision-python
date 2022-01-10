# Using the Vision API with Python

Learn how to use various functionality of the Google Cloud Vision API with Python by building 4 separate scripts that highlight a different feature available in the API.

## Prerequisites

- A Google account (G Suite accounts may require administrator approval)
- A Google Cloud Platform project
- An active GCP billing account
- Basic Python skills

NOTE: Python >=3.6 is required for this codelab. Python 2 is no longer supported but the code should work provided you make the appropriate backports (e.g., `print()` function calls, f-strings, etc.) and use the Python 2 Vision API client library—see [its repo](https://github.com/googleapis/python-vision) for the last known 2.x version.

## Description

The [Google Cloud Vision API](https://cloud.google.com/vision) allows developers to easily integrate vision detection features within applications, including image labeling, facial features detection, landmark detection, optical character recognition (OCR), "safe search", or tagging of explicit content, detecting product or corporate logos, and several others. These are sample scripts that demonstrate usage of the API for the Python language. It is possible to backport the code to 2.x provided you have the requisite libraries, however we recommend migrating to 3.x as soon as possible.

### Codelab

This repository consists of the sample scripts that correspond to the ["Using the Vision API with Python" hands-on codelab](http://g.co/codelabs/vision-python). That codelab teaches developers how to use some of the features described above with the Cloud Vision API using Python, namely label annotations, OCR/text extraction, landmark detection, and detecting facial features.

### Cost

Use of the [Vision API is not free](https://cloud.google.com/vision/pricing), however certain Google Cloud Platform (GCP) products feature an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#always-free) for which you have to exceed in order to incur billing. For the purposes of the codelab, each call to the Vision API counts against that free tier, and so long as you stay within its limits in aggregate (within each month), you should not incur any charges.

## Resources

### This codelab in other languages

- [.NET/C#](https://codelabs.developers.google.com/codelabs/cloud-vision-api-csharp)
- [Ruby](https://web.archive.org/web/20201009194731/https://codelabs.developers.google.com/codelabs/cloud-vision-api-ruby) (archived)

### Cloud Vision API

- [Google Cloud Vision API home page and live demo](https://cloud.google.com/vision)
- [Vision API label detection/annotation](https://cloud.google.com/vision/docs/labels)
- [Vision API facial feature recognition](https://cloud.google.com/vision/docs/detecting-faces)
- [Vision API landmark detection](https://cloud.google.com/vision/docs/detecting-landmarks)
- [Vision API optical character recognition (OCR)](https://cloud.google.com/vision/docs/ocr)
- [Vision API "Safe Search"](https://cloud.google.com/vision/docs/detecting-safe-search)
- [Vision API product or corporate logo detection](https://cloud.google.com/vision/docs/detecting-logos)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-vision)

### Python and Google Cloud

- [Python on the Google Cloud Platform](https://cloud.google.com/python)
- [GCP Python client libraries](https://googlecloudplatform.github.io/google-cloud-python)

### Support

If you've found an error in the codelab or the sample app, check the [Issues](https://github.com/googlecodelabs/cloud-vision-python/issues) tab to see if there's an open issue or file a new one. Patches are encouraged; please refer to [CONTRIBUTING](CONTRIBUTING.md) for details.
