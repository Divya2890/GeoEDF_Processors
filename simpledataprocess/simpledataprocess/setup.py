from setuptools import setup, find_packages

setup(name='simpledataprocess',
      version='0.1',
      description='Processor for creates har files data using a txt file which users can edit',
      url='https://github.com/Divya2890/GeoEDF_Processors/simpledataprocess',
      author='Rajesh Kalyanam, Divya Sree Pulipati',
      author_email='rkalyanapurdue@gmail.com, divyareddy2890@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['geopandas'],
      scripts=['bin/02_data_proc.r'],
      data_files=[('data',['data/parameters.csv','data/region.csv'])],
      include_package_data=True,
      zip_safe=False)
