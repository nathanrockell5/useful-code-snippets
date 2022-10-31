import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {
    /*
     * Complete the 'caesarCipher' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. INTEGER k
     */
    public static String caesarCipher(String s, int k) {
    // Write your code here
        String alphabet = "abcdefghijklmnopqrstuvwxyz";   
        String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String cip = "";
        
        for(int i = 0; i < s.length(); i++){
            if(Character.isLetter(s.charAt(i))){
                if(Character.isUpperCase(s.charAt(i))){
                    int pos = ALPHABET.indexOf(s.charAt(i));   
                    int newPos = (pos+k)%26; 
                    cip+=ALPHABET.charAt(newPos);
                }else{
                    int pos = alphabet.indexOf(s.charAt(i));   
                    int newPos = (pos+k)%26;  
                    cip+=alphabet.charAt(newPos);
                } 
            }else{
                cip += s.charAt(i);
                
            } 
        }
        return cip;
    }

}