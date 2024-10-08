from setuptools import setup, find_packages

setup(name='simpledataclean',
      version='0.1',
      description='Processor for aggregating CSV files downloaded from FAOSTAT database',
      url='https://github.com/Divya2890/GeoEDF_Processors/simpledataclean',
      author='Rajesh Kalyanam , Divya Sree Pulipati',
      author_email='rkalyanapurdue@gmail.com, divyareddy2890@gmail.com',
      license='MIT',
      packages=find_packages(),
      scripts=['bin/01_data_clean.r'],
      data_files=[('data',['data/in/reg_map.csv','data/in/reg_sets.csv','data/in/crop_sets.csv','data/in/livestock_sets.csv'])],
      include_package_data=True,
      zip_safe=False)
