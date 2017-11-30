from setuptools import setup

setup(
    name='cdx-index-client',
    version='0.1',
    description='A command-line interface to the CommonCrawl Index API',
    url='https://github.com/harto/cdx-index-client',
    entry_points={
        'console_scripts': [
            'cdx-index-client=cdx_index_client:main',
        ],
    },
)
