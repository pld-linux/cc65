Summary:	Crosscompiler/crossassembler for 6502 systems
Summary(pl):	Kompilator/asembler skrośny dla systemów 6502
Name:		cc65
Version:	2.10.1
Release:	1
License:	Freeware with exceptions - see docs
Group:		Development/Languages
# ftp.musoftware.de is ugly, there is mirror at ftp://ftp.funet.fi/pub/cbm/programming/cc65/
#Source0:	ftp://ftp.musoftware.de/pub/uz/cc65/%{name}-sources-%{version}.tar.bz2
Source0:	http://cc65.civitas64.de/%{name}-sources-%{version}.tar.bz2
# Source0-md5:	ea600666a514a792d2a18c4af2859380
Patch0:		%{name}-types.patch
URL:		http://www.cc65.org/
BuildRequires:	perl-base
BuildRequires:	sgml-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C crosscompiler for 6502 systems, including a macroassembler that
supports 6502, 65SC02 and 65816 CPUs, a linker, an archiver and some
other tools. To create programs for one of the supported target
machines, you have to install at least one of the library packages.

%description -l pl
Kompilator skrośny C dla systemów 6502, włączając w to makroassembler
wspierający 6502, 65SC02 oraz 65816 jako CPI, linker i parę innych
narzędzi. By tworzyć programy będziesz musiał zainstalować jeden z
pakietów bibliotecznych.

%package vic20
Summary:	VIC20 specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla VIC20 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description vic20
This package contains the header files and libraries needed to write
programs for the Commodore VIC20 using the cc65 crosscompiler.

%description vic20 -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore VIC20 korzystając z kompilatora skrośnego
cc65.

%package c16
Summary:	C16/116 specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla C16/116 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description c16
This package contains the header files and libraries needed to write
programs for the Commodore C16/116 using the cc65 crosscompiler.

%description c16 -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore C16/116 korzystając z kompilatora skrośnego
cc65.

%package c64
Summary:	C64 specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla C64 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description c64
This package contains the header files and libraries needed to write
programs for the Commodore C64 using the cc65 crosscompiler.

%description c64 -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore C64 korzystając z kompilatora skrośnego cc65.

%package c128
Summary:	C128 specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla C128 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description c128
This package contains the header files and libraries needed to write
programs for the Commodore C128 using the cc65 crosscompiler.

%description c128 -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore C128 korzystając z kompilatora skrośnego cc65.

%package atari
Summary:	Atari specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla Atari biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description atari
This package contains the header files and libraries needed to write
programs for the 8 bit Atari using the cc65 crosscompiler.

%description atari -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla 8 bitowego Atari korzystając z kompilatora skrośnego
cc65.

%package plus4
Summary:	Plus/4 specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla Plus/4 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description plus4
This package contains the header files and libraries needed to write
programs for the Commodore Plus/4 and C16/116 using the cc65
crosscompiler.

%description plus4 -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore Plus/4 i C16/116 korzystając z kompilatora
skrośnego cc65.

%package pet
Summary:	PET specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla PET biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description pet
This package contains the header files and libraries needed to write
programs for the Commodore PET using the cc65 crosscompiler.

%description pet -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore PET korzystając z kompilatora skrośnego cc65.

%package cbm510
Summary:	CBM 510 specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla CBM 510 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description cbm510
This package contains the header files and libraries needed to write
programs for the Commodore CBM 510 (aka P500) using the cc65
crosscompiler.

%description cbm510 -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore CBM 510 (zwany też P500) korzystając z
kompilatora skrośnego cc65.

%package cbm610
Summary:	CBM 610 specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla CBM 610 biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description cbm610
This package contains the header files and libraries needed to write
programs for the Commodore PET-II (CBM600/700) using the cc65
crosscompiler.

%description cbm610 -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore PET-II (CBM600/700) korzystając z kompilatora
skrośnego cc65.

%package apple2
Summary:	Apple ][ specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla Apple ][ biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description apple2
This package contains the header files and libraries needed to write
programs for the Apple ][ using the cc65 crosscompiler.

%description apple2 -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Apple ][ korzystając z kompilatora skrośnego cc65.

%package atmos
Summary:	Oric Atmos specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla Oric Atmos biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description atmos
This package contains the header files and libraries needed to write
programs for the Oric Atmos using the cc65 crosscompiler.

%description atmos -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Oric Atmos korzystając z kompilatora skrośnego cc65.

%package geos
Summary:	GEOS specific libraries and headers for the cc65 compiler
Summary(pl):	Specyficzne dla GEOS biblioteki i pliki nagłówkowe
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description geos
This package contains the header files and libraries needed to write
GEOS programs for the C64/C128 using the cc65 crosscompiler.

%description geos -l pl
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów GEOS dla C64/C128 korzystając z kompilatora skrośnego cc65.

%package nes
Summary:	NES (Nintendo Entertainment System) specific libraries for the cc65 compiler
Summary(pl):	Specyficzne dla NES (Nintendo Entertainment System) biblioteki dla cc65
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description nes
This package contains the libraries needed to write programs for the
NES (Nintendo Entertainment System) using the cc65 crosscompiler.

%description nes -l pl
Pakiet zawiera biblioteki potrzebne do pisania programów dla NES
(Nintendo Entertainment System) korzystając z kompilatora skrośnego
cc65.

%package supervision
Summary:	Supervision specific libraries for the cc65 compiler
Summary(pl):	Specyficzne dla Supervision biblioteki dla kompilatora cc65
License:	Freeware
Group:		Development/Languages
Requires:	%{name} = %{version}

%description supervision
This package contains the libraries needed to write programs for the
Supervision console using the cc65 crosscompiler.

%description supervision -l pl
Pakiet zawiera biblioteki potrzebne do pisania programów dla konsoli
Supervision korzystając z kompilatora skrośnego cc65.

%prep
%setup -q
%patch0 -p1

echo 'CDEFS=-D$(SPAWN)' >> src/cl65/make/gcc.mak

%build
%{__make} -C src -f make/gcc.mak \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -I../common \$(CDEFS)"

%{__make} -C libsrc zap all
%{__make} -C doc html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/cc65/{asminc,emd,lib,tgi,include/{geos,tgi}}}

