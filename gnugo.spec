Summary:	GNU GO
Summary(pl):	Wersja GNU gry w GO
Name:		gnugo
Version:	2.6
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.gnu.org/gnu/gnugo/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/gnugo/
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

%description -l pl
Go to gra strategiczna dla dwóch graczy rozgrywana na planszy 19x19
nazywanej goban. GNU Go gra przeciwko u¿ytkownikowi. Ma wiele
mo¿liwo¶ci: mo¿e graæ przeciwko sobie samemu lub innemu programowi,
analizowaæ i punktowaæ zapisan± grê. GNU Go jest kompatybilny z Go
Modem Protocol, a zapisuje/odczytuje gry w formacie Smart Go.

GNU Go domy¶lnie ma standardowo proste, alfanumeryczne wy¶wietlanie
planszy. Je¶li chcesz graficzny interfejs do GNU Go, doinstaluj pakiet
CGoban (wymagaj±cy X Window System).

%prep
%setup -q
%patch -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gnugo
%{_infodir}/*
%{_mandir}/man6/*
