from setuptools import setup

setup(
    name="eigenvault",
    version="0.1.0",
    packages=["cli"],  # Or your main package/folder name
    entry_points={
        "console_scripts": [
            "eigenvault = src.main:main",  # 'src.main' is the module, 'main' is the function
        ],
    },
    install_requires=[],
    python_requires=">=3.6",
)