install -m 755 src/ar65/ar65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/ca65/ca65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/ca65html/ca65html $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/cc65/cc65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/cl65/cl65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/da65/da65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/grc/grc $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/ld65/ld65 $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/od65/od65 $RPM_BUILD_ROOT%{_bindir}
install libsrc/*.lib libsrc/*.o $RPM_BUILD_ROOT%{_libdir}/%{name}/lib
install include/*.h $RPM_BUILD_ROOT%{_libdir}/%{name}/include
install include/geos/*.h $RPM_BUILD_ROOT%{_libdir}/%{name}/include/geos
install include/tgi/*.h $RPM_BUILD_ROOT%{_libdir}/%{name}/include/tgi
install asminc/*.inc $RPM_BUILD_ROOT%{_libdir}/%{name}/asminc

# TGI and EM drivers
install -m 644 libsrc/*.emd $RPM_BUILD_ROOT%{_libdir}/%{name}/emd
install -m 644 libsrc/*.tgi $RPM_BUILD_ROOT%{_libdir}/%{name}/tgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{BUGS,CREDITS,compile.txt,grc.txt,internal.txt,newvers.txt,readme.1st} doc/*.html announce.txt samples
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

%files vic20
%defattr(644,root,root,755)
%doc src/ld65/cfg/vic20.cfg
%{_libdir}/%{name}/lib/vic20.lib
%{_libdir}/%{name}/lib/vic20.o

%files c16
%defattr(644,root,root,755)
%doc src/ld65/cfg/c16.cfg
%{_libdir}/%{name}/lib/c16.lib
%{_libdir}/%{name}/lib/c16.o
%{_libdir}/%{name}/emd/c16-*.emd

%files c64
%defattr(644,root,root,755)
%doc src/ld65/cfg/c64.cfg
%{_libdir}/%{name}/lib/c64.lib
%{_libdir}/%{name}/lib/c64.o
%{_libdir}/%{name}/emd/c64-*.emd
%{_libdir}/%{name}/tgi/c64-*.tgi

%files c128
%defattr(644,root,root,755)
%doc src/ld65/cfg/c128.cfg
%{_libdir}/%{name}/lib/c128.lib
%{_libdir}/%{name}/lib/c128.o
%{_libdir}/%{name}/emd/c128-*.emd
%{_libdir}/%{name}/tgi/c128-*.tgi

%files atari
%defattr(644,root,root,755)
%doc src/ld65/cfg/atari.cfg
%{_libdir}/%{name}/lib/atari.lib
%{_libdir}/%{name}/lib/atari.o

%files plus4
%defattr(644,root,root,755)
%doc src/ld65/cfg/plus4.cfg
%{_libdir}/%{name}/lib/plus4.lib
%{_libdir}/%{name}/lib/plus4.o

%files pet
%defattr(644,root,root,755)
%doc src/ld65/cfg/pet.cfg
%{_libdir}/%{name}/lib/pet.lib
%{_libdir}/%{name}/lib/pet.o

%files cbm510
%defattr(644,root,root,755)
%doc src/ld65/cfg/cbm510.cfg
%{_libdir}/%{name}/lib/cbm510.lib
%{_libdir}/%{name}/lib/cbm510.o
%{_libdir}/%{name}/emd/cbm510-*.emd

%files cbm610
%defattr(644,root,root,755)
%doc src/ld65/cfg/cbm610.cfg
%{_libdir}/%{name}/lib/cbm610.lib
%{_libdir}/%{name}/lib/cbm610.o
%{_libdir}/%{name}/emd/cbm610-*.emd

%files apple2
%defattr(644,root,root,755)
%doc src/ld65/cfg/apple2.cfg
%{_libdir}/%{name}/lib/apple2.lib
%{_libdir}/%{name}/lib/apple2.o
%{_libdir}/%{name}/emd/a2.*.emd
%{_libdir}/%{name}/tgi/a2.*.tgi

%files atmos
%defattr(644,root,root,755)
%doc src/ld65/cfg/atmos.cfg
%{_libdir}/%{name}/lib/atmos.lib
%{_libdir}/%{name}/lib/atmos.o

%files geos
%defattr(644,root,root,755)
%doc src/ld65/cfg/geos.cfg
%attr(755,root,root) %{_bindir}/grc
%{_libdir}/%{name}/lib/geos.lib
%{_libdir}/%{name}/lib/geos.o
%dir %{_libdir}/%{name}/include/geos
%{_libdir}/%{name}/include/geos/*.h
%{_libdir}/%{name}/emd/geos-*.emd
%{_libdir}/%{name}/tgi/geos-*.tgi

%files nes
%defattr(644,root,root,755)
%doc src/ld65/cfg/nes.cfg
%{_libdir}/%{name}/lib/nes.lib
%{_libdir}/%{name}/lib/nes.o

%files supervision
%defattr(644,root,root,755)
%doc src/ld65/cfg/supervision*.cfg
%{_libdir}/%{name}/lib/supervision.lib
%{_libdir}/%{name}/lib/supervision.o
