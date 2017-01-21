# $Id$ $Revision$
# graphviz.spec.  Generated from graphviz.spec.in by configure.

# Note: pre gd-2.0.34 graphviz uses its own gd tree with gif support and other fixes


%define date %(date +%%Y_%%m_%%d)


#-- Global graphviz rpm and src.rpm tags-------------------------------------
Name:    graphviz-%{date}
Summary: Graph Visualization Tools
Version: 2.40.1


%define truerelease 1
%{?distroagnostic: %define release %{truerelease}}
%{!?distroagnostic: %define release %{truerelease}%{?dist}}

Release: %{?release}
Group:   Applications/Multimedia
License: EPL
URL:     http://www.graphviz.org/
Source0: http://www.graphviz.org/pub/graphviz/development/SOURCES/graphviz-2.40.1.tar.gz

Prefix: /usr

#-- feature and package selection -------------------------------------------
#   depends on macro values set by redhat-rpm-config

# All features are off (undefined) by default
# To enable, use: <percent>define FEATURE 1
# Available features are:
#    SHARP GHOSTSCRIPT _GO GUILE _IO JAVA LUA OCAML ORTHO PERL PHP
#    PYTHON RUBY R_LANG TCL IPSEPCOLA MYLIBGD PANGOCAIRO RSVG
#    GTK GLITZ SMYRNA DEVIL MING GDK _QT WEBP

# SuSE uses a different mechanism to generate BuildRequires
# norootforbuild
# neededforbuild  expat freetype2-devel gcc tcl tcl-devel tk tk-devel x-devel-packages

BuildRoot:     %{_tmppath}/graphviz-%{version}-%{release}-root-%(%{__id_u} -n)

# BuildRequires: zlib-devel expat-devel ann-devel
# BuildRequires: ksh bison m4 flex swig tk tcl >= 8.3 freetype-devel >= 2

#-- All platforms
%define __X 1

# What a meal PHP makes of versioning !!!
%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)
%global php_apiver %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)

# Fix private-shared-object-provides
# RPM 4.8
%{?filter_provides_in: %filter_provides_in %{php_extdir}/.*\.so$}
%{?filter_setup}
# RPM 4.9
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}%{php_extdir}/.*\\.so$


#-- main graphviz rpm ------------------------------------------------
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in bar-charts).

