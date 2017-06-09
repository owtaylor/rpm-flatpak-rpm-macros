Name:           flatpak-rpm-macros
Version:        27
Release:        1%{?dist}
BuildArch:      noarch
Summary:        Macros for building RPMS for flatpaks
Source0:        macros.flatpak

License:        MIT

%description
The macros in this package set up the RPM build environment so built applications install in /app rather than /usr. This package is meant only for installation in buildroots for modules that will be packaged as Flatpaks.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
install -t $RPM_BUILD_ROOT%{_sysconfdir}/rpm -m 644 %{SOURCE0}

%files
# The location in sysconfdir contradicts
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
# but I believe is necessary to properly override macros that are otherwise set.
%{_sysconfdir}/rpm/*

%changelog
* Wed May 31 2017 Owen Taylor <otaylor@redhat.com> - 27-1
- Initial version, based on work by Alex Larsson <alexl@redhat.com>
