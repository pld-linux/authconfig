Summary:	Text-mode tool for setting up NIS and shadow passwords.
Name:		authconfig
Version:	1.7
Release:	4
Copyright:	GPL
ExclusiveOS:	Linux
Group:		Base
Group(pl):	Podstawy
Source:		%{name}-%{version}.tar.gz
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

%build
make CFLAGS="-DVERSION=\"${VERSION}\" $RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
make INSTROOT=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

mv $RPM_BUILD_ROOT%{_mandir} $RPM_BUILD_ROOT%{_datadir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/authconfig

%changelog
* Mon May 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7-4]
- added using %%find_lang macro.

* Fri May 14 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7-3]
- now package is FHS 2.0 compliant.

* Wed Apr 28 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7-2]
- uncommented .mo files and added %lang macros for this files,
- gzippen man page,
- Group changed to Base,
- added BuildPrereq rules,
- added "rm -rf $RPM_BUILD_ROOT" on top %install.

Spec based on RH version.
