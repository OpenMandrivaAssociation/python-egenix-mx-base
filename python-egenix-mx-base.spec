%define rname egenix-mx-base

Name: python-%{rname}
Version: 2.0.6
Release: %mkrel 3
Summary: Python extensions from eGenix
Source0: %{rname}-%{version}.tar.bz2
License: eGenix.com Public License
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://www.egenix.com/files/python/eGenix-mx-Extensions.html
BuildRequires: python-devel 
Obsoletes: egenix-mx-base
Provides: egenix-mx-base = %{version}-%{release}

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
find . -type f -exec sed -i 's|/usr/local.*python|/usr/bin/python|' {} \;

%build
python setup.py   build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --prefix=%_prefix --no-compile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README mx/Doc mx/DateTime/Doc mx/Proxy/Doc mx/BeeBase/Doc mx/Queue/Doc mx/Stack/Doc mx/TextTools/Doc mx/Tools/Doc mx/DateTime/LICENSE mx/DateTime/COPYRIGHT
%{python_sitearch}/mx
%{python_sitelib}/mx
%{py_platsitedir}/*.egg-info


