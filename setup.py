import setuptools

with open("README.md", "r") as f:
    lstr_long_description = f.read()

setuptools.setup(
    name='guternberg_api',
    version='1.0.0',
    description='Python Distribution Utilities',
    author='Sonali Bhapkar',
    author_email='shonabhapkar2011@gmail.com',
    long_description=lstr_long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=['flask==2.0.3', 'flask-restful>=0.3.9', 'flask-sqlalchemy==2.5.1', 'mysqlclient==2.1.0','python-json-logger==2.0.1']
)
