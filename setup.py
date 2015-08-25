import os
from setuptools import setup, find_packages
import image_exif

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="django_image_exif",
    version=image_exif.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.md'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, filer, gallery, django-filer, image, exif',
    author='Sven Hertle',
    author_email='sven.hertle@googlemail.com',
    url="https://github.com/svenhertle/django_image_exif",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-filer',
        'exifread',
    ],
)
