Summary:	Crosscompiler/crossassembler for 6502 systems
Summary(pl.UTF-8):	Kompilator/asembler skrośny dla systemów 6502
Name:		cc65
Version:	2.13.2
Release:	1
License:	Freeware with exceptions - see docs
Group:		Development/Languages
Source0:	ftp://ftp.musoftware.de/pub/uz/cc65/%{name}-sources-%{version}.tar.bz2
# Source0-md5:	cbf9e25db21002371222ae025a6a1850
URL:		http://www.cc65.org/
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
BuildRequires:	sgml-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C crosscompiler for 6502 systems, including a macroassembler that
supports 6502, 65SC02 and 65816 CPUs, a linker, an archiver and some
other tools. To create programs for one of the supported target
machines, you have to install at least one of the library packages.

%description -l pl.UTF-8
Kompilator skrośny C dla systemów 6502, włączając w to makroassembler
wspierający 6502, 65SC02 oraz 65816 jako CPI, linker i parę innych
narzędzi. By tworzyć programy będziesz musiał zainstalować jeden z
pakietów bibliotecznych.

%package apple2
Summary:	Apple ][ specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Apple ][ biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description apple2
This package contains the header files and libraries needed to write
programs for the Apple ][ using the cc65 crosscompiler.

%description apple2 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Apple ][ korzystając z kompilatora skrośnego cc65.

%package apple2enh
Summary:	Apple //e specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Apple //e biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description apple2enh
This package contains the header files and libraries needed to write
programs for the Apple //e using the cc65 crosscompiler.

%description apple2enh -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Apple //e korzystając z kompilatora skrośnego cc65.

%package atari
Summary:	Atari specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Atari biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description atari
This package contains the header files and libraries needed to write
programs for the 8 bit Atari using the cc65 crosscompiler.

%description atari -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla 8 bitowego Atari korzystając z kompilatora skrośnego
cc65.

%package atmos
Summary:	Oric Atmos specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Oric Atmos biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description atmos
This package contains the header files and libraries needed to write
programs for the Oric Atmos using the cc65 crosscompiler.

%description atmos -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Oric Atmos korzystając z kompilatora skrośnego cc65.

%package c16
Summary:	C16/116 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla C16/116 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description c16
This package contains the header files and libraries needed to write
programs for the Commodore C16/116 using the cc65 crosscompiler.

%description c16 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore C16/116 korzystając z kompilatora skrośnego
cc65.

%package c64
Summary:	C64 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla C64 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description c64
This package contains the header files and libraries needed to write
programs for the Commodore C64 using the cc65 crosscompiler.

%description c64 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore C64 korzystając z kompilatora skrośnego cc65.

%package c128
Summary:	C128 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla C128 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description c128
This package contains the header files and libraries needed to write
programs for the Commodore C128 using the cc65 crosscompiler.

%description c128 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore C128 korzystając z kompilatora skrośnego cc65.

%package cbm510
Summary:	CBM 510 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla CBM 510 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description cbm510
This package contains the header files and libraries needed to write
programs for the Commodore CBM 510 (aka P500) using the cc65
crosscompiler.

%description cbm510 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore CBM 510 (zwany też P500) korzystając z
kompilatora skrośnego cc65.

%package cbm610
Summary:	CBM 610 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla CBM 610 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description cbm610
This package contains the header files and libraries needed to write
programs for the Commodore PET-II (CBM600/700) using the cc65
crosscompiler.

%description cbm610 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore PET-II (CBM600/700) korzystając z kompilatora
skrośnego cc65.

%package geos
Summary:	GEOS specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla GEOS biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description geos
This package contains the header files and libraries needed to write
GEOS programs for the C64/C128 using the cc65 crosscompiler.

%description geos -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów GEOS dla C64/C128 korzystając z kompilatora skrośnego cc65.

%package lynx
Summary:	Lynx specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Lynksa biblioteki dla cc65
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description lynx
This package contains the libraries needed to write programs for the
Lynx using the cc65 crosscompiler.

%description lynx -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla Lynksa
korzystając z kompilatora skrośnego cc65.

%package nes
Summary:	NES (Nintendo Entertainment System) specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla NES (Nintendo Entertainment System) biblioteki dla cc65
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description nes
This package contains the libraries needed to write programs for the
NES (Nintendo Entertainment System) using the cc65 crosscompiler.

%description nes -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla NES
(Nintendo Entertainment System) korzystając z kompilatora skrośnego
cc65.

%package pet
Summary:	PET specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla PET biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description pet
This package contains the header files and libraries needed to write
programs for the Commodore PET using the cc65 crosscompiler.

%description pet -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore PET korzystając z kompilatora skrośnego cc65.

%package plus4
Summary:	Plus/4 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Plus/4 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description plus4
This package contains the header files and libraries needed to write
programs for the Commodore Plus/4 and C16/116 using the cc65
crosscompiler.

%description plus4 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore Plus/4 i C16/116 korzystając z kompilatora
skrośnego cc65.

%package supervision
Summary:	Supervision specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Supervision biblioteki dla kompilatora cc65
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description supervision
This package contains the libraries needed to write programs for the
Supervision console using the cc65 crosscompiler.

%description supervision -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla konsoli
Supervision korzystając z kompilatora skrośnego cc65.

%package vic20
Summary:	VIC20 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla VIC20 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description vic20
This package contains the header files and libraries needed to write
programs for the Commodore VIC20 using the cc65 crosscompiler.

%description vic20 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore VIC20 korzystając z kompilatora skrośnego
cc65.

%prep
%setup -q

# use sgml-tools (no linuxdoc-tools in PLD)
sed -i -e 's/linuxdoc -B /sgml2/' doc/Makefile

%build
%{__make} -C src -f make/gcc.mak \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -ansi -Wall -W -I../common \$(CDEFS)"

%{__make} -j1 -C libsrc zap all
%{__make} -C doc html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/cc65/{asminc,emd,lib,tgi,include/{geos,tgi}}}

