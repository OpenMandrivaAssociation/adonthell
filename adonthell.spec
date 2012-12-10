#define debug_package %{nil}

%define	name	adonthell
%define	version	0.3.5
%define	rel	2
%define release	%{rel}

Summary:		A 2D graphical RPG game
Name:		%{name}
Version:		%{version}
Release:		%{release}
License:		GPLv2+
Group:		Games/Adventure
Source0:		adonthell-src-%{version}.tar.gz
Patch0:		adonthell-src-0.3.5-fix-str-fmt.patch
Patch1:		adonthell-0.3.5-glibc-2.10.patch
Patch2:		adonthell-0.3.5-configure.in.patch
Patch3:		adonthell-0.3.5-gcc-4.7.patch
URL:		http://adonthell.linuxgames.com/
BuildRequires:	pkgconfig(vorbis) 
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(python) 
BuildRequires:	pkgconfig(zlib)
BuildRequires:	swig
BuildRequires:	pkgconfig(SDL_mixer) 
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	gpm-devel 


%description
A 2D, graphical, single player role playing game inspired by good old 
console RPGs from the SNES like Secret of Mana or Chrono Trigger. 

This package contains the Adonthell engine. You will also need a game
package to play Adonthell. For this release, the official package is 
Waste's Edge.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p1

# Set default screen-mode to fullscreen
sed 's|screen_mode = 0|screen_mode = 1|g' -i src/prefs.cc

%build
autoreconf -fi
export CXXFLAGS="%{optflags} -O2 -fno-exceptions"
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make


%install
%makeinstall_std
install -m644 src/modules/adonthell.py -D %{buildroot}%{_gamesdatadir}/%{name}/modules/adonthell.py
install -m644 src/modules/dialogue.py -D %{buildroot}%{_gamesdatadir}/%{name}/modules/dialogue.py

%post
echo Set default screen-mode to fullscreen

#no language files
#find_lang  %{name} 


%files 
%doc ABOUT-NLS ChangeLog NEWS FULLSCREEN.howto README
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}-0.3
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*


%changelog
* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.3.5-2mdv2010.1
+ Revision: 508015
- add gentoo patches to make it build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jan 22 2009 Funda Wang <fwang@mandriva.org> 0.3.5-1mdv2009.1
+ Revision: 332432
- fix str fmt

* Sun Aug 10 2008 Emmanuel Andry <eandry@mandriva.org> 0.3.5-1mdv2009.0
+ Revision: 270333
- New version
- drop patches

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.3.4-3mdv2009.0
+ Revision: 135817
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Nicolas Vigier <nvigier@mandriva.com>
    - update license tag

* Mon Aug 13 2007 Nicolas Vigier <nvigier@mandriva.com> 0.3.4-3mdv2008.0
+ Revision: 62677
- rebuild for new python (fix bug #30942)
- add buildrequires on gpm-devel

  + Per Ã?yvind Karlsen <peroyvind@mandriva.org>
    - fix python detection
    - sync with ubuntu/debian patches to fix python2.5/swig, use of SDL_mixer & SDL_ttf etc.
    - fix build with gcc >= 4 (P0)


* Thu Apr 21 2005 Per Ã?yvind Karlsen <peroyvind@linux-mandrake.com> 0.3.4-1mdk
- 0.3.4 (fixes #15557)
- reduce optimizations
- drop P0 & P1
- fix summary-ended-with-dot

* Wed Feb 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.3-4mdk
- fix buildrequires for lib64
- use %%makeinstall_std macro
- don't manually strip binary in %%install

* Fri Aug 08 2003 Per Ã?yvind Karlsen <peroyvind@linux-mandrake.com> 0.3.3-3mdk
- rebuild for new perl

* Tue Mar 11 2003 Per Ã?yvind Karlsen <peroyvind@sintrax.net> 0.3.3-2mdk
- Added zlib-devel to BuildRequires

* Thu Nov 14 2002 Per Ã?yvind Karlsen <peroyvind@sintrax.net> 0.3.3-1mdk
- First mdk release

