#!/usr/bin/env python
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
 * =========================================================================
 * setup.py
 * -------------------------------------------------------------------------
 * DESCRIPTION:   Generic setup.py (generic_setup). This setup.py reads
 *                values from the source code of your module/application
 *                and auto-assemble the setup() function arguments for
 *                distutils.
 *                It also automagically generate an RPM .spec file with
 *                data gathered from inside your main program source file.
 *
 * AUTHOR:        (rcs) Rogério Carvalho Schneider <stockrt@gmail.com>
 *                http://stockrt.github.com
 * =========================================================================
'''
__program_file__        = 'setup.py'
__program_name__        = 'generic_%s' % __program_file__.split('.py')[0]
__scripts__             = []
__data_files__          = []
__version__             = '0.1.4'
__date__                = '2011/03/14'
__author_name__         = 'Rogério Carvalho Schneider'
__author_email__        = 'stockrt@gmail.com'
__author__              = '%s <%s>' % (__author_name__, __author_email__)
__maintainer_name__     = __author_name__
__maintainer_email__    = __author_email__
__maintainer__          = '%s <%s>' % (__maintainer_name__, __maintainer_email__)
__copyright__           = 'Copyright (C) 2011 %s' % __author_name__
__license__             = 'GPLv3'
__url__                 = 'http://stockrt.github.com'
__download_url__        = __url__
__py_modules__          = []
__platforms__           = ['any']
__keywords__            = 'generic setup.py'
__classifiers__         = [
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Utilities',
]
__description__         = 'Generic setup.py (generic_setup)'
__long_description__    = '''%s
Generic setup.py (generic_setup). This setup.py reads values from the source
code of your module/application and auto-assemble the setup() function
arguments for distutils.
It also automagically generate an RPM .spec file with data gathered from
inside your main program source file.
''' % __program_file__

### IMPORTS_START ###
try:
    import sys
    import re
    import os
    import itertools
    from distutils.sysconfig import get_python_lib
    from distutils.sysconfig import get_python_version
except ImportError, why:
    print
    print 'Error loading module: [%s]' % why
    print '''
You need to install some extra modules in order to run this program:
- easy_install
    wget http://peak.telecommunity.com/dist/ez_setup.py
    python ez_setup.py
    easy_install ...
- pip:
    pip install ...
'''
    sys.exit(1)
### IMPORTS_END ###

### DEFINES_START ###
# Set this parameter to point to your source file, leave the rest as is:
source_code = 'pytranslate.py'

# Basic specfile defines
brpmdata = '''
# Recommended Topdir
%define _topdir %(echo $HOME)/rpmbuild

# So the build does not fail due to unpackaged files or missing doc files:
%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0

# No debug package:
%define debug_package %{nil}
'''

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
### DEFINES_END ###

def local(command):
    ret = os.system(command)
    if ret:
        raise Exception('ERR: Error running local command: %s' % command)

def sortuniq(lista):
    if isinstance(lista, list) or isinstance(lista, tuple):
        return sorted([a for a,b in itertools.groupby(sorted(lista))])
    else:
        raise TypeError('Argument for sortuniq(arg) must be a tuple or a list')

def generic_setup():
    print 'For more help on %s, type:' % __program_name__
    print '    ./setup.py %s using' % __program_name__
    print '    ./setup.py %s rpmbuild' % __program_name__
    print
    print 'For automated rpmbuild, with custom .spec, type:'
    print '    ./setup.py rpmbuild'
    print

def generic_setup_using():
    print '''
##
## Using the generic_setup to distribute your software
##

- To start using this Generic setup.py (generic_setup) you need to do two
things:


1) Put these lines into your source code file, and change the values to match
your application.
- Right in the beginning of your source file, just after the interpreter
line, you should put your descriptions and then this:


-- copy this sample --
#!/usr/bin/env python
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

