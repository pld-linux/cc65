Summary:	Crosscompiler/Crossassembler for 6502 systems
Summary(pl):	Crosskompilator/Crossassembler dla systemów 6502
Name:		cc65
Version:	2.9.2
Release:	1
License:	GPL
Group:		Development/Languages
# ftp.musoftware.de is ugly, there is mirror at ftp://ftp.funet.fi/pub/cbm/programming/cc65/
Source0:	ftp://ftp.musoftware.de/pub/uz/cc65/%{name}-sources-%{version}.tar.bz2
# Source0-md5:	385678b9f7ad86fc231169d12122332b
URL:		http://www.cc65.org/
BuildRequires:	perl
BuildRequires:	sgml-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C crosscompiler for 6502 systems, including a macroassembler that
supports 6502, 65SC02 and 65816 CPUs, a linker, an archiver and some
other tools. To create programs for one of the supported target
machines, you have to install at least one of the library packages.

%description -l pl
C crosskompilator dla systemów 6502, w³±czaj±c w to makroassembler
wspieraj±cy 6502, 65S02 oraz 65816 jako CPI, linker i parê innych
narzêdzi. By tworzyæ programy bêdziesz musia³ zainstalowac jeden z
pakietów bibliotecznych.

%prep
%setup -q

%build
%{__make} -C src -f make/gcc.mak
%{__make} -C libsrc zap all
%{__make} -C doc html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/cc65/{lib,include/geos}}

install -m 755 src/ar65/ar65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/ca65/ca65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/ca65html/ca65html $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/cc65/cc65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/cl65/cl65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/da65/da65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/grc/grc $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/ld65/ld65 $RPM_BUILD_ROOT%{_bindir}
install libsrc/*.lib libsrc/*.o $RPM_BUILD_ROOT%{_libdir}/cc65/lib
install include/*.h $RPM_BUILD_ROOT%{_libdir}/cc65/include
install include/geos/*.h $RPM_BUILD_ROOT%{_libdir}/cc65/include/geos

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{BUGS,CREDITS,compile.txt,grc.txt,internal.txt,newvers.txt,readme.1st} doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_libdir}/cc65
