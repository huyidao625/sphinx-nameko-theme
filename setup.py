from setuptools import setup

setup(
    name='sphinx-nameko-theme-cn',
    version='0.0.3',
    author='hufei',
    author_email='hufei625@qq.com',
    description='Sphinx Nameko Theme Chinese',
    url='https://github.com/huyidao625/sphinx-nameko-theme',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Documentation',
    ],
    packages=['sphinx_nameko_theme'],
    install_requires=['sphinx'],
    entry_points = {
        'sphinx_themes': [
            'path = sphinx_nameko_theme:get_html_theme_path',
        ]
    },
    include_package_data=True,
    zip_safe=False
)
