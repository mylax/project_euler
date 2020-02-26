import java.math.BigInteger;
import java.util.ArrayList;

class QuickStart {
    public static void main(String[] args) {
        BigInteger n = new BigInteger("600851475143");
        System.out.println(find_highest_factor(n));
    }
    public static ArrayList<BigInteger> find_highest_factor(BigInteger n){
        ArrayList<BigInteger> primes = new ArrayList<BigInteger>();
        BigInteger i = new BigInteger("2");
        BigInteger bi2;
        BigInteger bi1 = new BigInteger("0");

        while(true) {
            bi2 = n.mod(i);
            if (bi2.equals(bi1)) {
                n = n.divide(i);
                primes.add(i);
            }
            i = i.add(new BigInteger("1"));
            if (i.compareTo(n) == 1) break;
        }
        return primes;
    }
}