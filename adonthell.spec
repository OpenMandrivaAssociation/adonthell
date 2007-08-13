%define	name	adonthell
%define	version	0.3.4
%define	cvs	cvs.20050813
%define	rel	3
%define release	%mkrel %{rel}

Summary:	A 2D graphical RPG game
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Adventure
Source0:	adonthell_%{version}.%{cvs}.orig.tar.gz
#Patch0:		adonthell-0.3.4-gcc4-fix.patch
Patch1:		adonthell_0.3.4.cvs.20050813-2.4ubuntu2.diff.gz
Patch2:		01_work_around_bug_381456.diff
Patch3:		02_use_libsdl-ttf.diff
Patch4:		03_use_libsdl-mixer.diff
Patch5:		04_python2.5.diff
URL:		http://adonthell.linuxgames.com/
BuildRequires:	oggvorbis-devel SDL-devel python-devel zlib-devel swig
BuildRequires:	SDL_mixer-devel SDL_ttf-devel
BuildRequires:	gpm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A 2D, graphical, single player role playing game inspired by good old 
console RPGs from the SNES like Secret of Mana or Chrono Trigger. 

This package contains the Adonthell engine. You will also need a game
package to play Adonthell. For this release, the official package is 
Waste's Edge.

%prep
%setup -q -n %{name}-%{version}.%{cvs}
#%patch0 -p1 -b .gcc4
%patch1 -p1 -b .ubuntu
%patch2 -p1 -b .workaround
%patch3 -p1 -b .sdl_ttf
%patch4 -p1 -b .sdl_mixer
%patch5 -p1 -b .py2.5

%build
#./autogen.sh
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--with-py-libs=-lpython%{python_version} \
		--with-py-cflags=-I/usr/include/python%{python_version}
#(perovyind) -O2 causes problems during linking for some reason..
%make CXXFLAGS="%{optflags} -O2 -fno-exceptions -DDATA_DIR=\"\\\"/usr/share/games/adonthell\"\\\"" LDFLAGS="-lSDL_ttf"

%install
rm -rf %{buildroot}
%makeinstall_std
install -m644 src/modules/adonthell.py -D %{buildroot}%{_gamesdatadir}/%{name}/modules/adonthell.py
install -m644 src/modules/dialogue.py -D %{buildroot}%{_gamesdatadir}/%{name}/modules/dialogue.py

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS ChangeLog NEWS FULLSCREEN.howto README
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*

