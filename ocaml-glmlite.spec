Name:           ocaml-glmlite
Version:        0.03.50
Release:        3
Summary:        OpenGL bindings for OCaml
License:        GPL
Group:          Development/Other
URL:            http://www.linux-nantes.org/~fmonnier/OCaml/GL/
Source0:        http://www.linux-nantes.org/~fmonnier/OCaml/GL/download/glMLite-%{version}.tgz
Patch0:         RedBook-Samples-fix-libpath.patch
Patch1:         glMLite-TEST-dir-libpath.patch
Patch4:         glMLite-TEST3-dir-libpath.patch
Patch2:         gle-examples-makefiles.patch
Patch3:         glMLite-LablGL-libpath.patch
BuildRequires:  ocaml
BuildRequires:	glut-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg-devel
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  libgle-devel
BuildRequires:  libftgl-devel

%package devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description
This package provides OpenGL bindings for OCaml.
There is a module for GL, Glu and Glut, and also some
texture loaders for different image file format.
There are specialised/optimised loaders for jpeg, png and svg,
and also a generic image loader (which uses the libmagick).
The names of the functions are the same than in the C API,
and the problematic types are packed in modules.
There are additional wrappers for the GLE and the FTGL
libraries, to perform extrusions and font rendering.

%description -n %{name}-devel
Development files for the package %{name}.

%prep
%setup -q -n glMLite-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

%build
%define _disable_ld_no_undefined 1
make everything OCAMLMKLIB="ocamlmklib -ldopt '%ldflags'"
make doc

%install
%define dest_dir %{buildroot}/%{_libdir}/ocaml/glMLite

install -d -m 755 %{dest_dir}
make install_everything PREFIX=%{dest_dir}

%files
%defattr(-,root,root)
%doc LICENSE_GPL.txt README.txt
%dir %{_libdir}/ocaml/glMLite
%{_libdir}/ocaml/glMLite/META
%{_libdir}/ocaml/glMLite/*.cma
%{_libdir}/ocaml/glMLite/*.cmi
%{_libdir}/ocaml/glMLite/*.so

%files devel
%defattr(-,root,root)
%doc SRC/doc
%doc TEST TEST3 toolbox RedBook-Samples gle-examples nehe-examples LablGL
%{_libdir}/ocaml/glMLite/*.a
%{_libdir}/ocaml/glMLite/*.o
%{_libdir}/ocaml/glMLite/*.cmx
%{_libdir}/ocaml/glMLite/*.cmxa



%changelog
* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 0.03.50-2mdv2011.0
+ Revision: 673609
- use correct build flags

* Mon Aug 16 2010 Florent Monnier <blue_prawn@mandriva.org> 0.03.50-1mdv2011.0
+ Revision: 570597
- updated version
- unified devel summary like the other packages

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 0.03.46-2mdv2011.0
+ Revision: 553485
- rebuild for new imagemagick

* Fri Apr 16 2010 Florent Monnier <blue_prawn@mandriva.org> 0.03.46-1mdv2010.1
+ Revision: 535249
- updated to version 0.03.46

* Sun Mar 28 2010 Florent Monnier <blue_prawn@mandriva.org> 0.03.45-1mdv2010.1
+ Revision: 528645
- updated to version 0.03.45

* Wed Feb 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.03.35-2mdv2010.1
+ Revision: 499934
- rebuild

* Tue Sep 29 2009 Florent Monnier <blue_prawn@mandriva.org> 0.03.35-1mdv2010.0
+ Revision: 451083
- include .o files in the devel package
- new version

* Tue Sep 29 2009 Florent Monnier <blue_prawn@mandriva.org> 0.03.34-2mdv2010.0
+ Revision: 451034
- corrected the rights of the README file (was -rw------- now -rw-r--r--)

* Mon Sep 28 2009 Florent Monnier <blue_prawn@mandriva.org> 0.03.34-1mdv2010.0
+ Revision: 450701
- new version

* Sat Sep 26 2009 Florent Monnier <blue_prawn@mandriva.org> 0.03.33-1mdv2010.0
+ Revision: 449585
- new version 0.03.33, and now includes the examples

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 0.03.31-2mdv2010.0
+ Revision: 419798
- rebuild for new libjpeg v7

* Thu Aug 13 2009 Florent Monnier <blue_prawn@mandriva.org> 0.03.31-1mdv2010.0
+ Revision: 415812
- import ocaml-glmlite


