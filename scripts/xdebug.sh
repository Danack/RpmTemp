
startDir=$(pwd)
. ./setupDirectory.sh


cp ../packages/xdebug/xdebug.spec $RPM_DIR/SPECS/xdebug.spec
cp ../packages/xdebug/* $RPM_DIR/SOURCES/
cp ../zips/xdebug/xdebug-2.3.2.tgz $RPM_DIR/SOURCES/xdebug-2.3.2.tgz

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/xdebug.spec

. ${startDir}/copyAndRepo.sh

