Name:		texlive-beamertheme-arguelles
Version:	65234
Release:	1
Summary:	Simple, typographic beamer theme
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-arguelles
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-arguelles.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-arguelles.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Arguelles is a beamer theme that helps you create beautiful
presentations. It aims for simplicity and readability by
following best practices of graphic design. The layout is
elegant but subtle, so as to keep the audience's attention on
your content. This is brought to life by Alegreya, one of the
53 Fonts of the Decade selected by the Association
Typographique Internationale (2011).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-arguelles
%doc %{_texmfdistdir}/doc/latex/beamertheme-arguelles

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
