import os

import setuptools

main_ns = {}
ver_path = os.path.abspath("wqp/__init__.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setuptools.setup(
    name="wqp",
    version=main_ns["__version__"],
    author="nicolas.gallot@gmail.com",
    description="Wine quality predictor - a packaged machine learning algorithm to predict wine",
    packages=setuptools.find_packages(),
    install_requires=["scikit-learn==1.3", "pandas==2.1.2", "click==8.1.7"],
    entry_points="""
    [console_scripts]
    wqp=wqp.cli:wqp
    """,
)
