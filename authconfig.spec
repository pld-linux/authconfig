Summary:	Text-mode tool for setting up NIS and shadow passwords.
Summary(de):	Textmodus-Tool, um NIS und shadow-Passwoerter zu konfigurieren
Summary(pl):	Narzêdzie do ustawiania przes³oniêtych hase³ oraz NIS.
Name:		authconfig
Version:	2.0
Release:	3
Copyright:	GPL
ExclusiveOS:	Linux
Group:		Base
Group(pl):	Podstawowe
Source:		%{name}-%{version}.tar.gz
Patch:		authconfig-make.patch
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	slang-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description 
Authconfig is a terminal mode program for setting up Network Information
Service (NIS) and shadow (more secure) passwords on your system. Authconfig
also configures the system to automatically turn on NIS at system startup.

%description -l de
Authconfig ist ein Textmodus-Programm, um Network Informations-Services
(NIS) und Shadow (sicherere) Passwörter auf Ihren System zu konfigurieren. 
Authconfig kann außerdem anschalten, daß NIS beim Systemstart angeschaltet
wird.

%description -l pl
Authconfig jest terminalowym programem dla ustawiania NIS (Network Information
Service) oraz przes³onietych (bardziej bezpiecznych) hase³ w Twoim systemie.
Authconfig dodatkowo konfiguruje system tak by NIS by³ aktywowany przy
starcie systemu.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="-DVERSION=\"${VERSION}\" $RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
make INSTROOT=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/authconfig
%{_mandir}/man8/*
