# ----------------------------------------------------------------------------
# pyShift - Cartesian Mesh Rigid Motion
#         - see file license.txt
#
(cd doc;make html)
(cd build; mv html pyShift-html; tar cvf pyShift.html.tar pyShift-html)
cp build/pyShift.html.tar ./doc