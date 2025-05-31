Name: fapg
Summary: Fast Audio Playlist Generator
Version: 0.45
Release: 1
Url: https://royale.zerezo.com/fapg/
Source: http://royale.zerezo.com/%{name}/%{name}-%{version}.tar.gz
Group: Sound
License: GPL
BuildRequires:  pkgconfig(liburiparser)

BuildRoot: %{_tmppath}/%{name}-buildroot

%description
FAPG is a tool to generate list of audio files (Wav, MP3, Ogg, etc)
in various formats (M3U, PLS, HTML, etc).

%prep 
%setup -q

%build 
%configure
%make_build

%install 
%make_install

%files 
%defattr(-,root,root,0755) 
%doc COPYING README
%{_bindir}/fapg
%{_mandir}/man1/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.35-6mdv2011.0
+ Revision: 618254
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.35-5mdv2010.0
+ Revision: 428702
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.35-4mdv2009.0
+ Revision: 245055
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.35-2mdv2008.1
+ Revision: 136408
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import fapg


* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 0.35-2mdv2007.0
- rebuild

* Tue Feb 08 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.32-1mdk
- from Antoine Jacquet <royale@zerezo.com> : 
 - Fixed group in the spec file

* Mon Feb 07 2005 Antoine Jacquet <royale@zerezo.com> 
- Added spec file
