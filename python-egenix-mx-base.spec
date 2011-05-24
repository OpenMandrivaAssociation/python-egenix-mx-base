%define rname egenix-mx-base

Name:           python-%{rname}
Version:        3.2.0
Release:        %mkrel 1
Summary:        Python extensions from eGenix
License:        eGenix.com Public License
Group:          Development/Python
URL: http://www.egenix.com/files/python/eGenix-mx-Extensions.html
Source0:        http://downloads.egenix.com/python/%{rname}-%{version}.tar.gz
Patch0:         egenix-mx-base-fix_underlinking.diff
Obsoletes: %{rname} < %{version}-%{release}
Provides: egenix-mx-base = %{version}-%{release}
BuildRequires:	python-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{_bindir}/find . -type f | grep .py | %{_bindir}/xargs -t %{__sed} -i 's|/usr/local.*python|/usr/bin/python|'
%patch0 -p0

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --prefix=%_prefix --no-compile

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README mx/*/Doc
%doc mx/DateTime/LICENSE mx/DateTime/COPYRIGHT
%{python_sitearch}/mx
%{python_sitelib}/mx
%{py_platsitedir}/*.egg-info
