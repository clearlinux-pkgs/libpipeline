#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x393587D97D86500B (cjwatson@debian.org)
#
Name     : libpipeline
Version  : 1.5.7
Release  : 27
URL      : https://download.savannah.nongnu.org/releases/libpipeline/libpipeline-1.5.7.tar.gz
Source0  : https://download.savannah.nongnu.org/releases/libpipeline/libpipeline-1.5.7.tar.gz
Source1  : https://download.savannah.nongnu.org/releases/libpipeline/libpipeline-1.5.7.tar.gz.asc
Summary  : Pipeline manipulation library
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: libpipeline-lib = %{version}-%{release}
Requires: libpipeline-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(check)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# libpipeline, a pipeline manipulation library
Git repository: https://gitlab.com/libpipeline/libpipeline

%package dev
Summary: dev components for the libpipeline package.
Group: Development
Requires: libpipeline-lib = %{version}-%{release}
Provides: libpipeline-devel = %{version}-%{release}
Requires: libpipeline = %{version}-%{release}

%description dev
dev components for the libpipeline package.


%package lib
Summary: lib components for the libpipeline package.
Group: Libraries
Requires: libpipeline-license = %{version}-%{release}

%description lib
lib components for the libpipeline package.


%package license
Summary: license components for the libpipeline package.
Group: Default

%description license
license components for the libpipeline package.


%prep
%setup -q -n libpipeline-1.5.7
cd %{_builddir}/libpipeline-1.5.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702020774
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702020774
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libpipeline
cp %{_builddir}/libpipeline-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libpipeline/31a3d460bb3c7d98845187c716a30db81c44b615 || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pipeline.h
/usr/lib64/libpipeline.so
/usr/lib64/pkgconfig/libpipeline.pc
/usr/share/man/man3/libpipeline.3
/usr/share/man/man3/pipecmd_arg.3
/usr/share/man/man3/pipecmd_argf.3
/usr/share/man/man3/pipecmd_args.3
/usr/share/man/man3/pipecmd_argstr.3
/usr/share/man/man3/pipecmd_argv.3
/usr/share/man/man3/pipecmd_chdir.3
/usr/share/man/man3/pipecmd_clearenv.3
/usr/share/man/man3/pipecmd_discard_err.3
/usr/share/man/man3/pipecmd_dump.3
/usr/share/man/man3/pipecmd_dup.3
/usr/share/man/man3/pipecmd_exec.3
/usr/share/man/man3/pipecmd_fchdir.3
/usr/share/man/man3/pipecmd_free.3
/usr/share/man/man3/pipecmd_get_nargs.3
/usr/share/man/man3/pipecmd_new.3
/usr/share/man/man3/pipecmd_new_args.3
/usr/share/man/man3/pipecmd_new_argstr.3
/usr/share/man/man3/pipecmd_new_argv.3
/usr/share/man/man3/pipecmd_new_function.3
/usr/share/man/man3/pipecmd_new_passthrough.3
/usr/share/man/man3/pipecmd_new_sequence.3
/usr/share/man/man3/pipecmd_new_sequencev.3
/usr/share/man/man3/pipecmd_nice.3
/usr/share/man/man3/pipecmd_pre_exec.3
/usr/share/man/man3/pipecmd_sequence_command.3
/usr/share/man/man3/pipecmd_setenv.3
/usr/share/man/man3/pipecmd_tostring.3
/usr/share/man/man3/pipecmd_unsetenv.3
/usr/share/man/man3/pipeline_command.3
/usr/share/man/man3/pipeline_command_args.3
/usr/share/man/man3/pipeline_command_argstr.3
/usr/share/man/man3/pipeline_command_argv.3
/usr/share/man/man3/pipeline_commands.3
/usr/share/man/man3/pipeline_commandv.3
/usr/share/man/man3/pipeline_connect.3
/usr/share/man/man3/pipeline_dump.3
/usr/share/man/man3/pipeline_free.3
/usr/share/man/man3/pipeline_get_command.3
/usr/share/man/man3/pipeline_get_infile.3
/usr/share/man/man3/pipeline_get_ncommands.3
/usr/share/man/man3/pipeline_get_outfile.3
/usr/share/man/man3/pipeline_get_pid.3
/usr/share/man/man3/pipeline_ignore_signals.3
/usr/share/man/man3/pipeline_install_post_fork.3
/usr/share/man/man3/pipeline_join.3
/usr/share/man/man3/pipeline_new.3
/usr/share/man/man3/pipeline_new_command_args.3
/usr/share/man/man3/pipeline_new_command_argv.3
/usr/share/man/man3/pipeline_new_commands.3
/usr/share/man/man3/pipeline_new_commandv.3
/usr/share/man/man3/pipeline_peek.3
/usr/share/man/man3/pipeline_peek_size.3
/usr/share/man/man3/pipeline_peek_skip.3
/usr/share/man/man3/pipeline_peekline.3
/usr/share/man/man3/pipeline_pump.3
/usr/share/man/man3/pipeline_read.3
/usr/share/man/man3/pipeline_readline.3
/usr/share/man/man3/pipeline_run.3
/usr/share/man/man3/pipeline_set_command.3
/usr/share/man/man3/pipeline_start.3
/usr/share/man/man3/pipeline_tostring.3
/usr/share/man/man3/pipeline_wait.3
/usr/share/man/man3/pipeline_wait_all.3
/usr/share/man/man3/pipeline_want_in.3
/usr/share/man/man3/pipeline_want_infile.3
/usr/share/man/man3/pipeline_want_out.3
/usr/share/man/man3/pipeline_want_outfile.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpipeline.so.1
/usr/lib64/libpipeline.so.1.5.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpipeline/31a3d460bb3c7d98845187c716a30db81c44b615
