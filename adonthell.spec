%define	name	adonthell
%define	version	0.3.4
%define	rel	1
%define release	%mkrel %{rel}

Summary:	A 2D graphical RPG game
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Adventure
Source0:	http://freesoftware.fsf.org/download/adonthell/%{name}-src-%{version}.tar.bz2
URL:		http://adonthell.linuxgames.com/
BuildRequires:	oggvorbis-devel SDL-devel python-devel zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A 2D, graphical, single player role playing game inspired by good old 
console RPGs from the SNES like Secret of Mana or Chrono Trigger. 

This package contains the Adonthell engine. You will also need a game
package to play Adonthell. For this release, the official package is 
Waste's Edge.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
#(perovyind) -O2 causes problems during linking for some reason..
%make CXXFLAGS="$RPM_OPT_FLAGS -O1 -fno-exceptions -DDATA_DIR=\"\\\"/usr/share/games/adonthell\"\\\""

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
install -m644 src/modules/adonthell.py $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/modules/adonthell.py
install -m644 src/modules/dialogue.py $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/modules/dialogue.py

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS ChangeLog NEWS FULLSCREEN.howto README
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*

