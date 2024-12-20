from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mattermostdriver',
    version='7.5.0',
    description='A Python Mattermost Driver',
    long_description=long_description,
    url='https://github.com/Vaelor/python-mattermost-driver',
    author='Christian Plümer',
    author_email='github@kuuku.net',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires=">=3.6",
    install_requires=[
        'aiohttp',
        'httpx<=0.27.2',
    ],
    include_package_data=True,  # Ensure that package data specified in MANIFEST.in is included
)
