import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mtANN", 
<<<<<<< HEAD
    version="0.1.0",
    py_modules=['mtANN.model', 'mtANN.utils'],
=======
    version="0.0.0",
    py_modules=['mtANN.mtANN_model', 'mtANN.mtANN_utils'],
>>>>>>> 72453049c5c54617b0d1fca69290eae901d86269
    author="Yi-Xuan Xiong",
    author_email="xyxuana@mails.ccnu.edu.cn",
    description="Ensemble Multiple References for Single-cell RNA Seuquencing Data Annotation and Unseen Cells Identification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)