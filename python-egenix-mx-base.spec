%define rname egenix-mx-base

Name:		python-%{rname}
Version:	3.2.4
Release:	1
Summary:	Python extensions from eGenix
License:	eGenix.com Public License
Group:		Development/Python
URL:		http://www.egenix.com/files/python/eGenix-mx-Extensions.html
Source0:	http://downloads.egenix.com/python/%{rname}-%{version}.tar.gz
Patch0:		egenix-mx-base-fix_underlinking.diff
Patch1:		mx-3.1.1-lib64.patch
Obsoletes:	%{rname} < %{version}-%{release}
Provides:	egenix-mx-base = %{version}-%{release}
BuildRequires:	python-devel

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
%setup -q -n %{rname}-%{version}
find . -type f | grep .py | xargs -t sed -i 's|/usr/local.*python|/usr/bin/python|'
%patch0 -p0
%patch1 -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix} --no-compile

%files
%defattr(-,root,root,0755)
%doc README mx/*/Doc
%doc mx/DateTime/LICENSE mx/DateTime/COPYRIGHT
%{python_sitearch}/mx
%{py_platsitedir}/*.egg-info

