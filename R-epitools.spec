#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-epitools
Version  : 0.5.10
Release  : 5
URL      : https://cran.r-project.org/src/contrib/epitools_0.5-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/epitools_0.5-10.tar.gz
Summary  : Epidemiology Tools
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n epitools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530335215

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530335215
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epitools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epitools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epitools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library epitools|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/epitools/DESCRIPTION
/usr/lib64/R/library/epitools/INDEX
/usr/lib64/R/library/epitools/Meta/Rd.rds
/usr/lib64/R/library/epitools/Meta/data.rds
/usr/lib64/R/library/epitools/Meta/features.rds
/usr/lib64/R/library/epitools/Meta/hsearch.rds
/usr/lib64/R/library/epitools/Meta/links.rds
/usr/lib64/R/library/epitools/Meta/nsInfo.rds
/usr/lib64/R/library/epitools/Meta/package.rds
/usr/lib64/R/library/epitools/NAMESPACE
/usr/lib64/R/library/epitools/R/epitools
/usr/lib64/R/library/epitools/R/epitools.rdb
/usr/lib64/R/library/epitools/R/epitools.rdx
/usr/lib64/R/library/epitools/data/oswego.rda
/usr/lib64/R/library/epitools/data/wcgs.rda
/usr/lib64/R/library/epitools/data/wnv.rda
/usr/lib64/R/library/epitools/help/AnIndex
/usr/lib64/R/library/epitools/help/aliases.rds
/usr/lib64/R/library/epitools/help/epitools.rdb
/usr/lib64/R/library/epitools/help/epitools.rdx
/usr/lib64/R/library/epitools/help/paths.rds
/usr/lib64/R/library/epitools/html/00Index.html
/usr/lib64/R/library/epitools/html/R.css
