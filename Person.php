<?php
	final class Person{
		private $name;
		public function setName($name){ $this->name = $name; }
		public function getName(){ return $this->name;}

		private $id;
		public function getId(){ return $this->id;}

		private $phone;
		public function setPhone($phone){ $this->phone = $phone; }
		public function getPhone(){ return $this->phone;}

	}
