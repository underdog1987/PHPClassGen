#!/usr/bin/python

"""

	PHPClass Generator - A simple class generator for PHP

	Program Name: Generador de clases PHP v0.1
	Author: @underdog1987, 4E27DC Group (@4E27DC) http://facebook.com/ViolentCode
	Usage:
	
		./classgen.py [input file]

	Input file must be a table in a plain text file, using | as column separator.

		classname:ClassName:<final>
		propertyName|set|get

	File example:(person.txt)

		classname:Person:final
		name|set|get
		id|get

	Usage example:

		./classgen.py person.txt

	Output: (Person.php)

		<?php final class Person{
			private $name;
                        public function setName($name){ $this->name=$name;}
                        public function getName(){return $this->name;}

			private $id;
			public function getId(){return $this->id;}
		}

"""

import sys

if len(sys.argv) <= 1:
    print 'Usage %s: [input file]' % sys.argv[0]
    print '  Example: %s MyPHPClass.txt' % sys.argv[0]
    sys.exit(1)

try:
    classParams=open(sys.argv[1],'r')
    lincount=1
    for line in classParams:
        line=line.strip()
        if line.startswith(";"):
            continue;
        if len(line)==0:
            continue;
        if lincount==1:
            l1Params=line.split(':')
            TheClassName = l1Params[1]
            isFinal="final " if l1Params[2]=="final" else ""
            #TO-DO check if file already exists
            phpWritter=open(TheClassName + ".php",'w')
            phpWritter.write("<?php\n")
            phpWritter.write("\t" + isFinal + "class " + TheClassName + "{\n")
            lincount = lincount + 1
        else:
            gettersSettersParams = line.split("|")
            property=gettersSettersParams[0]
            phpWritter.write("\t\tprivate $" + property + ";\n")

            if "set" in gettersSettersParams:            
                phpWritter.write("\t\tpublic function set" + property.upper()[0] + property[1:] + "($" + property + "){ $this->" + property + " = $" + property + "; }\n")
            if "get" in gettersSettersParams:
                phpWritter.write("\t\tpublic function get" + property.upper()[0] + property[1:] + "(){ return $this->" + property + ";}\n\n")

            #print gettersSettersParams[0].upper()[1:]
            
        lincount = lincount + 1

#    if len(sg)>0:
#        a=0
#        for prop in sg:
#            if "set" in gettersSettersParams[a]:
#                print "setter of " + prop
#            if "get" in gettersSettersParams[a]:
#                print "getter of " + prop
#            a = a + 1

    phpWritter.write("\t}\n")
    phpWritter.close()
    print "[+] Check file " + TheClassName + ".php"
except Exception as e:
    if "phpWritter" in locals() or "phpWritter" in globals():
        phpWritter.close()
    print "[!] Cannot continue", e

