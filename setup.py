from setuptools import setup, find_packages

setup(
    name='pyqt-hidable-menubar',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Hidable Menubar (show/hide menu bar with close button at the right corner of it)',
    url='https://github.com/yjg30737/pyqt-hidable-menubar.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main'
    ]
)