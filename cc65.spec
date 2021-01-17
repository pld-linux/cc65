Summary:	Crosscompiler/crossassembler for 6502 systems
Summary(pl.UTF-8):	Kompilator/asembler skrośny dla systemów 6502
Name:		cc65
Version:	2.19
Release:	1
License:	Zlib
Group:		Development/Languages
#Source0Download: https://github.com/cc65/cc65/releases
Source0:	https://github.com/cc65/cc65/archive/V%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	faff7b71a0212bb71faad1a271a83916
Patch0:		%{name}-verbose.patch
URL:		https://cc65.github.io/
BuildRequires:	linuxdoc-tools
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.752
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
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description apple2
This package contains the header files and libraries needed to write
programs for the Apple ][ using the cc65 crosscompiler.

%description apple2 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Apple ][ korzystając z kompilatora skrośnego cc65.

%package apple2enh
Summary:	Apple //e specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Apple //e biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-apple = %{version}-%{release}
%{?noarchpackage}

%description apple2enh
This package contains the header files and libraries needed to write
programs for the Apple //e using the cc65 crosscompiler.

%description apple2enh -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Apple //e korzystając z kompilatora skrośnego cc65.

%package atari
Summary:	Atari specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Atari biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

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
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description atmos
This package contains the header files and libraries needed to write
programs for the Oric Atmos using the cc65 crosscompiler.

%description atmos -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Oric Atmos korzystając z kompilatora skrośnego cc65.

%package cbm
Summary:	Development files common for Commodore Business Machines targets
Summary(pl.UTF-8):	Pliki programistyczne wspólne dla platform Commodore Business Machines
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description cbm
Development files common for Commodore Business Machines (and
compatible) targets: c16, c64, c128, cbm510, cbm610, cx16, plus4, pet,
vic20.

%description cbm -l pl.UTF-8
Pliki programistyczne wspólne dla platform Commodore Business Machines
(i kompatybilnych): c16, c64, c128, cbm510, cbm610, cx16, plus4, pet,
vic20.

%package c16
Summary:	C16/116 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla C16/116 biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

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
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

%description c64
This package contains the header files and libraries needed to write
programs for the Commodore C64 using the cc65 crosscompiler.

%description c64 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore C64 korzystając z kompilatora skrośnego cc65.

%package c128
Summary:	C128 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla C128 biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

%description c128
This package contains the header files and libraries needed to write
programs for the Commodore C128 using the cc65 crosscompiler.

%description c128 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore C128 korzystając z kompilatora skrośnego cc65.

%package cbm510
Summary:	CBM 510 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla CBM 510 biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

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
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

%description cbm610
This package contains the header files and libraries needed to write
programs for the Commodore PET-II (CBM600/700) using the cc65
crosscompiler.

%description cbm610 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore PET-II (CBM600/700) korzystając z kompilatora
skrośnego cc65.

%package pet
Summary:	PET specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla PET biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

%description pet
This package contains the header files and libraries needed to write
programs for the Commodore PET using the cc65 crosscompiler.

%description pet -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore PET korzystając z kompilatora skrośnego cc65.

%package plus4
Summary:	Plus/4 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Plus/4 biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

%description plus4
This package contains the header files and libraries needed to write
programs for the Commodore Plus/4 and C16/116 using the cc65
crosscompiler.

%description plus4 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore Plus/4 i C16/116 korzystając z kompilatora
skrośnego cc65.

%package vic20
Summary:	VIC20 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla VIC20 biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

%description vic20
This package contains the header files and libraries needed to write
programs for the Commodore VIC20 using the cc65 crosscompiler.

%description vic20 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Commodore VIC20 korzystając z kompilatora skrośnego
cc65.

%package cx16
Summary:	Commander X16 specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla platformy Commander X16 biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name}-cbm = %{version}-%{release}
%{?noarchpackage}

%description cx16
This package contains the header files and libraries needed to write
programs for the Commander X16 computer using the cc65 crosscompiler.

%description cx16 -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla komputera Commander X16 korzystając z kompilatora
skrośnego cc65.

%package geos
Summary:	GEOS specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla GEOS biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description geos
This package contains the header files and libraries needed to write
GEOS programs for the C64/C128 or Apple II using the cc65
crosscompiler.

