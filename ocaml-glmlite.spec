Summary:	OpenGL bindings for OCaml
Name:		ocaml-glmlite
Version:	0.03.51
Release:	1
License:	LGPLv3+ or MIT
Group:		Development/Other
Url:		http://www.linux-nantes.org/~fmonnier/OCaml/GL/
Source0:	http://www.linux-nantes.org/~fmonnier/OCaml/GL/download/glMLite-%{version}.tgz
Patch0:		RedBook-Samples-fix-libpath.patch
Patch1:		glMLite-TEST-dir-libpath.patch
Patch4:		glMLite-TEST3-dir-libpath.patch
Patch2:		gle-examples-makefiles.patch
Patch3:		glMLite-LablGL-libpath.patch
BuildRequires:	ocaml
BuildRequires:	jpeg-devel
BuildRequires:	libgle-devel
BuildRequires:	pkgconfig(ftgl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
Requires:	jpeg-devel
Requires:	libgle-devel
Requires:	pkgconfig(ftgl)
Requires:	pkgconfig(gl)
Requires:	pkgconfig(glu)
Requires:	pkgconfig(glut)
Requires:	pkgconfig(ImageMagick)
Requires:	pkgconfig(libpng)
Requires:	pkgconfig(librsvg-2.0)

%description
This package provides OpenGL bindings for OCaml.

There is a module for GL, Glu and Glut, and also some texture loaders for
different image file format. There are specialised/optimised loaders for
jpeg, png and svg,and also a generic image loader (which uses the libmagick).

The names of the functions are the same than in the C API, and the problematic
types are packed in modules. There are additional wrappers for the GLE and the
FTGL libraries, to perform extrusions and font rendering.

%files
%doc LICENSE_GPL.txt README.txt
%dir %{_libdir}/ocaml/glMLite
%{_libdir}/ocaml/glMLite/META
%{_libdir}/ocaml/glMLite/*.cma
%{_libdir}/ocaml/glMLite/*.cmi
%{_libdir}/ocaml/glMLite/*.so

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description -n %{name}-devel
Development files for the package %{name}.

%files devel
%doc SRC/doc
%doc TEST TEST3 toolbox RedBook-Samples gle-examples nehe-examples LablGL
%{_libdir}/ocaml/glMLite/*.a
%{_libdir}/ocaml/glMLite/*.o
%{_libdir}/ocaml/glMLite/*.cmx
%{_libdir}/ocaml/glMLite/*.cmxa

#----------------------------------------------------------------------------

%prep
%setup -q -n glMLite-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

%build
make everything
make doc

%install
install -d -m 755 %{buildroot}%{_libdir}/ocaml/glMLite
make install_everything PREFIX=%{buildroot}%{_libdir}/ocaml/glMLite

