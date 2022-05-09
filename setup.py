from setuptools import setup, find_namespace_packages

setup(
    name='folder_cleaner',
    version='1.0.0',
    description='Hw 7. Python packages',
    author='Mykhailo Mavrodii',
    author_email='developer@mail.com',
    url="https://github.com/Mavr1/goit-python/tree/hw7",
    license='MIT',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean_folder=folder_cleaner.main:start']}
)