%description geos -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów GEOS dla C64/C128 lub Apple II korzystając z kompilatora
skrośnego cc65.

%package creativision
Summary:	VTech CreatiVision specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla VTech CreatiVision biblioteki dla kompilatora cc65
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description creativision
This package contains the libraries needed to write programs for the
VTech CreatiVision platform using the cc65 crosscompiler.

%description creativision -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla platformy
VTech CreatiVision korzystając z kompilatora skrośnego cc65.

%package gamate
Summary:	Gamate specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla konsoli Gamate biblioteki dla kompilatora cc65
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description gamate
This package contains the libraries needed to write programs for the
Gamate console using the cc65 crosscompiler.

%description gamate -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla konsoli
Gamate korzystając z kompilatora skrośnego cc65.

%package lynx
Summary:	Atari Lynx specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla konsoli Atari Lynx biblioteki dla cc65
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description lynx
This package contains the libraries needed to write programs for the
Atari Lynx console using the cc65 crosscompiler.

%description lynx -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla konsoli
Atari Lynx korzystając z kompilatora skrośnego cc65.

%package nes
Summary:	NES (Nintendo Entertainment System) specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla NES (Nintendo Entertainment System) biblioteki dla cc65
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description nes
This package contains the libraries needed to write programs for the
NES (Nintendo Entertainment System) using the cc65 crosscompiler.

%description nes -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla NES
(Nintendo Entertainment System) korzystając z kompilatora skrośnego
cc65.

%package osic1p
Summary:	Ohio Scientific Challenger 1P specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Ohio Scientific Challenger 1P biblioteki dla kompilatora cc65
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description osic1p
This package contains the libraries needed to write programs for the
Ohio Scientific Challenger 1P computers using the cc65 crosscompiler.

%description osic1p -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla
komputerów Watara Supervision korzystając z kompilatora skrośnego
cc65.

%package pce
Summary:	NEC PC-Engine specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla NEC PC-Engine biblioteki dla kompilatora cc65
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description pce
This package contains the libraries needed to write programs for the
NEC PC-Engine console using the cc65 crosscompiler.

%description pce -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla konsoli
NEC PC-Engine korzystając z kompilatora skrośnego cc65.

%package supervision
Summary:	Watara Supervision specific libraries for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Watara Supervision biblioteki dla kompilatora cc65
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description supervision
This package contains the libraries needed to write programs for the
Watara Supervision console using the cc65 crosscompiler.

%description supervision -l pl.UTF-8
Pakiet zawiera biblioteki potrzebne do pisania programów dla konsoli
Watara Supervision korzystając z kompilatora skrośnego cc65.

%package telestrat
Summary:	Oric Telestrat specific libraries and headers for the cc65 compiler
Summary(pl.UTF-8):	Specyficzne dla Oric Telestrat biblioteki i pliki nagłówkowe
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?noarchpackage}

%description telestrat
This package contains the header files and libraries needed to write
programs for the Oric Telestrat using the cc65 crosscompiler.

%description telestrat -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do pisania
programów dla Oric Telestrat korzystając z kompilatora skrośnego cc65.

%package doc
Summary:	CC65 suite documentation in HTML format and examples
Summary(pl.UTF-8):	Dokumentacja w formacie HTML oraz przykłady do pakietu programistycznego CC65
Group:		Documentation
%{?noarchpackage}

%description doc
CC65 suite documentation in HTML format and examples.

%description doc -l pl.UTF-8
Dokumentacja w formacie HTML oraz przykłady do pakietu
programistycznego CC65.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	USER_CFLAGS="%{rpmcflags} %{rpmcppflags}"

%{__make} html

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

