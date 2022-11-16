Name:		texlive-froufrou
Version:	59103
Release:	1
Summary:	Fancy section separators
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/froufrou
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/froufrou.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/froufrou.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/froufrou.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides fancy separators, which are visual cues
that indicate a change of subject or context without actually
starting a new chapter or section.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/froufrou
%{_texmfdistdir}/tex/latex/froufrou
%doc %{_texmfdistdir}/doc/latex/froufrou

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
