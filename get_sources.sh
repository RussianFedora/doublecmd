#!/bin/bash

VERSION=0.5.0
SVN_REVISION=3860

rm -rf doublecmd
echo "Cloning svn $SVN_REVISION"
svn co -r $SVN_REVISION https://doublecmd.svn.sourceforge.net/svnroot/doublecmd/trunk doublecmd >/dev/null
echo "Clean .svn"
find doublecmd -name ".svn" -exec rm -rf {} \; 2>/dev/null

echo "Make tarball $1"
if [ "$1" = "fast" ]
then
    tar c doublecmd | xz > doublecmd-0.5.0-svn$SVN_REVISION.tar.xz
else
    tar c doublecmd | xz --best > doublecmd-0.5.0-svn$SVN_REVISION.tar.xz
fi
