import setuptools
import os

print('-------------installing--------------')

os.system('pip3 install websocket-client')



setuptools.setup(
  name="hackchatpy",
  version="1.0",
  author="Sprinkle",
  author_email="sprinkleponcho@dingtalk.com",
  description="A package for hack-chat",
  long_description='A package for hack-chat',
  long_description_content_type="text/markdown",
  url="https://github.com/pypa/sampleproject",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