# move to PLD standard place
install -d $RPM_BUILD_ROOT%{_examplesdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/cc65

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
# doc/{BUGS,CREDITS,compile.txt,internal.txt,newvers.txt,readme.1st} doc/*.html announce.txt
%attr(755,root,root) %{_bindir}/ar65
%attr(755,root,root) %{_bindir}/ca65
%attr(755,root,root) %{_bindir}/cc65
%attr(755,root,root) %{_bindir}/chrcvt65
%attr(755,root,root) %{_bindir}/cl65
%attr(755,root,root) %{_bindir}/co65
%attr(755,root,root) %{_bindir}/da65
%attr(755,root,root) %{_bindir}/ld65
%attr(755,root,root) %{_bindir}/od65
%attr(755,root,root) %{_bindir}/sim65
%attr(755,root,root) %{_bindir}/sp65
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/asminc
%{_datadir}/%{name}/asminc/_file.inc
%{_datadir}/%{name}/asminc/_heap.inc
%{_datadir}/%{name}/asminc/cpu.mac
%{_datadir}/%{name}/asminc/ctype.inc
%{_datadir}/%{name}/asminc/ctype_common.inc
%{_datadir}/%{name}/asminc/ctypetable.inc
%{_datadir}/%{name}/asminc/em-error.inc
%{_datadir}/%{name}/asminc/em-kernel.inc
%{_datadir}/%{name}/asminc/errno.inc
%{_datadir}/%{name}/asminc/fcntl.inc
%{_datadir}/%{name}/asminc/generic.mac
%{_datadir}/%{name}/asminc/get_tv.inc
%{_datadir}/%{name}/asminc/joy-error.inc
%{_datadir}/%{name}/asminc/joy-kernel.inc
%{_datadir}/%{name}/asminc/longbranch.mac
%{_datadir}/%{name}/asminc/modload.inc
%{_datadir}/%{name}/asminc/module.mac
%{_datadir}/%{name}/asminc/mouse-kernel.inc
%{_datadir}/%{name}/asminc/o65.inc
%{_datadir}/%{name}/asminc/opcodes.inc
%{_datadir}/%{name}/asminc/ser-error.inc
%{_datadir}/%{name}/asminc/ser-kernel.inc
%{_datadir}/%{name}/asminc/signal.inc
%{_datadir}/%{name}/asminc/smc.inc
%{_datadir}/%{name}/asminc/stdio.inc
%{_datadir}/%{name}/asminc/tgi-error.inc
%{_datadir}/%{name}/asminc/tgi-kernel.inc
%{_datadir}/%{name}/asminc/tgi-vectorfont.inc
%{_datadir}/%{name}/asminc/time.inc
%{_datadir}/%{name}/asminc/utsname.inc
%{_datadir}/%{name}/asminc/zeropage.inc
%dir %{_datadir}/%{name}/cfg
%{_datadir}/%{name}/cfg/bbc.cfg
%{_datadir}/%{name}/cfg/lunix.cfg
%{_datadir}/%{name}/cfg/module.cfg
%{_datadir}/%{name}/cfg/none.cfg
%{_datadir}/%{name}/cfg/sim6502.cfg
%{_datadir}/%{name}/cfg/sim65c02.cfg
%dir %{_datadir}/%{name}/include
%{_datadir}/%{name}/include/6502.h
%{_datadir}/%{name}/include/_heap.h
%{_datadir}/%{name}/include/ascii_charmap.h
%{_datadir}/%{name}/include/assert.h
%{_datadir}/%{name}/include/inttypes.h
%{_datadir}/%{name}/include/iso646.h
%{_datadir}/%{name}/include/joystick.h
%{_datadir}/%{name}/include/limits.h
%{_datadir}/%{name}/include/locale.h
%{_datadir}/%{name}/include/cc65.h
%{_datadir}/%{name}/include/conio.h
%{_datadir}/%{name}/include/ctype.h
%{_datadir}/%{name}/include/dbg.h
%{_datadir}/%{name}/include/device.h
%{_datadir}/%{name}/include/dio.h
%{_datadir}/%{name}/include/dirent.h
%{_datadir}/%{name}/include/em.h
%{_datadir}/%{name}/include/errno.h
%{_datadir}/%{name}/include/fcntl.h
%{_datadir}/%{name}/include/lz4.h
%{_datadir}/%{name}/include/modload.h
%{_datadir}/%{name}/include/mouse.h
%{_datadir}/%{name}/include/o65.h
%{_datadir}/%{name}/include/peekpoke.h
%{_datadir}/%{name}/include/pen.h
%{_datadir}/%{name}/include/serial.h
%{_datadir}/%{name}/include/setjmp.h
%{_datadir}/%{name}/include/signal.h
%{_datadir}/%{name}/include/stdarg.h
%{_datadir}/%{name}/include/stdbool.h
%{_datadir}/%{name}/include/stddef.h
%{_datadir}/%{name}/include/stdint.h
%{_datadir}/%{name}/include/stdio.h
%{_datadir}/%{name}/include/stdlib.h
%{_datadir}/%{name}/include/string.h
%{_datadir}/%{name}/include/target.h
%{_datadir}/%{name}/include/tgi.h
%{_datadir}/%{name}/include/time.h
%{_datadir}/%{name}/include/unistd.h
%{_datadir}/%{name}/include/zlib.h
%{_datadir}/%{name}/include/em
%{_datadir}/%{name}/include/joystick
%{_datadir}/%{name}/include/mouse
%{_datadir}/%{name}/include/sys
%{_datadir}/%{name}/include/tgi
# common for atmos, cbm (cx16,pet,vic20), telestrat
%{_datadir}/%{name}/include/_6522.h
# common for atari, cbm (pet)
%{_datadir}/%{name}/include/_pia.h
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/none.lib
%{_datadir}/%{name}/lib/sim6502.lib
%{_datadir}/%{name}/lib/sim65c02.lib
%dir %{_datadir}/%{name}/target

%files apple2
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/apple2.inc
%{_datadir}/%{name}/asminc/apple2.mac
%{_datadir}/%{name}/cfg/apple2.cfg
%{_datadir}/%{name}/cfg/apple2-asm.cfg
%{_datadir}/%{name}/cfg/apple2-hgr.cfg
%{_datadir}/%{name}/cfg/apple2-overlay.cfg
%{_datadir}/%{name}/cfg/apple2-system.cfg
%{_datadir}/%{name}/include/apple2.h
%{_datadir}/%{name}/include/apple2_filetype.h
%{_datadir}/%{name}/lib/apple2.lib
%{_datadir}/%{name}/lib/apple2-iobuf-0800.o
%{_datadir}/%{name}/target/apple2

%files apple2enh
%defattr(644,root,root,755)
%{_datadir}/%{name}/cfg/apple2enh.cfg
%{_datadir}/%{name}/cfg/apple2enh-asm.cfg
%{_datadir}/%{name}/cfg/apple2enh-hgr.cfg
%{_datadir}/%{name}/cfg/apple2enh-overlay.cfg
%{_datadir}/%{name}/cfg/apple2enh-system.cfg
%{_datadir}/%{name}/include/apple2enh.h
%{_datadir}/%{name}/lib/apple2enh.lib
%{_datadir}/%{name}/lib/apple2enh-iobuf-0800.o
%{_datadir}/%{name}/target/apple2enh

%files atari
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/atari.inc
%{_datadir}/%{name}/asminc/atari.mac
%{_datadir}/%{name}/asminc/atari2600.inc
%{_datadir}/%{name}/asminc/atari2600_riot.inc
%{_datadir}/%{name}/asminc/atari2600_tia.inc
%{_datadir}/%{name}/asminc/atari5200.inc
%{_datadir}/%{name}/asminc/atari_antic.inc
%{_datadir}/%{name}/asminc/atari_gtia.inc
%{_datadir}/%{name}/asminc/atari_pokey.inc
%{_datadir}/%{name}/cfg/atari.cfg
%{_datadir}/%{name}/cfg/atari-asm-xex.cfg
%{_datadir}/%{name}/cfg/atari-asm.cfg
%{_datadir}/%{name}/cfg/atari-cart.cfg
%{_datadir}/%{name}/cfg/atari-cassette.cfg
%{_datadir}/%{name}/cfg/atari-overlay.cfg
%{_datadir}/%{name}/cfg/atari-xex.cfg
%{_datadir}/%{name}/cfg/atari2600.cfg
%{_datadir}/%{name}/cfg/atari5200.cfg
%{_datadir}/%{name}/cfg/atarixl.cfg
%{_datadir}/%{name}/cfg/atarixl-largehimem.cfg
%{_datadir}/%{name}/cfg/atarixl-overlay.cfg
%{_datadir}/%{name}/cfg/atarixl-xex.cfg
%{_datadir}/%{name}/include/_antic.h
%{_datadir}/%{name}/include/_atarios.h
%{_datadir}/%{name}/include/_gtia.h
%{_datadir}/%{name}/include/_pbi.h
%{_datadir}/%{name}/include/_pokey.h
%{_datadir}/%{name}/include/_riot.h
%{_datadir}/%{name}/include/_tia.h
%{_datadir}/%{name}/include/atari.h
%{_datadir}/%{name}/include/atari2600.h
%{_datadir}/%{name}/include/atari5200.h
%{_datadir}/%{name}/include/atari_atascii_charmap.h
%{_datadir}/%{name}/include/atari_screen_charmap.h
%{_datadir}/%{name}/lib/atari.lib
%{_datadir}/%{name}/lib/atari2600.lib
%{_datadir}/%{name}/lib/atari5200.lib
%{_datadir}/%{name}/lib/atari5200-conioscreen-20x12.o
%{_datadir}/%{name}/lib/atarixl.lib
%{_datadir}/%{name}/target/atari
%{_datadir}/%{name}/target/atari5200
%{_datadir}/%{name}/target/atarixl

%files atmos
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/atmos.inc
%{_datadir}/%{name}/cfg/atmos.cfg
%{_datadir}/%{name}/include/atmos.h
%{_datadir}/%{name}/lib/atmos.lib
%{_datadir}/%{name}/target/atmos

%files cbm
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/accelerator.inc
%{_datadir}/%{name}/asminc/cbm.mac
%{_datadir}/%{name}/asminc/cbm_filetype.inc
%{_datadir}/%{name}/asminc/cbm_kernal.inc
# cbm510, cbm610
%{_datadir}/%{name}/include/_6525.h
# c64, c128, cbm510, cbm610
%{_datadir}/%{name}/include/_6526.h
# cbm610, pet
%{_datadir}/%{name}/include/_6545.h
# cbm510, cbm610, pet, plus4
%{_datadir}/%{name}/include/_6551.h
# c64, c128, cbm510, cbm610
%{_datadir}/%{name}/include/_sid.h
# c16, plus4
%{_datadir}/%{name}/include/_ted.h
# c64, c128
%{_datadir}/%{name}/include/_vdc.h
# c64, c128, cb510
%{_datadir}/%{name}/include/_vic2.h
%{_datadir}/%{name}/include/accelerator.h
%{_datadir}/%{name}/include/cbm.h
# c16, plus4
%{_datadir}/%{name}/include/cbm264.h
%{_datadir}/%{name}/include/cbm_filetype.h
%{_datadir}/%{name}/include/cbm_petscii_charmap.h
%{_datadir}/%{name}/include/cbm_screen_charmap.h

%files c16
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/c16.inc
%{_datadir}/%{name}/cfg/c16.cfg
%{_datadir}/%{name}/cfg/c16-32k.cfg
%{_datadir}/%{name}/include/c16.h
%{_datadir}/%{name}/lib/c16.lib
%{_datadir}/%{name}/target/c16

%files c64
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/c64.inc
%{_datadir}/%{name}/cfg/c64.cfg
%{_datadir}/%{name}/cfg/c64-asm.cfg
%{_datadir}/%{name}/cfg/c64-overlay.cfg
%{_datadir}/%{name}/include/c64.h
%{_datadir}/%{name}/lib/c64.lib
%{_datadir}/%{name}/lib/c64-soft80.o
%{_datadir}/%{name}/lib/c64-soft80mono.o
%{_datadir}/%{name}/lib/c64-tgimousedata.o
%{_datadir}/%{name}/target/c64

%files c128
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/c128.inc
%{_datadir}/%{name}/cfg/c128.cfg
%{_datadir}/%{name}/cfg/c128-overlay.cfg
%{_datadir}/%{name}/include/c128.h
%{_datadir}/%{name}/lib/c128.lib
%{_datadir}/%{name}/target/c128

%files cbm510
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/cbm510.inc
%{_datadir}/%{name}/cfg/cbm510.cfg
%{_datadir}/%{name}/include/cbm510.h
%{_datadir}/%{name}/lib/cbm510.lib
%{_datadir}/%{name}/target/cbm510

%files cbm610
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/cbm610.inc
%{_datadir}/%{name}/cfg/cbm610.cfg
%{_datadir}/%{name}/include/cbm610.h
%{_datadir}/%{name}/lib/cbm610.lib
%{_datadir}/%{name}/target/cbm610

%files pet
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/pet.inc
%{_datadir}/%{name}/cfg/pet.cfg
%{_datadir}/%{name}/include/pet.h
%{_datadir}/%{name}/lib/pet.lib
%{_datadir}/%{name}/target/pet

%files plus4
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/plus4.inc
%{_datadir}/%{name}/cfg/plus4.cfg
%{_datadir}/%{name}/include/plus4.h
%{_datadir}/%{name}/lib/plus4.lib
%{_datadir}/%{name}/target/plus4

%files vic20
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/vic20.inc
%{_datadir}/%{name}/cfg/vic20.cfg
%{_datadir}/%{name}/cfg/vic20-32k.cfg
%{_datadir}/%{name}/include/_vic.h
%{_datadir}/%{name}/include/vic20.h
%{_datadir}/%{name}/lib/vic20.lib
%{_datadir}/%{name}/target/vic20

%files cx16
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/cx16.inc
%{_datadir}/%{name}/cfg/cx16.cfg
%{_datadir}/%{name}/cfg/cx16-asm.cfg
%{_datadir}/%{name}/cfg/cx16-bank.cfg
%{_datadir}/%{name}/include/cx16.h
%{_datadir}/%{name}/lib/cx16.lib
%{_datadir}/%{name}/target/cx16

%files geos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/grc65
%{_datadir}/%{name}/cfg/geos-apple.cfg
%{_datadir}/%{name}/cfg/geos-cbm.cfg
%{_datadir}/%{name}/include/geos.h
%{_datadir}/%{name}/include/geos
%{_datadir}/%{name}/lib/geos-apple.lib
%{_datadir}/%{name}/lib/geos-cbm.lib
%{_datadir}/%{name}/target/geos-apple
%{_datadir}/%{name}/target/geos-cbm

%files creativision
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/creativision.inc
%{_datadir}/%{name}/cfg/creativision.cfg
%{_datadir}/%{name}/include/creativision.h
%{_datadir}/%{name}/lib/creativision.lib
%{_datadir}/%{name}/target/creativision

%files gamate
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/gamate.inc
%{_datadir}/%{name}/cfg/gamate.cfg
%{_datadir}/%{name}/include/gamate.h
%{_datadir}/%{name}/lib/gamate.lib
%{_datadir}/%{name}/target/gamate

%files lynx
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/lynx.inc
%{_datadir}/%{name}/cfg/lynx.cfg
%{_datadir}/%{name}/cfg/lynx-bll.cfg
%{_datadir}/%{name}/cfg/lynx-coll.cfg
%{_datadir}/%{name}/cfg/lynx-uploader.cfg
%{_datadir}/%{name}/include/_mikey.h
%{_datadir}/%{name}/include/_suzy.h
%{_datadir}/%{name}/include/lynx.h
%{_datadir}/%{name}/lib/lynx.lib
%{_datadir}/%{name}/target/lynx

%files nes
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/nes.inc
%{_datadir}/%{name}/cfg/nes.cfg
%{_datadir}/%{name}/include/nes.h
%{_datadir}/%{name}/lib/nes.lib
%{_datadir}/%{name}/target/nes

%files osic1p
%defattr(644,root,root,755)
%{_datadir}/%{name}/cfg/osic1p.cfg
%{_datadir}/%{name}/cfg/osic1p-asm.cfg
%{_datadir}/%{name}/include/osic1p.h
%{_datadir}/%{name}/lib/osic1p.lib
%{_datadir}/%{name}/lib/osic1p-screen-s3-32x28.o

%files pce
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/pce.inc
%{_datadir}/%{name}/cfg/pce.cfg
%{_datadir}/%{name}/include/pce.h
%{_datadir}/%{name}/lib/pce.lib
%{_datadir}/%{name}/target/pce

%files supervision
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/supervision.inc
%{_datadir}/%{name}/cfg/supervision.cfg
%{_datadir}/%{name}/cfg/supervision-16k.cfg
%{_datadir}/%{name}/cfg/supervision-64k.cfg
%{_datadir}/%{name}/cfg/supervision-128k.cfg
%{_datadir}/%{name}/include/supervision.h
%{_datadir}/%{name}/lib/supervision.lib
%{_datadir}/%{name}/target/supervision

%files telestrat
%defattr(644,root,root,755)
%{_datadir}/%{name}/asminc/telestrat.inc
%{_datadir}/%{name}/cfg/telestrat.cfg
%{_datadir}/%{name}/include/telestrat.h
%{_datadir}/%{name}/lib/telestrat.lib
%{_datadir}/%{name}/target/telestrat

%files doc
%defattr(644,root,root,755)
%doc html/*.html
%{_examplesdir}/%{name}-%{version}
