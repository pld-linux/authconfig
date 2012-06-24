Summary:	Text-mode tool for setting up NIS and shadow passwords
Summary(de):	Textmodus-Tool, um NIS und shadow-Passwoerter zu konfigurieren
Summary(es):	Herramienta de interfaz texto para configuraci�n de contrase�as shadow y NIS
Summary(ja):	NIS �ȥ���ɡ��ѥ���ɤ����ꤹ�뤿��Υƥ����ȥ⡼�ɤΥġ��롣
Summary(pl):	Narz�dzie do ustawiania przes�oni�tych hase� oraz NIS
Summary(pt_BR):	Ferramenta de interface texto para configura��o de senhas shadow e NIS
Summary(ru):	������� ���������� ������ ��� ��������� shadow � NIS-�������
Summary(uk):	���̦�� ���������� ������ ��� ������������ shadow �� NIS-����̦�
Name:		authconfig
Version:	2.0
Release:	4
License:	GPL
ExclusiveOS:	Linux
Group:		Base
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
Informations-Services (NIS) und Shadow (sicherere) Passw�rter auf
Ihren System zu konfigurieren. Authconfig kann au�erdem anschalten,
da� NIS beim Systemstart angeschaltet wird.

%description -l es
authconfig es un programa de interfaz de texto para configurar NIS y
contrase�as shadow en el sistema. El programa authconfig tambi�n puede
inicializar NIS cuando se arranca el sistema.

%description -l ja
authconfig �ϥ����ƥ�� Network Information Service (NIS) �ȥ���ɡ�
(��ꥻ�����ƥ������⤤)�ѥ���ɤΥ��åƥ��󥰤򤹤�ü���⡼�ɤ�
�ץ����Ǥ���authconfig �Ϥޤ������ƥ൯ư���˼�ưŪ�� NIS ��
����ˤ���褦�˥����ƥ������Ǥ��ޤ���

%description -l pl
Authconfig jest terminalowym programem dla ustawiania NIS (Network
Information Service) oraz przes�onietych (bardziej bezpiecznych) hase�
w Twoim systemie. Authconfig dodatkowo konfiguruje system tak by NIS
by� aktywowany przy starcie systemu.

%description -l pt_BR
O authconfig � um programa de interface texto para configurar o NIS e
senhas shadow no seu sistema. O authconfig tamb�m pode inicializar o
NIS no boot do sistema.

%description -l ru
Authconfig - ��� ������������ ��������� ��� ��������� Network
Information Service (NIS) � shadow (����� ����������) ������� � �����
�������. Authconfig ����� ����������� ������� �� �������������� ������
NIS ��� ������ �������.

%description -l uk
Authconfig - �� ���ͦ������ �������� ��� ������������ Network
Information Service (NIS) �� shadow (¦��� ���������) ����̦� � ��ۦ�
�����ͦ. Authconfig ����� ���Ʀ���դ ������� ��� ������������� �������
NIS ��� ����Ԧ �������.

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
