%define name fapg
%define version 0.35
%define release %mkrel 4

Name: %name
Summary: Fast Audio Playlist Generator
Version: %version
Release: %release
Url: http://royale.zerezo.com/fapg/
Source: http://royale.zerezo.com/%{name}/%{name}-%{version}.tar.bz2
Group: Sound
License: GPL
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
FAPG is a tool to generate list of audio files (Wav, MP3, Ogg, etc)
in various formats (M3U, PLS, HTML, etc).

%prep 
%setup -q

%build 
make

%install 
make install PRE=$RPM_BUILD_ROOT/usr

rm -rf $RPM_BUILD_ROOT/%_docdir/

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755) 
%doc COPYING README
%{_bindir}/fapg
%{_mandir}/man1/*


