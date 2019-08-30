from setuptools import setup

setup(name='tsconv',
      version='0.0.2',
      description='convert ts in sec/milisec/microsec/nanosec to human readable time',
      long_description='convert ts in sec/milisec/microsec/nanosec to human readable time',
      author='Guo Xiaoyong',
      author_email='guo.xiaoyong@gmail.com',
      url='https://github.com/guoxiaoyong/tsconv',
      packages=['tsconv'],
      include_package_data=True,
      entry_points={
         'console_scripts': ['tsconv=tsconv:main'],
      },
)
