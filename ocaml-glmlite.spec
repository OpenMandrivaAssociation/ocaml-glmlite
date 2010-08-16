Name:           ocaml-glmlite
Version:        0.03.46
Release:        %mkrel 2
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
BuildRequires:  X11-devel
BuildRequires:  Mesa-common-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg-devel
BuildRequires:  libmagick-devel
BuildRequires:  libgle-devel
BuildRequires:  libftgl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
make everything
make doc

%install
rm -rf %{buildroot}
%define dest_dir %{buildroot}/%{_libdir}/ocaml/glMLite

install -d -m 755 %{dest_dir}
make install_everything PREFIX=%{dest_dir}

%clean
rm -rf %{buildroot}

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

