Summary:	GNU GO
Summary(pl.UTF-8):	Wersja GNU gry w GO
Name:		gnugo
Version:	3.8
Release:	5
License:	GPL v3
Group:		Applications/Games
Source0:	ftp://ftp.gnu.org/gnu/gnugo/%{name}-%{version}.tar.gz
# Source0-md5:	6db0a528df58876d2b0ef1659c374a9a
Patch0:		%{name}-info.patch
Patch1:		%{name}-tinfo.patch
Patch2:		gnugo-3.8-format-security.patch
URL:		http://www.gnu.org/software/gnugo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Go is a game of strategy between two players usually played on a 19x19
grid called goban. GNU Go plays a game of Go against the user. It has
many other features: it can play against itself or another program,
analyse and score a recorded game. GNU Go is compliant with Go Modem
Protocol, and load/save games in the Smart Go format.

GNU Go default is a simple alpha-numeric board display, if you'd like
to use a graphical interface with GNU Go, you'll also need to install
the CGoban package and the X Window System.

%description -l pl.UTF-8
Go to gra strategiczna dla dwóch graczy rozgrywana na planszy 19x19
nazywanej goban. GNU Go gra przeciwko użytkownikowi. Ma wiele
możliwości: może grać przeciwko sobie samemu lub innemu programowi,
analizować i punktować zapisaną grę. GNU Go jest kompatybilny z Go
Modem Protocol, a zapisuje/odczytuje gry w formacie Smart Go.

GNU Go domyślnie ma standardowo proste, alfanumeryczne wyświetlanie
planszy. Jeśli chcesz graficzny interfejs do GNU Go, doinstaluj pakiet
CGoban (wymagający X Window System).

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gnugo
%{_infodir}/gnugo.info*
%{_mandir}/man6/*
