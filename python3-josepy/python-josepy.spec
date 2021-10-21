%global pypi_name josepy

%global py3_prefix python%{python3_pkgversion}

%bcond_with docs

Name:           python3-%{pypi_name}
Version:        1.10.0
Release:        1%{?dist}
Summary:        JOSE protocol implementation in Python

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/josepy
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
Source2:        https://dl.eff.org/certbot.pub
BuildArch:      noarch

# Remove various unpackaged testing dependencies that are used only for linting
Patch0:         0000-ignore-missing-linters.patch

BuildRequires:  %{py3_prefix}-cryptography
BuildRequires:  %{py3_prefix}-devel
BuildRequires:  %{py3_prefix}-pytest
BuildRequires:  %{py3_prefix}-pyOpenSSL
BuildRequires:  %{py3_prefix}-setuptools

# Used to verify OpenPGP signature
BuildRequires:  gnupg2

%description
JOSE protocol implementation in Python using cryptography.

This is the Python 3 version of the package.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
rm %{buildroot}%{_bindir}/jws

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -x -v

%files
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/josepy
%{python3_sitelib}/josepy-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Sep 30 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.0-1
- initial Python 3 package for EPEL 7
