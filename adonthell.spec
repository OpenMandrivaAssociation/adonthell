%define	name	adonthell
%define	version	0.3.5
%define	rel	2
%define release	%mkrel %{rel}

Summary:	A 2D graphical RPG game
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Games/Adventure
Source0:	adonthell-src-%{version}.tar.gz
Patch0:		adonthell-src-0.3.5-fix-str-fmt.patch
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
%setup -q
%patch0 -p0

%build
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
%{_gamesbindir}/%{name}-0.3
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*

