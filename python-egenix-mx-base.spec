%define rname egenix-mx-base

Summary:	Python extensions from eGenix
Name:		python-%{rname}
Version:	3.2.6
Release:	11
License:	eGenix.com Public License
Group:		Development/Python
Url:		https://www.egenix.com/files/python/eGenix-mx-Extensions.html
Source0:	http://downloads.egenix.com/python/%{rname}-%{version}.tar.gz
Source100:	python-egenix-mx-base.rpmlintrc
Patch0:		egenix-mx-base-fix_underlinking.diff
Patch1:		mx-3.1.1-lib64.patch
BuildRequires:	pkgconfig(python2)
Provides:	egenix-mx-base = %{version}-%{release}

%description
The eGenix mx Extension Series are a collection of
Python extensions written in ANSI C and Python
which provide a large spectrum of useful additions
to everyday Python programming.

The BASE package includes the Open Source subpackages
of the series and is needed by all other add-on
packages of the series.

This software is brought to you by eGenix.com and
distributed under the eGenix.com Public License.

%prep
%setup -qn %{rname}-%{version}
find . -type f | grep .py | xargs -t sed -i 's|/usr/local.*python|/usr/bin/python|'
%patch0 -p0
%patch1 -p1

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=%{buildroot} --prefix=%{_prefix} --no-compile

%files
%doc README mx/*/Doc
%doc mx/DateTime/LICENSE mx/DateTime/COPYRIGHT
%{python2_sitearch}/mx
%{py2_platsitedir}/*.egg-info

