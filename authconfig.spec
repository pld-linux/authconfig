Summary:	Text-mode tool for setting up NIS and shadow passwords
Summary(de.UTF-8):	Textmodus-Tool, um NIS und shadow-Passwoerter zu konfigurieren
Summary(es.UTF-8):	Herramienta de interfaz texto para configuración de contraseñas shadow y NIS
Summary(ja.UTF-8):	NIS とシャドーパスワードを設定するためのテキストモードのツール。
Summary(pl.UTF-8):	Narzędzie do ustawiania przesłoniętych haseł oraz NIS
Summary(pt_BR.UTF-8):	Ferramenta de interface texto para configuração de senhas shadow e NIS
Summary(ru.UTF-8):	Утилита текстового режима для настройки shadow и NIS-паролей
Summary(uk.UTF-8):	Утиліта текстового режиму для налагодження shadow та NIS-паролів
Name:		authconfig
Version:	6.2.2
Release:	0.5
License:	GPL v2+
Group:		Base
Source0:	https://fedorahosted.org/releases/a/u/authconfig/%{name}-%{version}.tar.bz2
# Source0-md5:	13feaa9de8ddd93fde618415bf3aec75
Patch0:		libs-resolv.patch
URL:		https://fedorahosted.org/authconfig
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	newt-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	slang-devel >= 2.0.0
#Requires:	libpwquality > 0.9
Requires:	pam >= 0.99.10.0
Requires:	python
Requires:	python-snack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authconfig is a terminal mode program for setting up Network
Information Service (NIS) and shadow (more secure) passwords on your
system. Authconfig also configures the system to automatically turn on
NIS at system startup.

%description -l de.UTF-8
Authconfig ist ein Textmodus-Programm, um Network
Informations-Services (NIS) und Shadow (sicherere) Passwörter auf
Ihren System zu konfigurieren. Authconfig kann außerdem anschalten,
daß NIS beim Systemstart angeschaltet wird.

%description -l es.UTF-8
Authconfig es un programa de interfaz de texto para configurar NIS y
contraseñas shadow en el sistema. El programa authconfig también puede
inicializar NIS cuando se arranca el sistema.

%description -l ja.UTF-8
authconfig はシステムに Network Information Service (NIS) とシャドー
(よりセキュリティーが高い)パスワードのセッティングをする端末モードの
プログラムです。authconfig はまたシステム起動時に自動的に NIS を
オンにするようにシステムを設定できます。

%description -l pl.UTF-8
Authconfig jest terminalowym programem dla ustawiania NIS (Network
Information Service) oraz przesłoniętych (bardziej bezpiecznych) haseł
w Twoim systemie. Authconfig dodatkowo konfiguruje system tak by NIS
był aktywowany przy starcie systemu.

%description -l pt_BR.UTF-8
O authconfig é um programa de interface texto para configurar o NIS e
senhas shadow no seu sistema. O authconfig também pode inicializar o
NIS no boot do sistema.

%description -l ru.UTF-8
Authconfig - это терминальная программа для настройки Network
Information Service (NIS) и shadow (более безопасных) паролей в вашей
системе. Authconfig также настраивает систему на автоматический запуск
NIS при старте системы.

%description -l uk.UTF-8
Authconfig - це термінальна програма для налагодження Network
Information Service (NIS) та shadow (більш безпечних) паролів у вашій
системі. Authconfig також конфігурує систему для автоматичного запуску
NIS при старті системи.

%package gtk
Summary:	Graphical tool for setting up authentication from network services
Group:		Base
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	python-pygtk-glade >= 2.14.0
Requires:	usermode-gtk

%description gtk
Authconfig-gtk is a GUI program which can configure a workstation to
use shadow (more secure) passwords. Authconfig-gtk can also configure
a system to be a client for certain networked user information and
authentication schemes.

%prep
%setup -q
%patch0 -p1

#mv po/sr{,@latin}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -fPIC"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/bal

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/acutilmodule.a
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/acutilmodule.la

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/authconfig-tui.py
ln -s authconfig.py $RPM_BUILD_ROOT%{_datadir}/%{name}/authconfig-tui.py

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post gtk
%update_icon_cache_post hicolor

%postun gtk
%update_icon_cache_post hicolor

%triggerin -- authconfig <= 5.4.9
authconfig --update --nostart >/dev/null 2>&1 || :

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NOTES TODO README.samba3
%ghost %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/authconfig
%ghost %config(noreplace) /etc/pam.d/system-auth-ac
%ghost %config(noreplace) /etc/pam.d/password-auth-ac
%ghost %config(noreplace) /etc/pam.d/fingerprint-auth-ac
%ghost %config(noreplace) /etc/pam.d/smartcard-auth-ac
%ghost %config(noreplace) /etc/pam.d/postlogin-ac
%attr(755,root,root) %{_sbindir}/cacertdir_rehash
%attr(755,root,root) %{_sbindir}/authconfig
%attr(755,root,root) %{_sbindir}/authconfig-tui
%attr(755,root,root) %{py_sitedir}/acutilmodule.so
%{_mandir}/man8/*
%{_mandir}/man5/*
%exclude %{_mandir}/man8/system-config-authentication.*
%exclude %{_mandir}/man8/authconfig-gtk.*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/authconfig.py
%{_datadir}/%{name}/authconfig-tui.py*
%{_datadir}/%{name}/authinfo.py*
%{_datadir}/%{name}/shvfile.py*
%{_datadir}/%{name}/dnsclient.py*
%{_datadir}/%{name}/msgarea.py*
%attr(700,root,root) %dir %{_localstatedir}/lib/%{name}

%files gtk
%defattr(644,root,root,755)
%config(noreplace) /etc/pam.d/authconfig
%config(noreplace) /etc/pam.d/authconfig-gtk
%config(noreplace) /etc/pam.d/authconfig-tui
%config(noreplace) /etc/pam.d/system-config-authentication
%config(noreplace) /etc/security/console.apps/authconfig
%config(noreplace) /etc/security/console.apps/authconfig-gtk
%config(noreplace) /etc/security/console.apps/authconfig-tui
%config(noreplace) /etc/security/console.apps/system-config-authentication
%attr(755,root,root) %{_bindir}/authconfig
%attr(755,root,root) %{_bindir}/authconfig-gtk
%attr(755,root,root) %{_bindir}/authconfig-tui
%attr(755,root,root) %{_bindir}/system-config-authentication
%attr(755,root,root) %{_sbindir}/authconfig-gtk
%attr(755,root,root) %{_sbindir}/system-config-authentication
%{_mandir}/man8/system-config-authentication.*
%{_mandir}/man8/authconfig-gtk.*
%{_datadir}/%{name}/authconfig.glade
%{_datadir}/%{name}/authconfig-gtk.py*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/system-config-authentication.*
