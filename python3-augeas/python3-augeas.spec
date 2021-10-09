
%global py3_prefix python%{python3_pkgversion}

Name:		python3-augeas
Version:	1.1.0
Release:	1%{?dist}
Summary:	Python 3 bindings to augeas
License:	LGPLv2+
URL:		https://augeas.net/
Source0:	https://github.com/hercules-team/python-augeas/archive/v%{version}/python-augeas-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	augeas
BuildRequires:	%{py3_prefix}-pytest
BuildRequires:	%{py3_prefix}-cffi

Requires:	augeas-libs
Requires:	%{py3_prefix}-cffi
%{?python_provide:%python_provide python3-augeas}

%description
python3-augeas is a set of Python bindings around augeas.

%prep
%autosetup -n python-augeas-%{version} -p1

%build
%{py3_build}

%install
%{py3_install}

%check
%{python3} setup.py test

%files -n python3-augeas
%license COPYING
%doc AUTHORS README.txt
%{python3_sitelib}/augeas.py
%{python3_sitelib}/augeas/
%{python3_sitelib}/python_augeas-*.egg-info
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/test/*


%changelog
* Sun Oct 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.0-1
- initial package based on Fedora's spec file

