%global pypi_name certbot-dns-sakuracloud
%global py3_prefix python%{python3_pkgversion}

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has problems building the documentation due to #1492884
%bcond_with docs
%else
%bcond_without docs
%endif

Name:           python-%{pypi_name}
Version:        1.14.0
Release:        1%{?dist}
Summary:        Sakura Cloud DNS Authenticator plugin for Certbot

License:        ASL 2.0
URL:            https://github.com/certbot/certbot
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
Source2:        https://dl.eff.org/certbot.pub

BuildArch:      noarch

BuildRequires:  python3-acme >= 0.31.0
BuildRequires:  python3-certbot >= 1.1.0
BuildRequires:  python3-devel
BuildRequires:  python3-dns-lexicon >= 2.1.23
BuildRequires:  %{py3_prefix}-pytest
BuildRequires:  python3-setuptools

%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  %{py3_prefix}-sphinx_rtd_theme
%endif

# Used to verify OpenPGP signature
BuildRequires:  gnupg2

%description
Sakura Cloud DNS Authenticator plugin for Certbot

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-acme >= 0.31.0
Requires:       python3-certbot >= 1.1.0
Requires:       python3-dns-lexicon >= 2.1.23
Requires:       python3-setuptools
Requires:       %{py3_prefix}-zope-interface

# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:      %{pypi_name} = %{version}-%{release}
%endif

%description -n python3-%{pypi_name}
Sakura Cloud DNS Authenticator plugin for Certbot

This is the Python 3 version of the package.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-certbot-dns-sakuracloud
%description -n python-%{pypi_name}-doc
Documentation for python-certbot-dns-sakuracloud
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if %{with docs}
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
%{__python3} -m pytest

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/certbot_dns_sakuracloud
%{python3_sitelib}/certbot_dns_sakuracloud-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files doc
%license LICENSE.txt
%doc README.rst
%doc html
%endif

%changelog
* Wed Apr 07 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0 (#1946820)

* Tue Mar 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0 (#1934813)

* Tue Feb 2 2021 Nick Bebout <nb@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0 (#1913033)

* Thu Dec  3 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#1904199)

* Thu Dec  3 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0 (#1903327)

* Thu Oct 08 2020 Nick Bebout <nb@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Tue Oct 06 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Aug 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#1866071)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1854590)

* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843217)

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831929)

* Thu Mar 05 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-2
- bump release to retry koji build

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809785)

* Sat Feb 29 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.0-1
- Update to 1.2.0 (#1791083)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769117)

* Wed Dec 04 2019 Eli Young <elyscape@gmail.com> - 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757590)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748628)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742591)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717692)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686199)

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673774)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669328)

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1627584)

* Thu Jul 19 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.0-1
- Initial import (#1602111)
