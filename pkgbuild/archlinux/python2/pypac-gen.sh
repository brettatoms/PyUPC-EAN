#!/bin/bash

scriptdir="$(realpath $(dirname $(readlink -f $0)))"
pyscriptfile="${scriptdir}/pypac-gen.py"
pyshellfile="${scriptdir}/pypac-gen.sh"
pythonexec="$(which python2)"
oldwd="$(pwd)"

if [ $# -eq 0 ]; then
 pypacdir="$(${pythonexec} "${pyscriptfile}" -g)"
 pypacparentdir="$(${pythonexec} "${pyscriptfile}" -s "${pypacdir}" -p)"
 pypactarname="$(${pythonexec} "${pyscriptfile}" -s "${pypacdir}" -t)"
 pypacdirname="$(${pythonexec} "${pyscriptfile}" -s "${pypacdir}" -d)"
fi
if [ $# -gt 0 ]; then
 if [ $# -gt 1 ]; then
  codename="${2}"
 fi
 pypacdir="$(${pythonexec} "${pyscriptfile}" -s "${1}" -g)"
 pypacparentdir="$(${pythonexec} "${pyscriptfile}" -s "${pypacdir}" -p)"
 pypactarname="$(${pythonexec} "${pyscriptfile}" -s "${pypacdir}" -t)"
 pypacdirname="$(${pythonexec} "${pyscriptfile}" -s "${pypacdir}" -d)"
fi

cd "${pypacparentdir}"
tar -cavvf "${pypacparentdir}/${pypactarname}" --transform="s/$(basename ${pypacdir})/${pypacdirname}/" "$(basename ${pypacdir})"
file -z -k "${pypacparentdir}/${pypactarname}"
cd "${pypacdir}"
${pythonexec} "${pyscriptfile}" -s "${pypacdir}"
cd "${pypacparentdir}"
mv -v "${pypacparentdir}/${pypactarname}" "$(realpath "${pypacdir}/py2upc-ean")/${pypactarname}"
cd "${oldwd}"
