from setuptools import setup, find_packages

setup(name='simpledataprocess02',
      version='0.1',
      description='Processor for converting Shapefiles to GeoJSON format',
      url='http://github.com/geoedf/shapefile2geojson',
      author='Rajesh Kalyanam',
      author_email='rkalyanapurdue@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['geopandas'],
      scripts=['bin/02_data_proc.r'],
      data_files=[('data',['data/parameters.csv','data/region.csv'])],
      include_package_data=True,
      zip_safe=False)
