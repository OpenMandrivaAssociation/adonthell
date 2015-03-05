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
BuildRequires:	pkgconfig(python2) 
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
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH

sed '/^ *for ac_prog in / s|python|python2|' -i configure

%configure	--bindir=%{_gamesbindir} \
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
