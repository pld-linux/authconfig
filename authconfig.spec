Summary:	Text-mode tool for setting up NIS and shadow passwords
Summary(de):	Textmodus-Tool, um NIS und shadow-Passwoerter zu konfigurieren
Summary(es):	Herramienta de interfaz texto para configuraciСn de contraseЯas shadow y NIS
Summary(ja):	NIS ╓х╔╥╔Ц╔и║╪╔я╔╧╔О║╪╔и╓РюъдЙ╓╧╓К╓©╓А╓н╔ф╔╜╔╧╔х╔Б║╪╔и╓н╔д║╪╔К║ё
Summary(pl):	NarzЙdzie do ustawiania przesЁoniЙtych haseЁ oraz NIS
Summary(pt_BR):	Ferramenta de interface texto para configuraГЦo de senhas shadow e NIS
Summary(ru):	Утилита текстового режима для настройки shadow и NIS-паролей
Summary(uk):	Утил╕та текстового режиму для налагодження shadow та NIS-парол╕в
Name:		authconfig
Version:	2.0
Release:	7
License:	GPL
Group:		Base
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	5299be78429fd5f550950966b0a3e015
Patch0:		%{name}-make.patch
Patch1:		%{name}-po.patch
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	slang-devel
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authconfig is a terminal mode program for setting up Network
Information Service (NIS) and shadow (more secure) passwords on your
system. Authconfig also configures the system to automatically turn on
NIS at system startup.

%description -l de
Authconfig ist ein Textmodus-Programm, um Network
Informations-Services (NIS) und Shadow (sicherere) PasswЖrter auf
Ihren System zu konfigurieren. Authconfig kann auъerdem anschalten,
daъ NIS beim Systemstart angeschaltet wird.

%description -l es
authconfig es un programa de interfaz de texto para configurar NIS y
contraseЯas shadow en el sistema. El programa authconfig tambiИn puede
inicializar NIS cuando se arranca el sistema.

%description -l ja
authconfig ╓о╔╥╔╧╔ф╔Ю╓к Network Information Service (NIS) ╓х╔╥╔Ц╔и║╪
(╓Х╓Й╔╩╔╜╔Е╔Й╔ф╔ё║╪╓╛╧Б╓╓)╔я╔╧╔О║╪╔и╓н╔╩╔ц╔ф╔ё╔С╔╟╓Р╓╧╓Кц╪кЖ╔Б║╪╔и╓н
╔в╔М╔╟╔И╔Ю╓г╓╧║ёauthconfig ╓о╓ч╓©╔╥╔╧╔ф╔Ю╣╞ф╟╩Ч╓к╪╚ф╟е╙╓к NIS ╓Р
╔╙╔С╓к╓╧╓К╓Х╓╕╓к╔╥╔╧╔ф╔Ю╓РюъдЙ╓г╓╜╓ч╓╧║ё

%description -l pl
Authconfig jest terminalowym programem dla ustawiania NIS (Network
Information Service) oraz przesЁoniЙtych (bardziej bezpiecznych) haseЁ
w Twoim systemie. Authconfig dodatkowo konfiguruje system tak by NIS
byЁ aktywowany przy starcie systemu.

%description -l pt_BR
O authconfig И um programa de interface texto para configurar o NIS e
senhas shadow no seu sistema. O authconfig tambИm pode inicializar o
NIS no boot do sistema.

%description -l ru
Authconfig - это терминальная программа для настройки Network
Information Service (NIS) и shadow (более безопасных) паролей в вашей
системе. Authconfig также настраивает систему на автоматический запуск
NIS при старте системы.

%description -l uk
Authconfig - це терм╕нальна програма для налагодження Network
Information Service (NIS) та shadow (б╕льш безпечних) парол╕в у ваш╕й
систем╕. Authconfig також конф╕гуру╓ систему для автоматичного запуску
NIS при старт╕ системи.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv po/{no,nb}.po
mv po/sr{,@Latn}.po

%build
%{__make} \
	CFLAGS="-DVERSION=\"${VERSION}\" %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT

# remove empty translation files
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/authconfig
%{_mandir}/man8/*
