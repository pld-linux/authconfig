Summary:	Text-mode tool for setting up NIS and shadow passwords
Summary(de.UTF-8):	Textmodus-Tool, um NIS und shadow-Passwoerter zu konfigurieren
Summary(es.UTF-8):	Herramienta de interfaz texto para configuración de contraseñas shadow y NIS
Summary(ja.UTF-8):	NIS とシャドーパスワードを設定するためのテキストモードのツール。
Summary(pl.UTF-8):	Narzędzie do ustawiania przesłoniętych haseł oraz NIS
Summary(pt_BR.UTF-8):	Ferramenta de interface texto para configuração de senhas shadow e NIS
Summary(ru.UTF-8):	Утилита текстового режима для настройки shadow и NIS-паролей
Summary(uk.UTF-8):	Утиліта текстового режиму для налагодження shadow та NIS-паролів
Name:		authconfig
Version:	2.0
Release:	8
License:	GPL
Group:		Base
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	5299be78429fd5f550950966b0a3e015
Patch0:		%{name}-make.patch
Patch1:		%{name}-po.patch
BuildRequires:	gettext-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	slang-devel >= 2.0.0
ExclusiveOS:	Linux
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