### GENERIC_SETUP_MARKER_START ###
__program_file__        = 'your_program.py'
__program_name__        = '%s' % __program_file__.split('.py')[0]
# if you have scripts
__scripts__             = []
# if only a module
__data_files__          = []
# if a program (have config files, extras)
__data_files__          = [('/usr/local/%s/conf' % __program_name__, ['%s.conf' % __program_name__]), ('/usr/local/%s/bin' % __program_name__, [__program_file__]), ('/var/spool/%s' % __program_name__, [])]
__version__             = '0.1.8'
__date__                = '2011/03/14'
__author_name__         = 'Rogério Carvalho Schneider'
__author_email__        = 'stockrt@gmail.com'
__author__              = '%s <%s>' % (__author_name__, __author_email__)
__maintainer_name__     = __author_name__
__maintainer_email__    = __author_email__
__maintainer__          = '%s <%s>' % (__maintainer_name__, __maintainer_email__)
__copyright__           = 'Copyright (C) 2011 %s' % __author_name__
__license__             = 'GPLv3'
__url__                 = 'http://stockrt.github.com'
__download_url__        = __url__
# if installing a module
__py_modules__          = [__program_name__]
# if you don't have modules
__py_modules__          = []
__platforms__           = ['any']
__keywords__            = 'python utilities functions'
__classifiers__         = [
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Utilities',
]
__description__         = 'Python utilities.'
__long_description__    = \'''%s
Python utilities.
\''' % __program_file__
__rpm_data__            = \'''
%post
echo
echo 'Some message to your users'
echo

%files
%defattr(-,root,root,-)
%dir /var/spool/%{name}
%config(noreplace) /usr/local/%{name}/conf/%{name}.conf
/usr/local/%{name}/bin/%{name}.py
\'''
### GENERIC_SETUP_MARKER_END ###
-- copy this sample --


- Then here you start the 'import' calls, whatsoever.
- Note that the tags MUST be placed as in the sample, since they are markers
for the generic_setup:
    '### GENERIC_SETUP_MARKER_START ###'
and
    '### GENERIC_SETUP_MARKER_END ###'
- Just copy/paste the sample into your source code and it should work fine.


2) Edit this setup.py script and change the 'source_code' define to point to
your program.
- Point it to your app:

### DEFINES_START ###
# Set this parameter to point to your source file, leave the rest as is:
#source_code = 'change_me.py'
source_code = 'your_program.py'
### DEFINES_END ###


3) Customize any other specfile tag you want to use, but keep %files as the
last one.


Done :)


Now you can:
    ./setup.py install          install your app
    ./setup.py sdist            create a source distribution (tarball, zip file, etc.)
    ./setup.py bdist            create a built (binary) distribution
    ./setup.py bdist_dumb       create a "dumb" built distribution
    ./setup.py bdist_rpm        create an RPM distribution
    ./setup.py bdist_wininst    create an executable installer for MS Windows
    ./setup.py register         register the distribution with the Python Package Index
    ./setup.py sdist upload     upload the source distribution to the Python Package Index
    ./setup.py bdist upload     upload the built (binary) distribution to the Python Package Index

And the special rpmbuild:
    ./setup.py rpmbuild         automated rpmbuild with custom .spec

Also you can still use all the commands and options available from --help and --help-commands
'''

def generic_setup_rpmbuild():
    print '''
##
## RPM creation tips
##

- Some tips on creating RPM packages:


# Creating the RPM (rpmbuild tip)
- Create an RPM based on the .spec automagically generated from the data
gathered in the main source file of your application:

    yum -y install rpmdev-setuptree
    rpmdev-setuptree

    ./setup.py rpmbuild

** When you are creating your own project, you may want to change some data
in the source file, as it's name, descriptions and RPM data, since this is
only an example.


# Creating the RPM (bdist_rpm tip)
- The default distutils approach for automatic RPM generation:

    ./setup.py bdist_rpm

** This approach has a problem: It do not take care of %config(noreplace) for
the configuration files we may have in our project, so take a look at the
"rpmbuild tip" above using a custom, automagically generated, RPM .spec file.
'''