%files
%defattr(-,root,root,-)
# %if 0%{?SEPARATE_LICENSE}
# %license COPYING
# %endif
# %doc COPYING AUTHORS ChangeLog NEWS README
%exclude %{_bindir}/dot_builtins
%{_bindir}/acyclic
%{_bindir}/bcomps
%{_bindir}/ccomps
%{_bindir}/circo
%{_bindir}/cluster
%{_bindir}/dijkstra
%{_bindir}/dot
%{_bindir}/dot2gxl
%{_bindir}/fdp
%{_bindir}/gc
%{_bindir}/gml2gv
%{_bindir}/graphml2gv
%{_bindir}/gv2gml
%{_bindir}/gv2gxl
%{_bindir}/gvcolor
%{_bindir}/gvgen
%{_bindir}/gvmap
%{_bindir}/gvmap.sh
%{_bindir}/gvpack
%{_bindir}/gvpr
%{_bindir}/gxl2dot
%{_bindir}/gxl2gv
%{_bindir}/edgepaint
%{_bindir}/mm2gv
%{_bindir}/neato
%{_bindir}/nop
%{_bindir}/osage
%{_bindir}/patchwork
%{_bindir}/prune
%{_bindir}/sccmap
%{_bindir}/sfdp
%{_bindir}/tred
%{_bindir}/twopi
%{_bindir}/unflatten
%{_mandir}/man1/acyclic.1*
%{_mandir}/man1/bcomps.1*
%{_mandir}/man1/ccomps.1*
%{_mandir}/man1/circo.1*
%{_mandir}/man1/cluster.1*
%{_mandir}/man1/diffimg.1*
%{_mandir}/man1/dijkstra.1*
%{_mandir}/man1/dot.1*
%{_mandir}/man1/fdp.1*
%{_mandir}/man1/gc.1*
%{_mandir}/man1/gml2gv.1*
%{_mandir}/man1/graphml2gv.1*
%{_mandir}/man1/gv2gml.1*
%{_mandir}/man1/gv2gxl.1*
%{_mandir}/man1/gvcolor.1*
%{_mandir}/man1/gvgen.1*
%{_mandir}/man1/gvmap.1*
%{_mandir}/man1/gvmap.sh.1*
%{_mandir}/man1/gvpack.1*
%{_mandir}/man1/gvpr.1*
%{_mandir}/man1/gxl2gv.1*
%{_mandir}/man1/mingle.1*
%{_mandir}/man1/edgepaint.1*
%{_mandir}/man1/mm2gv.1*
%{_mandir}/man1/neato.1*
%{_mandir}/man1/nop.1*
%{_mandir}/man1/osage.1*
%{_mandir}/man1/patchwork.1*
%{_mandir}/man1/prune.1*
%{_mandir}/man1/sccmap.1*
%{_mandir}/man1/sfdp.1*
%{_mandir}/man1/tred.1*
%{_mandir}/man1/twopi.1*
%{_mandir}/man1/unflatten.1*
%{_mandir}/man7/graphviz.7*
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/gvpr/*
# %{_bindir}/lefty                
%{_bindir}/lneato                 
%{_bindir}/dotty                  
# %{_bindir}/vimdot               
%{_mandir}/man1/lefty.1*          
%{_mandir}/man1/lneato.1*         
%{_mandir}/man1/dotty.1*          
%{_mandir}/man1/vimdot.1*         
%{_datadir}/graphviz/lefty        
%if 0%{?SMYRNA}                   
# %{_bindir}/smyrna               
# %{_datadir}/graphviz/smyrna     
%{_mandir}/man1/smyrna.1*         
%endif                            
%{_datadir}/graphviz/graphs
%{_bindir}/diffimg
%dir %{_libdir}/graphviz
%{_libdir}/graphviz/libgvplugin_gd.so.*
%{_libdir}/graphviz/libgvplugin_core.so.*
%{_libdir}/graphviz/libgvplugin_dot_layout.so.*
%{_libdir}/graphviz/libgvplugin_neato_layout.so.*
%{_libdir}/libcdt.so.*
%{_libdir}/libcgraph.so.*
%{_libdir}/libgvc.so.*
%{_libdir}/libgvpr.so.*
%{_libdir}/libpathplan.so.*
%{_libdir}/libxdot.so.4*
%{_libdir}/liblab_gamut.so.*
%{_mandir}/man1/smyrna.1*



#-- graphviz-libs rpm --------------------------------------------------
%package libs
Group:            Applications/Multimedia
Summary:          Graphviz base libs
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libs
Graphviz core libs 

%files libs
%defattr(-,root,root,-)
%{_libdir}/libcdt.so.*
%{_libdir}/libcgraph.so.*
%{_libdir}/libgvc.so.*
%{_libdir}/libgvpr.so.*
%{_libdir}/libpathplan.so.*
%{_libdir}/libxdot.so.4*
%{_libdir}/liblab_gamut.so.*

#-- graphviz-plugins-core rpm --------------------------------------------------
%package plugins-core
Group:            Applications/Multimedia
Summary:          Graphviz plugins - core layout engines and text renderers
Requires:         %{name} = %{version}-%{release}

%description plugins-core
Graphviz plugins - core layout engines and text renderers

# run "dot -c" to generate plugin config in {_libdir}/graphviz/config
%post
LD_LIBRARY_PATH=$RPM_INSTALL_PREFIX0/%{_lib} $RPM_INSTALL_PREFIX0/bin/dot -c

# if there is no dot after everything else is done, then remove config
%postun
if [ $1 -eq 0 ]; then
        rm -f $RPM_INSTALL_PREFIX0/%{_lib}/graphviz/config || :
fi

%files plugins-core
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz
%{_libdir}/graphviz/libgvplugin_core.so.*
%{_libdir}/graphviz/libgvplugin_dot_layout.so.*
%{_libdir}/graphviz/libgvplugin_neato_layout.so.*








#-- graphviz-plugins-webp rpm --------------------------------------------------
%if 0%{?WEBP}
%package plugins-webp
Group:            Applications/Multimedia
Summary:          Graphviz plugin for webp format images, using libwebp
Requires:         %{name}-x = %{version}-%{release}
Obsoletes:        %{name}-webp

%description plugins-webp
Graphviz plugin for webp image rendering. 

# run "dot -c" to generate plugin config in {_libdir}/graphviz/config
%post plugins-webp
LD_LIBRARY_PATH=$RPM_INSTALL_PREFIX0/%{_lib} $RPM_INSTALL_PREFIX0/bin/dot -c

%postun plugins-webp
[ -x $RPM_INSTALL_PREFIX0/bin/dot ] && LD_LIBRARY_PATH=$RPM_INSTALL_PREFIX0/%{_lib} $RPM_INSTALL_PREFIX0/bin/dot -c || :

%files plugins-webp
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz
%{_libdir}/graphviz/libgvplugin_webp.so.*
%endif



#-- graphviz-devel rpm --------------------------------------------
%package devel
Group:          Development/Libraries
Summary:        Development package for graphviz
Requires:       %{name}-libs = %{version}-%{release}, pkgconfig

%description devel
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in bar-charts).
This package contains development files for graphviz-libs.

%files devel
%defattr(-,root,root,-)
%{_includedir}/graphviz
%{_libdir}/libcdt.so
%{_mandir}/man3/cdt.3.*
%{_libdir}/pkgconfig/libcdt.pc
%{_libdir}/libcgraph.so
%{_mandir}/man3/cgraph.3.*
%{_libdir}/pkgconfig/libcgraph.pc
%{_libdir}/libgvc.so
%{_mandir}/man3/gvc.3.*
%{_libdir}/pkgconfig/libgvc.pc
%{_libdir}/libgvpr.so
%{_mandir}/man3/gvpr.3.*
%{_libdir}/pkgconfig/libgvpr.pc
%{_libdir}/libpathplan.so
%{_mandir}/man3/pathplan.3.*
%{_libdir}/pkgconfig/libpathplan.pc
%{_libdir}/libxdot.so
%{_mandir}/man3/xdot.3.*
%{_libdir}/pkgconfig/libxdot.pc
%{_libdir}/liblab_gamut.so
%{_mandir}/man3/lab_gamut.3.*
%{_libdir}/pkgconfig/liblab_gamut.pc
%{_mandir}/man3/expr.3.*
%{_mandir}/man3/pack.3.*
%exclude %{_libdir}/graphviz/libgvplugin*
%exclude %{_libdir}/graphviz/*.so



#-- building --------------------------------------------------

%prep
%setup -q -n graphviz-2.40.1




%build
# XXX ix86 only used to have -ffast-math, let's use everywhere
%{expand: %%define optflags %{optflags} -ffast-math}

# %%configure is broken in RH7.3 rpmbuild
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --libdir=%{_libdir} \
        --includedir=%{_includedir} \
        --datadir=%{_datadir} \
        --mandir=%{_mandir} \
        --disable-static \
        --disable-dependency-tracking \
        --with-libgd=yes \
        --with-expat=yes

#        --enable-sharp%{!?SHARP:=no} \
#        --enable-go%{!?_GO:=no} \
#        --enable-guile%{!?GUILE:=no} \
#        --enable-io%{!?_IO:=no} \
#        --enable-java%{!?JAVA:=no} \
#        --enable-lua%{!?LUA:=no} \
#        --enable-ocaml%{!?OCAML:=no} \
#        --enable-perl%{!?PERL:=no} \
#        --enable-php=no \
#        --enable-python%{!?PYTHON:=no} \
#        --enable-r%{!?R_LANG:=no} \
#        --enable-ruby%{!?RUBY:=no} \
#        --enable-tcl%{!?TCL:=no} \
#        --with%{!?DEVIL:out}-devil \
#        --with%{!?WEBP:out}-webp \
#        --with-libgd=yes \
#        --with%{!?GDK:out}-gdk \
#        --with%{!?GHOSTSCRIPT:out}-ghostscript \
#        --with%{!?GLITZ:out}-glitz \
#        --with%{!?IPSEPCOLA:out}-ipsepcola \
#        --with%{!?LASI:out}-lasi \
#        --with%{!?MING:out}-ming \
#        --with%{!?_QT:out}-qt \
#        --with%{!?PANGOCAIRO:out}-pangocairo \
#        --with%{!?POPPLER:out}-poppler \
#        --with%{!?RSVG:out}-rsvg \
#        --with%{!?ORTHO:out}-ortho \
#        --with%{!?SFDP:out}-sfdp \
#        --with%{!?SMYRNA:out}-smyrna \
#        --with%{!?__X:out}-x
make %{?_smp_mflags}

%install
rm -rf %{buildroot} __doc
make DESTDIR=%{buildroot} \
        docdir=%{buildroot}%{_docdir}/graphviz \
        pkgconfigdir=%{_libdir}/pkgconfig \
        install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
chmod -x %{buildroot}%{_datadir}/graphviz/lefty/*
cp -a %{buildroot}%{_datadir}/graphviz/doc __doc
rm -rf %{buildroot}%{_datadir}/graphviz/doc


%check
%ifnarch ppc64 ppc
# regression test, segfaults on ppc/ppc64, possible endian issues?
# regressions tests require ksh93 - not available on centos3
#cd rtest
#make rtest
%endif

%clean
# optional regression test using the products in the build tree
%if 0%{?rtest}
cd rtest
make rtest
%endif
# clean up temporary installation
 # rm -rf %{buildroot}



#-- changelog --------------------------------------------------

