from distutils.core import setup

setup(
    name='django-notifications-hq',
    version='1.0.0rc1',
    description='GitHub notifications alike app for Django.',
    long_description=open('README.rst').read(),
    author='Amplify Nation',
    author_email='tech@amplify-nation.com',
    url='http://github.com/amplify-nation/django-notifications',
    install_requires=[
      'django>=1.9.2',
      'django-model-utils==2.4'
    ],
    packages=['notifications',
            'notifications.templatetags',
            'notifications.migrations'
           ],
    package_data={'notifications': [
                             'templates/notifications/*.html']},
    classifiers=['Development Status :: 5 - Production/Stable',
               'Environment :: Web Environment',
               'Framework :: Django',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Utilities'],
)