def rpmbuild(sname, sversion, srpmdata):
    try:
        # Dirs
        local('mkdir -p ~/rpmbuild/BUILD')
        local('mkdir -p ~/rpmbuild/RPMS')
        local('mkdir -p ~/rpmbuild/SOURCES')
        # Default .spec
        local('./setup.py bdist_rpm --spec-only')
        # Default tarball
        local('./setup.py sdist --dist-dir ~/rpmbuild/SOURCES/')
        # Python Lib dir and Version
        pylib = get_python_lib()
        pyver = get_python_version()
        # Applying the changes to the .spec (%post/%files/%defattr/%dir/%config):
        # Initialize spec with the basic
        newspec = brpmdata
        for l in open('dist/%s.spec' % sname).readlines():
            # Remove the defaults:
            # '%files -f INSTALLED_FILES'
            # '%defattr(-,root,root,-)'
            if '%files -f INSTALLED_FILES' not in l and '%defattr' not in l:
                newspec += l
        # Insert the user defined specs (%post/%files/%defattr/%dir/%config):
        newspec += srpmdata

        # New INSTALLED_FILES
        build_tmp = '~/rpmbuild/BUILD/tmp'
        build_installed_files = os.path.join(PROJECT_DIR, 'build/INSTALLED_FILES')
        local('rm -rf %s' % build_tmp)
        local('./setup.py install --root=%s --record=%s' % (build_tmp, build_installed_files))
        local('python -O -m compileall %s' % build_tmp)
        local('cd %s && find . -type f | sed \'s,^\.,,g\' >> %s' % (build_tmp, build_installed_files))
        new_installed_files = []
        for l in open(build_installed_files).readlines():
            new_installed_files.append(l)
        new_installed_files = sortuniq(new_installed_files)
        new_installed_files_output = ''.join(new_installed_files)
        open(build_installed_files, 'w').write(new_installed_files_output)
        newspec += new_installed_files_output
        newspec += '\n'

        # New specfile
        open('dist/%s.spec' % sname, 'w').write(newspec)
        # Create the new RPM
        local('rpmbuild -bb dist/%s.spec' % sname)
        # Copy the created RPM to dist/
        local('/bin/cp ~/rpmbuild/RPMS/noarch/%s-%s-*.rpm dist/' % (sname, sversion))
    except Exception, why:
        print 'ERR: Error building the RPM with custom .spec file: [%s]' % why
        print

