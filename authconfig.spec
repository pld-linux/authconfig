Summary:	Text-mode tool for setting up NIS and shadow passwords
Summary(de):	Textmodus-Tool, um NIS und shadow-Passwoerter zu konfigurieren
Summary(es):	Herramienta de interfaz texto para configuración de contraseñas shadow y NIS
Summary(ja):	NIS ¤È¥·¥ã¥É¡¼¥Ñ¥¹¥ï¡¼¥É¤òÀßÄê¤¹¤ë¤¿¤á¤Î¥Æ¥­¥¹¥È¥â¡¼¥É¤Î¥Ä¡¼¥ë¡£
Summary(pl):	Narzêdzie do ustawiania przes³oniêtych hase³ oraz NIS
Summary(pt_BR):	Ferramenta de interface texto para configuração de senhas shadow e NIS
Name:		authconfig
Version:	2.0
Release:	4
License:	GPL
ExclusiveOS:	Linux
Group:		Base
Group(de):	Gründsätzlich
Group(es):	Base
Group(pl):	Podstawowe
Group(pt_BR):	Base
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Authconfig is a terminal mode program for setting up Network
Information Service (NIS) and shadow (more secure) passwords on your
system. Authconfig also configures the system to automatically turn on
NIS at system startup.

%description -l de
Authconfig ist ein Textmodus-Programm, um Network
Informations-Services (NIS) und Shadow (sicherere) Passwörter auf
Ihren System zu konfigurieren. Authconfig kann außerdem anschalten,
daß NIS beim Systemstart angeschaltet wird.

%description -l es
authconfig es un programa de interfaz de texto para configurar NIS y
contraseñas shadow en el sistema. El programa authconfig también puede
inicializar NIS cuando se arranca el sistema.

%description -l ja
authconfig ¤Ï¥·¥¹¥Æ¥à¤Ë Network Information Service (NIS) ¤È¥·¥ã¥É¡¼
(¤è¤ê¥»¥­¥å¥ê¥Æ¥£¡¼¤¬¹â¤¤)¥Ñ¥¹¥ï¡¼¥É¤Î¥»¥Ã¥Æ¥£¥ó¥°¤ò¤¹¤ëÃ¼Ëö¥â¡¼¥É¤Î
¥×¥í¥°¥é¥à¤Ç¤¹¡£authconfig ¤Ï¤Þ¤¿¥·¥¹¥Æ¥àµ¯Æ°»þ¤Ë¼«Æ°Åª¤Ë NIS ¤ò
¥ª¥ó¤Ë¤¹¤ë¤è¤¦¤Ë¥·¥¹¥Æ¥à¤òÀßÄê¤Ç¤­¤Þ¤¹¡£

%description -l pl
Authconfig jest terminalowym programem dla ustawiania NIS (Network
Information Service) oraz przes³onietych (bardziej bezpiecznych) hase³
w Twoim systemie. Authconfig dodatkowo konfiguruje system tak by NIS
by³ aktywowany przy starcie systemu.

%description -l pt_BR
O authconfig é um programa de interface texto para configurar o NIS e
senhas shadow no seu sistema. O authconfig também pode inicializar o
NIS no boot do sistema.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="-DVERSION=\"${VERSION}\" %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} INSTROOT=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/authconfig
%{_mandir}/man8/*
