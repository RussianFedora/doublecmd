#!/bin/bash

ORIGNAME=doublecmd
VERSION=0.5.0
SVN_REVISION=3860
NAME=${ORIGNAME}-${VERSION}.svn${SVN_REVISION}

rm -rf ${ORIGNAME}
svn co -r $SVN_REVISION https://doublecmd.svn.sourceforge.net/svnroot/doublecmd/trunk doublecmd >/dev/null
find ${ORIGNAME} -name ".svn" -exec rm -rf {} \; 2>/dev/null
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
