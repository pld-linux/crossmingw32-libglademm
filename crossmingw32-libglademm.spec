Summary:	C++ wrappers for libglade (cross mingw32 version)
Summary(pl.UTF-8):	Interfejsy C++ dla libglade (wersja skrośna mingw32)
%define		_realname   libglademm
Name:		crossmingw32-%{_realname}
Version:	2.6.3
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libglademm/2.6/%{_realname}-%{version}.tar.bz2
# Source0-md5:	3dd3c3777c4407b8a330bd79089ddbfc
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	crossmingw32-gcc-c++
BuildRequires:	crossmingw32-gtkmm >= 2.10.0
BuildRequires:	crossmingw32-libglade2 >= 2.6.0
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	perl-base
BuildRequires:	pkgconfig
Requires:	crossmingw32-gtkmm >= 2.10.0
Requires:	crossmingw32-libglade2 >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
C++ wrappers for libglade (cross mingw32 version).

%description -l pl.UTF-8
Interfejsy C++ dla libglade (wersja skrośna mingw32).

%package static
Summary:	Static libglademm library (cross mingw32 version)
Summary(pl.UTF-8):	Statyczna biblioteka libglademm (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static libglademm library (cross mingw32 version).

%description static -l pl.UTF-8
Statyczna biblioteka libglademm (wersja skrośna mingw32).

%package dll
Summary:	DLL libglademm library for Windows
Summary(pl.UTF-8):	Biblioteka DLL libglademm dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-gtkmm-dll >= 2.10.0
Requires:	crossmingw32-libglade2-dll >= 2.6.0
Requires:	wine

%description dll
DLL libglademm library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL libglademm dla Windows.

%prep
%setup -q -n %{_realname}-%{version}

%build
export PKG_CONFIG_PATH=%{_prefix}/lib/pkgconfig
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--target=%{target} \
	--host=%{target} \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

rm -rf $RPM_BUILD_ROOT%{_libdir}/libglademm-2.4/proc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_libdir}/libglademm-2.4.la
%{_libdir}/libglademm-2.4.dll.a
%{_includedir}/%{_realname}-2.4
%{_libdir}/%{_realname}-2.4
%{_pkgconfigdir}/%{_realname}-2.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglademm-2.4.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libglademm*-2.4-*.dll
