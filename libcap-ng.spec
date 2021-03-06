# based on PLD Linux spec git://git.pld-linux.org/packages/libcap-ng.git
Summary:	Next Generation of POSIX capabilities library
Name:		libcap-ng
Version:	0.7.7
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (utilities)
Group:		Libraries
Source0:	http://people.redhat.com/sgrubb/libcap-ng/%{name}-%{version}.tar.gz
# Source0-md5:	3d7d126b29e2869a0257c17c8b0d9b2e
URL:		http://people.redhat.com/sgrubb/libcap-ng/
BuildRequires:	attr-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libcap-ng library should make programming with POSIX capabilities
easier. The library has some utilities to help you analyse a system
for apps that may have too much privileges.

%package devel
Summary:	Header files for libcap-ng library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcap-ng library.

%package utils
Summary:	Utilities for analysing and setting file capabilities
License:	GPL v2+
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains applications to analyse the POSIX capabilities
of all the program running on a system. It also lets you set the file
system based capabilities.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static    \
	--with-python=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libcap-ng.so.0
%attr(755,root,root) %{_libdir}/libcap-ng.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcap-ng.so
%{_libdir}/libcap-ng.la
%{_includedir}/cap-ng.h
%{_pkgconfigdir}/libcap-ng.pc
%{_aclocaldir}/cap-ng.m4
%{_mandir}/man3/capng_*.3*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/captest
%attr(755,root,root) %{_bindir}/filecap
%attr(755,root,root) %{_bindir}/netcap
%attr(755,root,root) %{_bindir}/pscap
%{_mandir}/man8/captest.8*
%{_mandir}/man8/filecap.8*
%{_mandir}/man8/netcap.8*
%{_mandir}/man8/pscap.8*

