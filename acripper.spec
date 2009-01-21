Summary:	ACRipper is a tool for ripping and encoding CD tracks on the fly
Summary(pl.UTF-8):	ACRipper jest narzędziem służącym do kodowania scieżek CD w locie
Name:		acripper
Version:	1.2.1
Release:	0.1
License:	GPL v2
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/acripper/%{name}-%{version}.tar.gz
# Source0-md5:	2a0b67260ffbfd6378b2d39ceda3a531
Patch0:		%{name}-bash.patch
URL:		http://sourceforge.net/projects/acripper/
Requires:	bash
Requires:	cdparanoia
Requires:	vorbis-tools
Suggests:	flac
Suggests:	lame
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Automatic command line CD ripper and ogg encoder along with freedb.org
client. It tries to connect to freedb.org server to get CD info. If no
info is found a text file may be provided instead. Also suport FLAC
and MP3 (ID3 tag).

%description -l pl.UTF-8
Automatyczny ripper CD i enkoder ogg obsługiwany z linii poleceń, jest
również klientem freedb.org. Próbuje łączyć się z serwerem freedb.org
by pobrać informacje o CD. Jeśli żadne informacje nie zostaną
znalezione można wprowadzić ręcznie alternatywny opis. Program wspiera
FLAC i MP3 (tagi ID3).

%prep
%setup -q -n acriper-%{version}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install {acripper,cddbc} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/acripper
%attr(755,root,root) %{_bindir}/cddbc
