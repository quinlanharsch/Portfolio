public class Movie{
    public String name;
    public Double rating;
    public int timesWatched;

    public Movie(String name, double rating){
        this.name = name;
        this.rating = rating;
        this.timesWatched = 1;
    }

    public String toString(){
        return "Title:\t\t"+name+"\nRating:\t\t"+rating+"\nTimes Watched:\t"+timesWatched+"\n";
    }
}
