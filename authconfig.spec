Summary:	Text-mode tool for setting up NIS and shadow passwords.
Name:		authconfig
Version:	1.7
Release:	4
Copyright:	GPL
ExclusiveOS:	Linux
Group:		Base
Group(pl):	Podstawowe
Source:		%{name}-%{version}.tar.gz
Patch:		authconfig-make.patch
BuildPrereq:	newt-devel
BuildPrereq:	popt-devel
BuildPrereq:	slang-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description 
Authconfig is a terminal mode program for setting up Network Information
Service (NIS) and shadow (more secure) passwords on your system. Authconfig
also configures the system to automatically turn on NIS at system startup.

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
