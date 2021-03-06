# Created by pyp2rpm-3.3.3
%global pypi_name django-cleanup

Name:           python-%{pypi_name}
Version:        5.1.0
Release:        1%{?dist}
Summary:        Deletes old files

License:        MIT License
URL:            https://github.com/un1t/django-cleanup
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_cleanup
%{python3_sitelib}/django_cleanup-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 28 2020 Evgeni Golov - 5.1.0-1
- Initial package.