install src/ar65/ar65 $RPM_BUILD_ROOT%{_bindir}
install src/ca65/ca65 $RPM_BUILD_ROOT%{_bindir}
install src/ca65html/ca65html $RPM_BUILD_ROOT%{_bindir}
install src/cc65/cc65 $RPM_BUILD_ROOT%{_bindir}
install src/cl65/cl65 $RPM_BUILD_ROOT%{_bindir}
install src/da65/da65 $RPM_BUILD_ROOT%{_bindir}
install src/grc/grc $RPM_BUILD_ROOT%{_bindir}
install src/ld65/ld65 $RPM_BUILD_ROOT%{_bindir}
install src/od65/od65 $RPM_BUILD_ROOT%{_bindir}
install libsrc/*.lib libsrc/*.o $RPM_BUILD_ROOT%{_libdir}/%{name}/lib
install include/*.h $RPM_BUILD_ROOT%{_libdir}/%{name}/include
install include/geos/*.h $RPM_BUILD_ROOT%{_libdir}/%{name}/include/geos
install include/tgi/*.h $RPM_BUILD_ROOT%{_libdir}/%{name}/include/tgi
install asminc/*.inc $RPM_BUILD_ROOT%{_libdir}/%{name}/asminc

# TGI and EM drivers
install libsrc/*.emd $RPM_BUILD_ROOT%{_libdir}/%{name}/emd
install libsrc/*.tgi $RPM_BUILD_ROOT%{_libdir}/%{name}/tgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{BUGS,CREDITS,compile.txt,internal.txt,newvers.txt,readme.1st} doc/*.html announce.txt samples
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/emd
%dir %{_libdir}/%{name}/lib
%dir %{_libdir}/%{name}/tgi
%dir %{_libdir}/%{name}/include
%dir %{_libdir}/%{name}/include/tgi
%dir %{_libdir}/%{name}/asminc
%{_libdir}/%{name}/include/*.h
%{_libdir}/%{name}/asminc/*.inc
%{_libdir}/%{name}/include/tgi/*.h

%files apple2enh
%defattr(644,root,root,755)
%{_libdir}/%{name}/lib/apple2enh.lib
%{_libdir}/%{name}/lib/apple2enh-iobuf-0800.o
%{_libdir}/%{name}/emd/a2e.*.emd
%{_libdir}/%{name}/tgi/a2e.*.tgi

%files apple2
%defattr(644,root,root,755)
%doc src/ld65/cfg/apple2.cfg
%{_libdir}/%{name}/lib/apple2.lib
%{_libdir}/%{name}/lib/apple2-iobuf-0800.o
%{_libdir}/%{name}/emd/a2.*.emd
%{_libdir}/%{name}/tgi/a2.*.tgi

%files atari
%defattr(644,root,root,755)
%doc src/ld65/cfg/atari.cfg
%{_libdir}/%{name}/lib/atari.lib

%files atmos
%defattr(644,root,root,755)
%doc src/ld65/cfg/atmos.cfg
%{_libdir}/%{name}/lib/atmos.lib
%{_libdir}/%{name}/tgi/atmos-*.tgi

%files c16
%defattr(644,root,root,755)
%doc src/ld65/cfg/c16.cfg
%{_libdir}/%{name}/lib/c16.lib
%{_libdir}/%{name}/emd/c16-*.emd

%files c64
%defattr(644,root,root,755)
%doc src/ld65/cfg/c64.cfg
%{_libdir}/%{name}/lib/c64.lib
%{_libdir}/%{name}/emd/c64-*.emd
%{_libdir}/%{name}/emd/dtv-himem.emd
%{_libdir}/%{name}/tgi/c64-*.tgi

%files c128
%defattr(644,root,root,755)
%doc src/ld65/cfg/c128.cfg
%{_libdir}/%{name}/lib/c128.lib
%{_libdir}/%{name}/emd/c128-*.emd
%{_libdir}/%{name}/tgi/c128-*.tgi

%files cbm510
%defattr(644,root,root,755)
%doc src/ld65/cfg/cbm510.cfg
%{_libdir}/%{name}/lib/cbm510.lib
%{_libdir}/%{name}/emd/cbm510-*.emd

%files cbm610
%defattr(644,root,root,755)
%doc src/ld65/cfg/cbm610.cfg
%{_libdir}/%{name}/lib/cbm610.lib
%{_libdir}/%{name}/emd/cbm610-*.emd

%files geos
%defattr(644,root,root,755)
%doc src/ld65/cfg/geos.cfg
%attr(755,root,root) %{_bindir}/grc
%{_libdir}/%{name}/lib/geos.lib
%dir %{_libdir}/%{name}/include/geos
%{_libdir}/%{name}/include/geos/*.h
%{_libdir}/%{name}/emd/geos-*.emd
%{_libdir}/%{name}/tgi/geos-*.tgi

%files lynx
%defattr(644,root,root,755)
%doc src/ld65/cfg/lynx.cfg
%{_libdir}/%{name}/lib/lynx.lib
%{_libdir}/%{name}/tgi/lynx-*.tgi

%files nes
%defattr(644,root,root,755)
%doc src/ld65/cfg/nes.cfg
%{_libdir}/%{name}/lib/nes.lib

%files pet
%defattr(644,root,root,755)
%doc src/ld65/cfg/pet.cfg
%{_libdir}/%{name}/lib/pet.lib

%files plus4
%defattr(644,root,root,755)
%doc src/ld65/cfg/plus4.cfg
%{_libdir}/%{name}/lib/plus4.lib

%files supervision
%defattr(644,root,root,755)
%doc src/ld65/cfg/supervision*.cfg
%{_libdir}/%{name}/lib/supervision.lib

%files vic20
%defattr(644,root,root,755)
%doc src/ld65/cfg/vic20.cfg
%{_libdir}/%{name}/lib/vic20.lib