##########
## MAIN ##
##########
def main():
    # Help for generic_setup
    if len(sys.argv) == 3:
        if sys.argv[1] == 'generic_setup' and sys.argv[2] == 'using':
            generic_setup_using()
            sys.exit(0)
        if sys.argv[1] == 'generic_setup' and sys.argv[2] == 'rpmbuild':
            generic_setup_rpmbuild()
            sys.exit(0)

    # Distribution function
    from distutils.core import setup

    # Read source file content
    if not os.path.exists(source_code):
        print
        print 'ERR: Check your setup.py script defines. File not found: [%s]' % source_code
        print
        generic_setup()
        sys.exit(1)
    source_code_data = open(source_code).read()

    # Does this file contain special coding?
    coding = re.search('(.*coding: .*)', source_code_data)
    setup_data = ''
    if coding:
        setup_data += coding.group(1)

    # Search for the delimiters and filter content between:
    ### GENERIC_SETUP_MARKER_START ###
    ### GENERIC_SETUP_MARKER_END ###
    if '### GENERIC_SETUP_MARKER_START ###' not in source_code_data or \
    '### GENERIC_SETUP_MARKER_END ###' not in source_code_data:
        print
        print 'ERR: Check your program "%s" define markers. Some of the \
required markers are missing (\
\"### GENERIC_SETUP_MARKER_START ###\" or \
\"### GENERIC_SETUP_MARKER_END ###\").' % source_code
        generic_setup()
        sys.exit(1)
    setup_data += source_code_data.split('### GENERIC_SETUP_MARKER_START ###')[1].split('### GENERIC_SETUP_MARKER_END ###')[0]

    # Save this content, so we can import to use it later:
    open('setup_data_file.py', 'w').write(setup_data)
    try:
        import setup_data_file
    except Exception, why:
        print
        print 'ERR: Check your program "%s" defines. Some of the required \
entries are probably missing: [%s]' % (source_code, why)
        generic_setup()
        sys.exit(1)
    try:
        os.remove('setup_data_file.py')
        os.remove('setup_data_file.pyc')
    except:
        pass

    # Test if the program file contains all the variables needed to run setup.py
    try:
        sname             = setup_data_file.__program_name__
        sscripts          = setup_data_file.__scripts__
        sdata_files       = setup_data_file.__data_files__
        sversion          = setup_data_file.__version__
        sauthor_email     = setup_data_file.__author_email__
        sauthor           = setup_data_file.__author__
        smaintainer_email = setup_data_file.__maintainer_email__
        smaintainer       = setup_data_file.__maintainer__
        slicense          = setup_data_file.__license__
        surl              = setup_data_file.__url__
        sdownload_url     = setup_data_file.__download_url__
        spy_modules       = setup_data_file.__py_modules__
        splatforms        = setup_data_file.__platforms__
        skeywords         = setup_data_file.__keywords__
        sclassifiers      = setup_data_file.__classifiers__
        sdescription      = setup_data_file.__description__
        slong_description = setup_data_file.__long_description__
        srpmdata          = setup_data_file.__rpm_data__
    except Exception, why:
        print
        print 'ERR: Check your program "%s" defines. Some of the required \
entries are probably missing: [%s]' % (source_code, why)
        generic_setup()
        sys.exit(1)

    # Remove e-mail from the author's and maintainer's name (for the .spec generation)
    sauthor = sauthor.split(' <')[0]
    smaintainer = smaintainer.split(' <')[0]

    # Create the MANIFEST file with data_files included
    s = ['setup.py', setup_data_file.__program_file__]
    for f in sdata_files:
        for f1 in f[1]:
            s.append(f1)
    for f in sscripts:
        s.append(f)
    # sort -u
    s = sortuniq(s)
    m = open('MANIFEST', 'w')
    for f in s:
        m.write(f + '\n')
    m.close()

    # Modules
#    for m in spy_modules:
#        if not os.path.exists(m):
#            os.mkdir(m)
#        if not os.path.exists(m + '/__init__.py'):
#            open(m + '/__init__.py', 'a').write('')

    # All set here. Just use the values now.

    # Help for generic_setup
    if len(sys.argv) == 1:
        generic_setup()

    # rpmbuild for a custom, automagically generated RPM .spec file
    if len(sys.argv) == 2:
        if sys.argv[1] == 'rpmbuild':
            rpmbuild(sname, sversion, srpmdata)
            sys.exit(0)

    # Older versions do not have 'classifiers'
    if sys.version_info < (2, 3):
        _setup = setup
        def setup(**kwargs):
            if kwargs.has_key('classifiers'):
                del kwargs['classifiers']
            _setup(**kwargs)

    # The real thing
    setup(
        name             = sname,
        scripts          = sscripts,
        data_files       = sdata_files,
        version          = sversion,
        author_email     = sauthor_email,
        author           = sauthor,
        maintainer_email = smaintainer_email,
        maintainer       = smaintainer,
        license          = slicense,
        url              = surl,
        download_url     = sdownload_url,
        py_modules       = spy_modules,
        platforms        = splatforms,
        keywords         = skeywords,
        classifiers      = sclassifiers,
        description      = sdescription,
        long_description = slong_description
    )

    # Clean all, really
    if len(sys.argv) == 2:
        if sys.argv[1] == 'clean':
            local('rm -rf MANIFEST build dist temp *.pyc *.pyo')
            for m in spy_modules:
                local('rm -rf %s.egg-info' % m)
            sys.exit(0)

if __name__ == '__main__':
    main()

'''
# References:
http://docs.python.org/distutils/
http://docs.python.org/install/
http://docs.python.org/distutils/setupscript.html
http://docs.python.org/distutils/apiref.html#module-distutils.core

# Trove classifiers:
http://pypi.python.org/pypi?:action=list_classifiers

# Maximum RPM:
http://www.rpm.org/max-rpm/
'''
