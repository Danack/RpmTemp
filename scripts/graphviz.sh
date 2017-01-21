

startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/graphviz/graphviz.spec $RPM_DIR/SPECS/graphviz.spec
cp ../zips/graphviz/graphviz-2.40.1.tar.gz $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/graphviz.spec

. ${startDir}/copyAndRepo.sh





