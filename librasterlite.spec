Summary:	Spatial SQL database engine based on SQLite
Summary(pl.UTF-8):	Silnik przestrzennej bazy danych SQL oparty na SQLite
Name:		librasterlite
Version:	1.1c
Release:	2
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://www.gaia-gis.it/gaia-sins/librasterlite-sources/%{name}-%{version}.tar.gz
# Source0-md5:	f9c18e25fe50d6fc501b7d14c149782f
URL:		https://www.gaia-gis.it/fossil/librasterlite
BuildRequires:	libgeotiff-devel >= 1.2.5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	libgeotiff >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spatial SQL database engine based on SQLite.

%description -l pl.UTF-8
Silnik przestrzennej bazy danych SQL oparty na SQLite.

%package devel
Summary:	Header files for rasterlite library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki rasterlite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgeotiff-devel >= 1.2.5
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel
Requires:	zlib-devel

%description devel
Header files for rasterlite library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki rasterlite.

%package static
Summary:	Static rasterlite library
Summary(pl.UTF-8):	Statyczna biblioteka rasterlite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static rasterlite library.

%description static -l pl.UTF-8
Statyczna biblioteka rasterlite.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librasterlite.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog 
%attr(755,root,root) %{_bindir}/rasterlite_*
%attr(755,root,root) %{_libdir}/librasterlite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librasterlite.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librasterlite.so
%{_includedir}/rasterlite.h
%{_pkgconfigdir}/rasterlite.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librasterlite.a
