# Using the Vision API with Python

Learn how to use various functionality of the Google Cloud Vision API with Python by building 4 separate scripts that highlight a different feature available in the API. This is the corresponding code repo for the _Using the Vision API with Python_ codelab (free, self-paced, hands-on tutorial) at <http://g.co/codelabs/vision-python>.

## Prerequisites

- A Gmail/Google account (Workspace accounts may require administrator approval)
- A Google Cloud (Platform) project
- An active GCP billing account
- Basic Python skills

**Supported versions:** Python 2.6+ or 3.6+

### Python 2 considerations


Python 2 has been [sunset by its community in Jan 2020](http://python.org/doc/sunset-python-2). As such, [support for Python 2 in most Google Cloud products will be waning](https://cloud.google.com/python/docs/python2-sunset) over time (with the except of App Engine, which has [expressed continued long-term support of legacy runtimes](https://cloud.google.com/appengine/docs/standard/long-term-support)). This includes the Vision API, whose final client library version supporting Python 2 is v1.0.0, and whose use is no longer featured in the [Vision API documentation](http://cloud.google.com/vision/docs).

To help accelerate upgrading to 3.x, the scripts in this tutorial only support Python 3 as-is, but commented out code supporting both Python 2 & 3 are available for use if desired. Removing the "# Py2+3" in the code samples gives you a script that works under both Python 2 (under Vision client library v1.0.0) and Python 3 (latest Vision client library). (No "Python 2-only" options are provided.) The Vision API client library source can be found in [its open source repo](https://github.com/googleapis/python-vision).


## Description

The [Google Cloud Vision API](https://cloud.google.com/vision) allows developers to easily integrate vision detection features within applications, including image labeling, facial features detection, landmark detection, optical character recognition (OCR), "safe search", or tagging of explicit content, detecting product or corporate logos, and several others. These are sample scripts that demonstrate usage of the API for the Python language. The code in this repo is both Python 2 & 3 compatible. It is available in Python 2 to help developers migrate to Python 3, and we recommend migrating to 3.x as soon as possible.

### Codelab

This repository consists of the sample scripts that correspond to the ["Using the Vision API with Python" hands-on codelab](http://g.co/codelabs/vision-python). That codelab teaches developers how to use some of the features described above with the Cloud Vision API using Python, namely label annotations, OCR/text extraction, landmark detection, and detecting facial features.

### Cost

Use of the [Vision API is not free](https://cloud.google.com/vision/pricing), however certain Google Cloud Platform (GCP) products feature an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#always-free) for which you have to exceed in order to incur billing. For the purposes of the codelab, each call to the Vision API counts against that free tier, and so long as you stay within its limits in aggregate (within each month), you should not incur any charges.

## Resources

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

### Other languages

- [.NET/C#](https://codelabs.developers.google.com/codelabs/cloud-vision-api-csharp)
- [Ruby](https://web.archive.org/web/20201009194731/https://codelabs.developers.google.com/codelabs/cloud-vision-api-ruby) (archived)

### Support

If you've found an error in the codelab or the sample app, check the [Issues](https://github.com/googlecodelabs/cloud-vision-python/issues) tab to see if there's an open issue or file a new one. Patches are encouraged; please refer to [CONTRIBUTING](CONTRIBUTING.md) for details.
