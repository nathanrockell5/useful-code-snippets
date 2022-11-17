package Number_Guessing_Game;

import java.util.Random;
import java.util.Scanner;


public class Number_Guessing_Game {

	public static void main(String[] args) {
		
		Random rand = new Random();
		int upperBound = 100;
		int guessingNumber = rand.nextInt(upperBound);
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("This is a number guessing game! \n enter a number to guess (hint: it's between 0-" + upperBound+")");
		
		int guess = scanner.nextInt();
		
		while(guess != guessingNumber) {
			if(guess > guessingNumber) {
				System.out.println("Number is lower");
			}else if(guess < guessingNumber) {
				System.out.println("Number is higher");
			}
			guess = scanner.nextInt();
		}
		System.out.println("Correct!");
		scanner.close();
	}
}
