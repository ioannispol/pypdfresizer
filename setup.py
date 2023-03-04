from setuptools import setup, find_packages

setup(
    name="pdf_resizer",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["pdf_resizer=pdf_resizer.main:main"]
    },
    install_requires=["PyPDF2", "tk"],
    author="Ioannis Polymenis",
    author_email="your.email@example.com",
    description="A simple GUI tool for resizing PDF files.",
    license="MIT",
    keywords="pdf",
    url="https://github.com/your-username/pdf-resizer",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
