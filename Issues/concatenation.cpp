// Java program to demonstrate 
// working of concat() method 

class Gfg { 
	public static void main(String args[]) 
	{ 
		String s = "Gfg"; 
		s = s.concat("! is the best."); 
		System.out.println(s); 
	} 
} 

// Java program to demonstrate 
// working of concat() method 

class Gfg { 
	public static void main(String args[]) 
	{ 
		String s = "Gfg"; 

		// We must explicitly assign result 
		// of s.concat() to s. Since not 
		// assigned to s, s does not change. 
		s.concat("! is the best."); 

		System.out.println(s); 
	} 
} 
