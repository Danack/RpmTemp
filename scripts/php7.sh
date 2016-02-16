
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/php/php7.spec $RPM_DIR/SPECS/php7.spec
cp ../packages/php/* $RPM_DIR/SOURCES/
cp ../zips/apcu/apcu-seven.tar.gz $RPM_DIR/SOURCES/apcu-seven.tar.gz
cp ../zips/yaml/yaml-1.2.0.tgz $RPM_DIR/SOURCES/yaml-1.2.0.tgz
cp ../zips/php/php-7.0.0RC3.tar.gz $RPM_DIR/SOURCES/php-7.0.0RC3.tar.gz

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/php7.spec

rc=$?
if [[ $rc != 0 ]] ; then
    echo "Failed to build rpm PHPCUSTOM"
    exit $rc
fi


. ${startDir}/copyAndRepo.sh






