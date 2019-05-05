import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Project7 {
    public static void main(String[] args){
        Scanner sScan = new Scanner(System.in);
        Scanner dScan = new Scanner(System.in);
        ArrayList<Movie> movieList = new ArrayList<Movie>();
        Boolean found;
        String searchTerm;
        System.out.println("a\tAdd a movie\n" +
                "w\tWatch a movie\n" +
                "r\tUpdate a movie's rating\n" +
                "lw\tList by most watched\n" +
                "lr\tList by rating\n" +
                "q\tQuit\n");
        String choice;
        boolean chooseQuit = false;
        while(!chooseQuit){
            choice= sScan.nextLine();
            switch (choice.toLowerCase()) {
                case "a":
                    System.out.print("Name: ");
                    String name = sScan.nextLine();
                    System.out.print("Rating: ");
                    Double rating = dScan.nextDouble();
                    movieList.add(new Movie(name,rating));
                    System.out.println("Added.");
                    break;
                case "w":
                    System.out.print("Name: ");
                    searchTerm = sScan.nextLine();
                    found = false;
                    for(Movie mov : movieList){
                        if(mov.name.equals(searchTerm)) {
                            found = true;
                            System.out.println("Ok, you watched " + searchTerm + " " + (++mov.timesWatched) + " times now.");
                        }
                    }
                    if (!found) System.out.println("Couldn't find the movie "+searchTerm+". Try adding it.");
                    break;
                case "r":
                    System.out.print("Name: ");
                    searchTerm = sScan.nextLine();
                    for(Movie mov : movieList){
                        if(mov.name.equals(searchTerm)){
                            System.out.print("Ok, New rating:");
                            mov.rating = dScan.nextDouble();
                            System.out.println("Ok. "+mov.name+"'s rating is now a "+mov.rating+".");
                        } else {
                            System.out.println("Couldn't find the movie "+searchTerm+". Try adding it.");
                        }
                    }
                    break;
                case "lw":
                    movieList.sort(new Comparator<Movie>() {
                        @Override
                        public int compare(Movie o1, Movie o2) {
                            return Integer.compare(o1.timesWatched, o2.timesWatched);
                        }
                    });
                    for(Movie mov : movieList){
                        System.out.println(mov.toString());
                    }
                    break;
                case "lr":
                    movieList.sort(new Comparator<Movie>() {
                        @Override
                        public int compare(Movie o1, Movie o2) {
                            return (o1.rating).compareTo(o2.rating);
                        }
                    });
                    for(Movie mov : movieList){
                        System.out.println(mov.toString());
                    }
                    break;
                case "q":
                    chooseQuit = true;
                default:
                    System.out.println("Invalid input");
                    break;

            }
        }
    }
}
