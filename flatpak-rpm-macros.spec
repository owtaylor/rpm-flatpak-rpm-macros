Name:           flatpak-rpm-macros
Version:        26
Release:        1%{?dist}
BuildArch:      noarch
Summary:        Macros for building RPMS for flatpaks
Source0:        macros.flatpak

License:        GPL

%description
The macros in this package set up the environment so built applications install in /app rather than /usr.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
install -t $RPM_BUILD_ROOT%{_sysconfdir}/rpm -m 644 %{SOURCE0}

%files
%{_sysconfdir}/rpm/*

%changelog
* Wed May 31 2017 Owen Taylor <otaylor@redhat.com> - 26-1
- Initial version
