# PHPClassGen
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

