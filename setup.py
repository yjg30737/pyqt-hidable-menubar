from setuptools import setup, find_packages

setup(
    name='pyqt-hidable-menubar',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_hidable_menubar.ico': ['close.svg']},
    description='PyQt Hidable Menubar (show/hide menu bar with close button at the right corner of it)',
    url='https://github.com/yjg30737/pyqt-hidable-menubar.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-svg-button>=0.0.1'
    ]
)