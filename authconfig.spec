Summary:	Text-mode tool for setting up NIS and shadow passwords.
Name:		authconfig
Version:	1.7
Release:	3
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

mv $RPM_BUILD_ROOT%{_mandir} $RPM_BUILD_ROOT/usr/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/sbin/authconfig

%lang(hu) /usr/share/locale/hu/LC_MESSAGES/authconfig.mo
%lang(in) /usr/share/locale/in/LC_MESSAGES/authconfig.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/authconfig.mo
%lang(sk) /usr/share/locale/sk/LC_MESSAGES/authconfig.mo

%{_mandir}/man8/*

%changelog
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

* Thu Apr 01 1999 Preston Brown <pbrown@redhat.com>
- don't report errors about NIS fields not being filled in if not enabled

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- fix typo
- change domainname at nis start and stop

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- fixed man page

* Wed Mar 17 1999 Matt Wilson <msw@redhat.com>
- fixed rewriting /etc/yp.conf
- restarts ypbind so that new changes take effect

* Mon Mar 15 1999 Matt Wilson <msw@redhat.com>
- just make the NIS part of configuration grayed out if NIS is not installed

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- static buffer sizes increased.

* Tue Mar  9 1999 Matt Wilson <msw@redhat.com>
- removed build opts because of problems on alpha

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- Don't rewrite ypbind.conf if you're not configuring NIS

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- Don't configure NIS if /etc/ypbind.conf does not exist.

* Sat Feb  6 1999 Matt Wilson <msw@redhat.com>
- changed "/sbin/chkconfig --add ypbind" to
  "/sbin/chkconfig --level 345 ypbind on"
- added checks for null nis domains and servers if nis is enabled or if
  not using broadcast.
- added newt entry filter for spaces in domains

* Sat Feb  6 1999 Matt Wilson <msw@redhat.com>
- changed command line options to match user interface
- added --help

* Thu Feb  4 1999 Matt Wilson <msw@redhat.com>
- Rewrote UI to handle geometry management properly
- MD5 passwords do not require shadow passwords, so made them independent

* Wed Feb 03 1999 Preston Brown <pbrown@redhat.com>
- initial spec file
