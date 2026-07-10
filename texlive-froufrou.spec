%global tl_name froufrou
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.0
Release:	%{tl_revision}.1
Summary:	Fancy section separators
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/froufrou
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/froufrou.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/froufrou.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/froufrou.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides fancy separators, which are visual cues that
indicate a change of subject or context without actually starting a new
chapter or section.

