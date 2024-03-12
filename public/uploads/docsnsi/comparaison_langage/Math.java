public class Math {
    public static int factorielle(int n) {
	if ( n == 0 )
	    return 1;
        else if  ( n == 1 ) 
            return 1;
	else {
	    int result = 1;
	    int i = 0;
	    while (i < n) {
		i = i + 1;
		result = result * i;
	    }
	    return result;
	}
    }
    
    public static void main(String[] arg) {
	int n = Integer.parseInt(arg[0]);
	System.out.println(Math.factorielle(n));
    }

}
